"""Reproducible checks for the random quadratic Lagrange tail theorem.
All checks are diagnostics or finite algebraic identities, not an infinite-tail certificate.
"""
import math
import numpy as np
import sympy as sp

z,u,s,t=sp.symbols('z u s t', real=True)
wa=(z-u-s)*(z-u-s-t)/(s*(s+t))
wb=-(z-u)*(z-u-s-t)/(s*t)
wc=(z-u)*(z-u-s)/(t*(s+t))
assert sp.simplify(wa+wb+wc-1)==0
assert sp.simplify(u*wa+(u+s)*wb+(u+s+t)*wc-z)==0
assert sp.simplify(u*u*wa+(u+s)**2*wb+(u+s+t)**2*wc-z*z)==0
assert sp.simplify(sp.limit(s*wa,s,0)-(z-u)*(z-u-t)/t)==0
assert sp.simplify(sp.limit(s*wb,s,0)+(z-u)*(z-u-t)/t)==0
assert sp.simplify(sp.limit(s*wc,s,0))==0
assert sp.simplify(sp.limit(t*wa,t,0))==0
assert sp.simplify(sp.limit(t*wb,t,0)+(z-u)*(z-u-s)/s)==0
assert sp.simplify(sp.limit(t*wc,t,0)-(z-u)*(z-u-s)/s)==0
M=sp.integrate((z-u)**2,(u,0,1))
assert sp.simplify(M-(z*z-z+sp.Rational(1,3)))==0
assert sp.simplify(M.subs(z,sp.Rational(1,2))-sp.Rational(1,12))==0
assert sp.simplify(6*sp.sqrt(2)*M.subs(z,sp.Rational(1,2))-sp.sqrt(2)/2)==0

# Deterministic event-weighted importance sampling: corroboration, not proof.
rng=np.random.default_rng(193)
N=1200000
x=rng.random(N)
L=31.0
g1=np.exp(-L*rng.random(N));g2=np.exp(-L*rng.random(N))
valid=x+g1+g2<=1
for point in [0.5, 0.0]:
    a=(point-x-g1)*(point-x-g1-g2)/(g1*(g1+g2))
    b=-(point-x)*(point-x-g1-g2)/(g1*g2)
    c=(point-x)*(point-x-g1)/(g2*(g1+g2))
    w=np.hypot(np.hypot(a,b),c)
    weights=6*L*L*g1*g2*valid
    expected=6*math.sqrt(2)*(point*point-point+1/3)
    ratios=[]
    for T in [1e4,1e5,1e6,1e7]:
        prob=np.mean(weights*(w>T))
        ratios.append(prob*T/math.log(T))
    # Broad sanity check only, convergence has logarithmic corrections.
    assert all(0.55*expected<v<1.1*expected for v in ratios), (point,ratios,expected)
    print('point=',point,'asymptotic_constant=',expected,'finite-T ratios=',ratios)
print('PASS: 12 exact algebraic checks and bounded diagnostic integrations')
