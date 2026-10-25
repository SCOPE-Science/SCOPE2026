"""Reproduce the polynomial/discriminant and numerical mode classifications."""
import sympy as sp
import numpy as np
u,t,z=sp.symbols('u t z',real=True)
P=z**3-(2*t+2+u)*z**2+(t*t+2*(u-1)*t)*z-u*t*t
Q=4*t**3-(15+12*u)*t**2+(12-78*u+12*u*u)*t+(1-4*u)*(u+2)**2
assert sp.factor(sp.discriminant(P,z)-4*t*t*Q)==0
assert sp.factor(sp.discriminant(Q,t)+629856*u*(2*u-1)**3)==0
assert sp.factor(Q.subs(t,-u)+4*(2*u-1)**3)==0
assert sp.factor(Q.subs(t,-sp.Rational(1,2))+(2*u-1)**2*(4*u+25)/4)==0
assert sp.factor(Q.subs(t,2*(1-u))+27*u*(4*u*u-11*u+8))==0
assert sp.factor(Q.subs(t,0)-(1-4*u)*(u+2)**2)==0
assert sp.factor(P.subs(z,0)+u*t*t)==0
assert sp.factor(P.subs(z,t)+4*t*t)==0
assert sp.factor(Q.subs(u,0)-(t-2)**2*(4*t+1))==0
assert sp.factor(sp.diff(Q,u).subs({t:2,u:0})+216)==0
assert sp.factor(sp.diff(Q,t).subs({t:0,u:sp.Rational(1,4)})+sp.Rational(27,4))==0
assert sp.factor(sp.diff(Q,u).subs({t:0,u:sp.Rational(1,4)})+sp.Rational(81,4))==0

rng=np.random.default_rng(20261024)
counts={'nonoscillatory':0,'oscillatory':0,'neutral':0}
max_residual=0
for j in range(2500):
    uu=float(np.exp(rng.uniform(np.log(.0002),np.log(500))))
    qr=np.roots([4,-(15+12*uu),12-78*uu+12*uu**2,(1-4*uu)*(uu+2)**2])
    positives=sorted(v.real for v in qr if abs(v.imag)<1e-7*max(1,abs(v.real)) and v.real>0)
    assert len(positives)==(2 if uu<.25 else 1),(uu,qr)
    cutoff=positives[-1]
    starts=[cutoff*.13, cutoff*.47, cutoff*.87,cutoff*1.08,cutoff*2.5]
    if len(positives)==2:
        starts.extend([positives[0]*.13,positives[0]*.75,(positives[0]+positives[1])*.5])
    for tt in starts:
        zr=np.roots([1,-(2*tt+2+uu),tt*tt+2*(uu-1)*tt,-uu*tt*tt])
        qq=float(Q.subs({u:uu,t:tt})) if j<3 else float(4*tt**3-(15+12*uu)*tt**2+(12-78*uu+12*uu**2)*tt+(1-4*uu)*(uu+2)**2)
        if tt > cutoff:
            assert min(x.real for x in zr)>-1e-7
            assert max(abs(x.imag) for x in zr)<1e-6*max(1,max(abs(x) for x in zr))
            counts['neutral']+=1
        elif len(positives)==2 and tt<positives[0]:
            assert sum(x.real<0 and abs(x.imag)<1e-7*max(1,abs(x.real)) for x in zr)==2
            assert min(abs(x.imag) for x in zr)<1e-7
            counts['nonoscillatory']+=1
        else:
            assert sum(abs(x.imag)>1e-7*max(1,abs(x.real)) for x in zr)==2,(uu,tt,zr)
            counts['oscillatory']+=1
        for r in zr:
            max_residual=max(max_residual,abs(complex(P.subs({u:uu,t:tt,z:complex(r)})))/max(1,abs(r)**3)) if j<2 else max_residual

for uu in [.00001,.0001,.001,.01]:
    rr=np.roots([4,-(15+12*uu),12-78*uu+12*uu*uu,(1-4*uu)*(uu+2)**2]); pos=sorted(r.real for r in rr if abs(r.imag)<1e-8 and r.real>0)
    assert len(pos)==2
    ratios=[(pos[0]-2)/np.sqrt(uu),(pos[1]-2)/np.sqrt(uu)]
    assert abs(ratios[0]+2*np.sqrt(6))<2.5*np.sqrt(uu)+0.01
    assert abs(ratios[1]-2*np.sqrt(6))<2.5*np.sqrt(uu)+0.01
for eps in [1e-5,1e-4,1e-3]:
    uu=.25-eps
    rr=np.roots([4,-(15+12*uu),12-78*uu+12*uu*uu,(1-4*uu)*(uu+2)**2]); p=sorted(r.real for r in rr if abs(r.imag)<1e-8 and r.real>0)
    assert abs(p[0]/eps-3)<20*eps
print('symbolic identities: PASS (12); configurations: 2500; test groups:',counts,'max sample normalized residual',max_residual)
