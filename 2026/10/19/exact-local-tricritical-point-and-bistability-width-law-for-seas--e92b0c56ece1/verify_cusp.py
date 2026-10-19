"""Reproduce the local bifurcation coefficients for seasonal mutualistic viability.

Requires sympy and mpmath. This checks formal series and numerical witnesses;
finite-precision checks are supporting evidence, not a substitute for the proof.
"""
import sympy as sp
import mpmath as mp

q, z, m, c = sp.symbols('q z m c', real=True)
s = z*q - z**2*q**2/2 + z**3*q**3/6
B = c * sp.series(s*(1+m*s)*sp.exp(m*s), q, 0, 4).removeO()
G = sp.series(1-sp.exp(-z*B), q, 0, 4).removeO().expand()
coeff = {j: sp.factor(G.coeff(q,j)) for j in (1,2,3)}
assert sp.simplify(coeff[1]-c*z**2)==0
assert sp.simplify(coeff[2]+c*z**3*(c*z-4*m+1)/2)==0
assert sp.simplify(coeff[3]-c*z**4*(c**2*z**2-12*c*m*z+3*c*z+9*m*m-12*m+1)/6)==0
crit_2 = sp.factor(coeff[2].subs(c,1/z**2))
assert sp.simplify(crit_2-(z*(4*m-1)-1)/2)==0
crit_3=sp.factor(coeff[3].subs(c,1/z**2).subs(z,1/(4*m-1)))
D=(23*m*m-4*m+1)/(6*(4*m-1)**2)
assert sp.simplify(crit_3+D)==0

mp.mp.dps=60
fm=lambda x: (4*x-1)*mp.sqrt((1+x)*mp.exp(x))-1
mstar=mp.findroot(fm, (mp.mpf('.35'),mp.mpf('.48')))
zstar=mp.sqrt((1+mstar)*mp.exp(mstar))
Dstar=(23*mstar*mstar-4*mstar+1)/(6*(4*mstar-1)**2)
b1=2*zstar+(mstar+2)/(4*(1+mstar))
A=mp.sqrt(2/(zstar*Dstar))
W=zstar*b1*b1/(8*Dstar)
assert 0<mstar<1 and Dstar>0 and b1>0
assert abs(fm(mstar))<mp.mpf('1e-50')

def zcrit(mm):return mp.sqrt((1+mm)*mp.exp(mm))
def f(q,zz,mm):
    ss=-mp.expm1(-zz*q)
    bb=ss*(1+mm*ss)*mp.exp(mm*(ss-1))/(1+mm)
    return -mp.expm1(-zz*bb)-q

def g(q,zz,mm):
    if not q:
        return mp.exp(-mm)*zz*zz/(1+mm)-1
    return f(q,zz,mm)/q

# At the tricritical point the small positive root has square-root scaling.
for e in (mp.mpf('1e-3'),mp.mpf('1e-5'),mp.mpf('1e-7')):
    root=mp.findroot(lambda x:g(x,zstar+e,mstar), (A*mp.sqrt(e)/2,A*mp.sqrt(e)*2), solver='bisect')
    assert root>0 and abs(root/mp.sqrt(e)-A)<mp.mpf('1.0')*mp.sqrt(e)

# Saddle-node position and width in the m>mstar local wedge.
for eta in (mp.mpf('.02'),mp.mpf('.01'),mp.mpf('.005')):
    mm=mstar+eta
    zc=zcrit(mm)
    q0=(b1/(2*Dstar))*eta
    z0=zc-W*eta**2
    qf,zf=mp.findroot((lambda x,y:g(x,y,mm), lambda x,y:mp.diff(lambda t:g(t,y,mm),x)),(q0,z0))
    assert qf>0 and zf<zc
    assert abs((zc-zf)/eta**2-W)<mp.mpf('10')*eta
    assert abs(qf/eta-b1/(2*Dstar))<mp.mpf('10')*eta
    # Between fold and zero-state instability: three fixed points locally.
    zm=(zf+zc)/2
    lo=mp.findroot(lambda x:g(x,zm,mm),(qf*mp.mpf('.01'),qf),solver='bisect')
    hi=mp.findroot(lambda x:g(x,zm,mm),(qf,qf*2),solver='bisect')
    assert 0<lo<qf<hi
    assert mp.diff(lambda t:f(t,zm,mm),lo)>0
    assert mp.diff(lambda t:f(t,zm,mm),hi)<0
    assert g(0,zm,mm)<0
print('Symbolic coefficients, cusp scaling and local fold checks passed.')
for n,x in [('mean lifetime at cusp',1+mstar),('mean degree at cusp',zstar),('cubic magnitude',Dstar),('sqrt scaling amplitude',A),('bistable-width coefficient',W)]:
    print(n,mp.nstr(x,21))
