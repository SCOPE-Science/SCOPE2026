"""Independent exact matrix and low-dimensional cap checks for a simplex radial-volume theorem.
Run: python3 verify_simplex_thresholds.py
Uses sympy. The checks are finite corroboration, not an all-dimensional proof.
"""
import math
import sympy as sp

checks = 0
for d in range(2, 16):
    for k in range(1, d + 1):
        G = (sp.Rational(d+1,d)*sp.eye(k) - sp.ones(k)/d)
        inv = G.inv()
        a = sp.Rational(d, d-k+1)
        det = (sp.Rational(d+1,d)**(k-1))*sp.Rational(d-k+1,d)
        expected_inv = sp.Rational(d,d+1)*sp.eye(k) + sp.Rational(d,(d+1)*(d-k+1))*sp.ones(k)
        assert G.det() == det
        assert inv == expected_inv
        assert inv*sp.ones(k,1) == a*sp.ones(k,1)
        assert (sp.ones(1,k)*inv*sp.ones(k,1))[0] == sp.Rational(d*k,d-k+1)
        checks += 4
    for k in range(1, d):
        assert sp.Rational(d*k,d-k+1) < sp.Rational(d*(k+1), d-k)
        checks += 1

# Unit-ball cap beyond one tangent hyperplane in 3D.
# Exact volume = pi*(t-1)^2*(2*t+1)/3. The predicted leading
# coefficient at the first onset is pi (t-1)^2.
d=3;k=1
alpha=sp.Rational(d,d-k+1)
gdet=(sp.Rational(d+1,d)**(k-1))*sp.Rational(d-k+1,d)
r=sp.sqrt(sp.Rational(d*k,d-k+1))
coefficient = (sp.pi**sp.Rational(d-k,2)*(2*r)**sp.Rational(d+k,2)
               / ((2*alpha)**k*sp.sqrt(gdet)*sp.gamma(sp.Rational(d+k,2)+1)))
assert sp.simplify(coefficient-sp.pi)==0
assert sp.limit((sp.pi*(sp.Symbol('t')-1)**2*(2*sp.Symbol('t')+1)/3)
                /(sp.Symbol('t')-1)**2,sp.Symbol('t'),1,dir='+')==sp.pi
checks += 2

# An independent circular-segment expansion in 2D.
d=2;k=1
alpha=sp.Rational(d,d-k+1); gdet=sp.Rational(d-k+1,d)
r=sp.sqrt(sp.Rational(d*k,d-k+1))
c = (sp.pi**sp.Rational(d-k,2)*(2*r)**sp.Rational(d+k,2)
     /((2*alpha)**k*sp.sqrt(gdet)*sp.gamma(sp.Rational(d+k,2)+1)))
assert sp.simplify(c-4*sp.sqrt(2)/3)==0
for eps in (1e-3, 1e-4, 1e-5):
    t=1+eps
    exact=t*t*math.acos(1/t)-math.sqrt(t*t-1)
    assert abs(exact/(eps**1.5)-float(c))/float(c)<0.002
    checks += 1

print('PASS',checks,'checks (Gram inverses, distances, thresholds, and cap coefficients)')
