"""Standalone symbolic and high-precision checks for triangular softplus equilibrium curvature.
Requires sympy and mpmath. This script tests consequences of the analytic proof,
not a substitute for the proof of the global suprema.
"""
import random
import sympy as sp
import mpmath as mp

q, t, s = sp.symbols('q t s', positive=True)
d = 1-q*t
D = sp.diag(t,s)
W = sp.Matrix([[q,0],[q,0]])
A = sp.Matrix([1,1])
S = (sp.eye(2)-D*W).inv()
J = S*D*A
v = A+W*J
gamma = sp.Matrix([t*(1-t),s*(1-s)])
K = S * sp.Matrix([gamma[i]*v[i]**2 for i in range(2)])
H2 = s*(1-s)/d**2 + q*s*t*(1-t)/d**3
H1 = t*(1-t)/d**3
sopt=(1-q*t**2)/(2*d)
R=(1-q*t**2)/d**2
assert sp.simplify(K[1]-H2)==0
assert sp.simplify(K[0]-H1)==0
assert sp.simplify(H2-s*(1-q*t**2-d*s)/d**3)==0
assert sp.simplify(H2.subs(s,sopt)-(1-q*t**2)**2/(4*d**4))==0
assert sp.simplify(sp.diff(R,t)-2*q*(1-t)/d**3)==0
assert sp.simplify(sp.diff(H1,t)-(1-2*(1-q)*t-q*t*t)/d**4)==0
assert sp.simplify((2*d-(1-q*t*t))-((1-q)+q*(t-1)**2))==0
assert sp.simplify(H2.subs(s,1)-q*t*(1-t)/d**3)==0

mp.mp.dps=70
rnd=random.Random(20261022)
for _ in range(1500):
    qv=mp.mpf(rnd.randrange(1,9999))/10000
    tv=mp.mpf(rnd.randrange(1,9999))/10000
    sv=mp.mpf(rnd.randrange(1,9999))/10000
    dv=1-qv*tv
    direct=(sv*(1-sv)/dv**2 + qv*sv*tv*(1-tv)/dv**3)
    maxim=(1-qv*tv**2)**2/(4*dv**4)
    bound=1/(4*(1-qv)**2)
    assert direct>0 and direct<=maxim+mp.mpf('1e-58')
    assert maxim<bound
    svopt=(1-qv*tv**2)/(2*dv)
    assert 0<svopt<1
    assert mp.almosteq((svopt*(1-svopt)/dv**2 + qv*svopt*tv*(1-tv)/dv**3),maxim,rel_eps=mp.mpf('1e-58'))
    tonestar=1/((1-qv)+mp.sqrt((1-qv)**2+qv))
    assert 0<tonestar<1
    # Grid-perturb test, supplementary only; the analytic sign argument is decisive.
    h1star=tonestar*(1-tonestar)/(1-qv*tonestar)**3
    h1v=tv*(1-tv)/(1-qv*tv)**3
    assert h1v<=h1star+mp.mpf('1e-58')

for gap in ['0.1','0.01','0.001','0.00001','0.0000001']:
    eps=mp.mpf(gap); qq=1-eps
    star=1/(eps+mp.sqrt(eps**2+qq))
    one=eps**2*star*(1-star)/(1-qq*star)**3
    assert abs(one-mp.mpf(4)/27) < 2*mp.sqrt(eps)
    # Choosing t near 1 and the optimizing s gives the exact family envelope.
    tt=1-eps**3
    dd=1-qq*tt
    val=eps**2*(1-qq*tt**2)**2/(4*dd**4)
    assert val < mp.mpf(1)/4
    assert abs(val-mp.mpf(1)/4) < 2*eps**2

# Direct high-precision finite-difference check from independently reconstructed
# exact equilibria, avoiding the closed-form derivative formula.
for qq,tt,ss in [('0.2','0.3','0.65'),('0.7','0.8','0.4'),('0.91','0.96','0.55')]:
    qq,tt,ss=map(mp.mpf,(qq,tt,ss))
    z1=-mp.log(1-tt)
    b1=mp.log(tt/(1-tt))-qq*z1
    b2=mp.log(ss/(1-ss))-qq*z1
    def u(xx):
        z=mp.findroot(lambda z: z-mp.log(1+mp.exp(qq*z+xx+b1)),z1,solver='newton',tol=mp.mpf('1e-60'))
        return mp.log(1+mp.exp(qq*z+xx+b2))
    step=mp.mpf('0.0000001')
    fd=(u(step)-2*u(0)+u(-step))/step**2
    theoretical=ss*(1-ss)/(1-qq*tt)**2+qq*ss*tt*(1-tt)/(1-qq*tt)**3
    assert abs(fd-theoretical)<mp.mpf('0.00000001')

print('PASS: 7 symbolic identities; 1500 parameter triples; 5 singular-gap tests; 3 independent equilibrium finite-difference comparisons')
