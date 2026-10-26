"""Finite consistency checks for the real-root perturbation and cosine-grid laws.
The general theorem is proved analytically; these examples are not a substitute.
"""
from math import cos, pi, gcd, isqrt
from sympy import Poly, Rational, S, symbols
x = symbols('x', real=True)

# Exact rational Sturm counts for selected real perturbations.
cases = [
    (5, 2, x**2-1, 2, 1),
    (5, 2, -x**2+1, 2, 1),
    (6, 2, x**2-1, 2, 0),
    (6, 2, -x**2+1, 2, 2),
    (7, 3, x**3-2*x+1, 3, 0),
    (7, 3, -x**3+2*x-1, 3, 2),
]
for n, m, f, finite, exterior in cases:
    # Only use squarefree reference polynomials.
    initial = Poly(f, x).count_roots(-S.Infinity, S.Infinity)
    assert initial == finite, (n, m, f, initial, finite)
    perturbation = Poly(f + Rational(1, 10**18)*x**n, x)
    total = perturbation.count_roots(-S.Infinity, S.Infinity)
    assert total == finite+exterior, (n, m, f, total, finite+exterior)

# The predicted 'outer count' depends only on the top coefficient phases.
angles = [0.017, 0.123, 0.701, 1.227, 2.011]
for n in range(2, 45):
    for m in range(1, n):
        d = n-m
        k = (n+m)//2
        g = gcd(n,k) if d%2 == 0 else None
        L = n//g if g is not None else None
        allowable = {n} if d%2 or L%2==0 else {n-g,n+g}
        for phase in angles:
            signs = [cos(phase+pi*(n+m)*j/n) for j in range(n)]
            assert all(abs(v)>1e-9 for v in signs)
            observed = n if d%2 else 2*sum(s<0 for s in signs)
            assert observed in allowable, (n,m,phase,observed,allowable)

# The explicit fixed-coanalytic-degree example is a strict contradiction
# to the proposed historical equality bound, not to the known n*n upper bound.
n,m = 77,5
assert n*(1+m**0.5) > 249
assert n*(1+m**0.5) < 251
assert (251-n)%2 == 0
assert 251 > 3*n-2+m*(m-1)
assert 251 <= n*n
print('PASS: six exact Sturm cases, 4730 phase-grid instances, degree-(77,5) inequality')
