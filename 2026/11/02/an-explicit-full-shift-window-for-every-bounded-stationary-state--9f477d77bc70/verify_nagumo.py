#!/usr/bin/env python3
"""Check exact cubic-Nagumo cutoff identities and sample cycles. Requires sympy/numpy."""
import sympy as S
import numpy as np
z=S.sqrt(3)
r=(3-z)/12
m=z/8
d=(4*z-3)/416
x=S.symbols('x',real=True)
g=x*(1-x)*(x-S.Rational(1,2))
gp=S.diff(g,x)
assert S.simplify(2*d*(1+2*r)-r*m)==0
assert S.simplify(4*d/m-(4-z)/13)==0
assert S.simplify(gp.subs(x,r)+m)==0
assert S.simplify(gp.subs(x,S.Rational(1,2)-r)-m)==0
assert S.simplify(gp.subs(x,S.Rational(1,2)+r)-m)==0
assert 0<float(4*d/m)<1
# Each branch is monotone and its critical derivative magnitude is >= m:
for center in (0,.5,1):
    xs=np.linspace(center-float(r),center+float(r),1001)
    deriv=-3*xs**2+3*xs-.5
    assert min(abs(deriv))>float(m)-1e-12
for n in (3,5,13,37):
    for seed in range(4):
        rng=np.random.default_rng(seed+n)
        code=rng.choice([0,.5,1],n).astype(float)
        u=code.copy()
        coupling=.99*float(d)
        for k in range(300):
            target=-coupling*(np.roll(u,1)-2*u+np.roll(u,-1))
            v=code.copy()
            for j in range(10):
                v+=(target-v*(1-v)*(v-.5))/(-3*v*v+3*v-.5)
            if np.max(np.abs(v-u))<1e-15:
                u=v
                break
            u=v
        residual=coupling*(np.roll(u,1)-2*u+np.roll(u,-1))+u*(1-u)*(u-.5)
        assert np.max(np.abs(residual))<1e-12
        assert np.max(np.abs(u-code))<float(r)
print('PASS: exact identities, derivative certificate and sixteen cyclic checks')
