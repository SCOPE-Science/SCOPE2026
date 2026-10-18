"""Exact algebraic tests for the Gaussian SRK-I/SRK-II theorem.

Run: python3 verify.py (requires SymPy).
The universal statements are proved analytically in RESULT.md.
"""
from fractions import Fraction
import sympy as sp

h, lam, x, j, db, z = sp.symbols('h lam x j db z', real=True)
rt2 = sp.sqrt(2)
g = lambda t: lam * t
stage_i = x - 3*h*g(x)/4 + 3*rt2*j/(2*h)
out_i = x - h*g(x)/3 - 2*h*g(stage_i)/3 + rt2*db
stage_p = x - h*g(x)/2 + rt2*(1+1/rt2)*j/h
stage_m = x - h*g(x)/2 + rt2*(1-1/rt2)*j/h
out_ii = x - h*(g(stage_p)+g(stage_m))/2 + rt2*db
R = 1-z+z*z/2
canonical = R.subs(z,h*lam)*x + rt2*(db-lam*j)
checks = 0
for expr in (out_i, out_ii):
    assert sp.simplify(expr-canonical)==0
    checks += 1

# Brownian increment and integral moments give Q=2h(1-z+z*z/3).
Q = sp.expand(2*(h - lam*h*h + lam*lam*h*h*h/3))
assert sp.simplify(Q-2*h*(1-z+z*z/3).subs(z,h*lam))==0
checks += 1

numer = 1-z+z*z/3
den = 1-z+z*z/2-z*z*z/8
f = sp.factor(numer/den)
assert sp.simplify(f-1-z*z*(3*z-4)/(24*den))==0
checks += 1
assert sp.factor(1-R*R) == sp.factor(2*z*den)
checks += 1
assert sp.simplify(R.subs(z,sp.Rational(4,3))-sp.Rational(5,9)) == 0
checks += 1
assert sp.simplify(f.subs(z,sp.Rational(4,3))-1)==0
checks += 1
assert sp.simplify(sp.Rational(4,3)*(1+sp.Rational(5,9))/(1-sp.Rational(5,9))/2-sp.Rational(7,3))==0
checks += 1

# Independent exact-rational stage evaluation, not using canonical RHS for stages.
for H in (Fraction(1,8), Fraction(1,4), Fraction(2,3), Fraction(3,4), Fraction(4,3), Fraction(7,4)):
    for L in (Fraction(1,3), Fraction(2,3), Fraction(1), Fraction(2), Fraction(5,2)):
        for X in (Fraction(-7,5), Fraction(-1), Fraction(0), Fraction(5,11), Fraction(17,4)):
            # Represent Brownian components multiplied by sqrt(2) with rational B and J.
            for J, B in ((Fraction(-3,7),Fraction(9,5)),(Fraction(0),Fraction(0)),(Fraction(5,4),Fraction(-2,3))):
                si = X - 3*H*L*X/4 + 3*J/(2*H)
                vi = X-H*L*X/3-2*H*L*si/3+B
                # For the two symmetric stages, only the average is needed.
                smean = X-H*L*X/2+J/H
                vii = X-H*L*smean+B
                vr = (1-H*L+(H*L)**2/2)*X + B-L*J
                assert vi==vii==vr
                checks += 1

# Exact stationary and finite-horizon variance for stable scalar examples.
for Z in (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1),sp.Rational(4,3),sp.Rational(7,4)):
    r=sp.factor(R.subs(z,Z))
    q=sp.factor(2*Z*numer.subs(z,Z)) # h=Z, curvature lambda=1
    sig=sp.factor(q/(1-r*r))
    assert sig==sp.factor(f.subs(z,Z))
    for N in (2,3,4,7,17):
        cov_sum=sp.factor(sig*(N+2*sum((N-k)*r**k for k in range(1,N)))/N**2)
        # Construct autoregression covariance directly by covariance of stationary Gaussian data.
        entries=sp.Matrix([[sig*r**abs(a-b) for b in range(N)] for a in range(N)])
        direct=sp.factor((sp.ones(1,N)*entries*sp.ones(N,1))[0]/N**2)
        assert direct==cov_sum
        checks += 1
print('PASS:',checks,'exact symbolic and rational comparisons')
