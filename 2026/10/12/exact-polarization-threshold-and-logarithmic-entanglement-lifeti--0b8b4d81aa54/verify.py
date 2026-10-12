"""Direct algebraic and matrix checks of transient entanglement in a two-qubit collision model."""
import math
import numpy as np
import sympy as sp

# Algebra independent of floating-point experiments.
p,a,q,h,m=sp.symbols('p a q h m',real=True)
eta=q*(1-q)
b=1-a
d00=a*(1-p); d11=b*p; d01=b*(1-p); d10=a*p
pout=sp.expand(p*a + (1-q)*d00 + q*d11)
assert sp.simplify(pout-(q*p+(1-q)*a))==0
D=4*eta*m*m*h*h-(1-m*m)*(1-m*m*(1-h)**2)
Df=m*m*(4*eta+1-m*m)*h*h - 2*(1-m*m)*m*m*h -(1-m*m)**2
assert sp.expand(D-Df)==0
# Negativity matches the PPT block formula at each step.
pj=(1+m*(1-h))/2
assert sp.expand((d01+d10).subs({p:pj,a:(1+m)/2})-(1+m*m*(1-h))/2)==0
assert sp.expand((d01-d10).subs({p:pj,a:(1+m)/2})+m*(2-h)/2)==0
assert sp.expand((p-a).subs({p:pj,a:(1+m)/2})+m*h/2)==0
# Solve the full quadratic in h via the proposed positive root (introducing y).
y=sp.symbols('y',real=True)
Dpoly=sp.expand(Df.subs(eta,(y*y-1)/4))
hpos=(1-m*m)/(m*(y-m))
hneg=-(1-m*m)/(m*(y+m))
assert sp.factor(Dpoly-m*m*(y*y-m*m)*(h-hpos)*(h-hneg))==0

rng=np.random.default_rng(20261010)
H=np.zeros((4,4),complex); H[0,3]=H[3,0]=1
I=np.eye(4,dtype=complex)
count=0
for _ in range(1800):
    mm=float(rng.uniform(0,1)); theta=float(rng.uniform(.004,math.pi/2-.004))
    qq=math.cos(theta)**2
    t=math.sin(theta)*math.cos(theta)
    a0=(1+mm)/2
    anc=np.diag([a0,1-a0]); U=I+(math.cos(theta)-1)*H@H-1j*math.sin(theta)*H
    # diagonal target is rebuilt recursively, not from the closed form.
    ps=np.eye(2,dtype=complex)/2
    for k in range(1,8):
        initial=np.kron(ps,anc)
        joint=U@initial@U.conj().T
        # independent partial transpose calculation (ancilla subsystem)
        pt=joint.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        mineig=np.linalg.eigvalsh(pt).min()
        negativity=max(0.,-float(mineig))
        hh=qq**(k-1)
        claimed=max(0.,(mm*math.sqrt((2-hh)**2+4*qq*(1-qq)*hh*hh)-1-mm*mm*(1-hh))/4)
        if not math.isclose(negativity,claimed,abs_tol=4e-13):
            raise AssertionError((mm,theta,k,negativity,claimed))
        if 0<mm<1:
            crit=(1-mm*mm)/(mm*(math.sqrt(1+4*qq*(1-qq))-mm))
            if abs(hh-crit)>1e-9:
                assert (negativity>1e-12)==(hh>crit), (mm,theta,k,hh,crit,negativity)
        # independently trace out the ancilla for the next cycle
        ps=np.array([[joint[0,0]+joint[1,1],joint[0,2]+joint[1,3]],
                     [joint[2,0]+joint[3,1],joint[2,2]+joint[3,3]]])
        count+=1

# Handpicked near-threshold and pure-bath cases.
for mm in [0.,1/math.sqrt(2),.8,.9,1.]:
    q0=.5;y0=math.sqrt(1+4*q0*(1-q0))
    vals=[max(0,(mm*math.sqrt((2-q0**j)**2+q0**(2*j))-(1+mm*mm*(1-q0**j)))/4) for j in range(10)]
    assert all(v>=0 for v in vals)
    if mm<=1/math.sqrt(2): assert max(vals)<1e-13
    if mm==1: assert min(vals)>0
    if mm==.9:assert vals[0]>0 and vals[1]>0 and max(vals[2:])==0

print('VERIFY_OK',count,'matrix comparisons; symbolic identities passed')
