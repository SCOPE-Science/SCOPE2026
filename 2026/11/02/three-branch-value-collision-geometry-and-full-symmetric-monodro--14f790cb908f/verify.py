"""Exact consistency tests for the sparse logarithmic critical-point covers."""
import sympy as sp

r, t, e = sp.symbols('r t e')
for q in range(3, 9):
    eq = (-1)**q * sp.Rational((q-1)**(q-1), q**q)
    f = 1 + t + e*t**q
    P = e*(r+q)*t**q + (r+1)*t + r
    R = -t*sp.diff(f, t)/f
    N = 1 + q**2*e*t**(q-1) + (q-1)**2*e*t**q
    assert sp.cancel(sp.diff(R, t) + N/f**2) == 0
    assert sp.expand(r*f + t*sp.diff(f, t) - P) == 0
    assert sp.cancel(N.subs(t, -sp.Rational(q, q-1)) - (1-e/eq)) == 0
    assert sp.cancel(R + q - (q+(q-1)*t)/f) == 0
    D = (-1)**q*(q-1)**(q-1)*(r+1)**q - q**q*e*r**(q-1)*(r+q)
    disc = sp.discriminant(P, t)
    quotient = sp.factor(disc / ((e*(r+q))**(q-2)*D))
    assert quotient in [1, -1]
    E = eq*(r+1)**q/(r**(q-1)*(r+q))
    assert sp.cancel(sp.diff(E, r)/E + q*(q-1)/(r*(r+1)*(r+q))) == 0
    assert sp.factor(D.subs(e, E)) == 0
print('VERIFY_OK')
