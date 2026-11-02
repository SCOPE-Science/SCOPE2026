"""Exact algebraic verification for a six-pattern permutation rank statistic.

Run: python verify_null_limit.py
Requires: sympy. All integrals are symbolic over rational polynomials.
The limit theorem additionally uses the standard Hoeffding decomposition
and canonical order-two U-statistic spectral convergence.
"""
from itertools import combinations, permutations
from math import comb, factorial, lcm
from fractions import Fraction
import sympy as sp

PATTERNS = {
    "123": sp.Integer(1), "321": sp.Integer(1),
    "2143": sp.Integer(1), "3412": sp.Integer(1),
    "2413": sp.Rational(1, 2), "3142": sp.Rational(1, 2),
}
x, u, y, v = sp.symbols("x u y v", real=True)


def ranked_pairs(k, left, right):
    for i in range(1, k):
        for j in range(i + 1, k + 1):
            a, b, c = i - 1, j - i - 1, k - j
            prob = (sp.factorial(k - 2) * left**a * (right-left)**b
                    * (1-right)**c / (sp.factorial(a)*sp.factorial(b)*sp.factorial(c)))
            yield i, j, prob


def one_point(k, a, b):
    rank_a = [sp.binomial(k-1, i) * a**i * (1-a)**(k-1-i) for i in range(k)]
    rank_b = [sp.binomial(k-1, i) * b**i * (1-b)**(k-1-i) for i in range(k)]
    total = 0
    for pattern, weight in PATTERNS.items():
        if len(pattern) == k:
            total += weight * sum(rank_a[i] * rank_b[int(pattern[i])-1]
                                  for i in range(k)) / factorial(k-1)
    return sp.expand(total)


def two_points_same_order(k):
    """Conditional expectation on the chamber x<u and y<v."""
    ans = 0
    for i, j, px in ranked_pairs(k, x, u):
        for ell, m, py in ranked_pairs(k, y, v):
            for pattern, weight in PATTERNS.items():
                if len(pattern) == k and int(pattern[i-1]) == ell and int(pattern[j-1]) == m:
                    ans += weight * px * py / factorial(k-2)
    return sp.expand(ans)


L = lambda t: 6*t*t - 6*t + 1
eta3 = one_point(3, x, y)
eta4 = one_point(4, x, y)
assert sp.simplify(eta3 - sp.Rational(1, 3) - L(x)*L(y)/6) == 0
assert sp.simplify(eta4 - sp.Rational(1, 8) + L(x)*L(y)/8) == 0
assert sp.simplify(3*eta3 + 4*eta4 - sp.Rational(3, 2)) == 0

h3 = two_points_same_order(3)
h4 = two_points_same_order(4)
kern = sp.expand(
    3*(h3 - eta3 - one_point(3, u, v) + sp.Rational(1, 3))
    + 6*(h4 - eta4 - one_point(4, u, v) + sp.Rational(1, 8))
)
assert kern.subs({x:sp.Rational(1,4), u:sp.Rational(3,4),
                  y:sp.Rational(1,4), v:sp.Rational(3,4)}) == sp.Rational(5,32)

# Independent coordinate reversals preserve the set of weighted patterns.
for p, weight in PATTERNS.items():
    assert PATTERNS[p[::-1]] == weight
    assert PATTERNS[''.join(str(len(p)+1-int(z)) for z in p)] == weight

# Integrate K^2 over x<u, y<v. Four order chambers contribute equally.
quadrant = sp.Integer(0)
for (a,b,c,d), coef in sp.Poly(kern*kern, x,u,y,v).terms():
    quadrant += coef/(sp.Integer(a+1)*(a+b+2)*(c+1)*(c+d+2))
quadrant = sp.factor(quadrant)
assert quadrant == sp.Rational(121,14400)
assert 4*quadrant == sp.Rational(121,3600)
assert 8*quadrant == sp.Rational(121,1800)

# Exhaustive finite-permutation means and variances, independent of the integral.
pattern_weights_twice = {tuple(map(int,p)):int(2*w) for p,w in PATTERNS.items()}
expected = {
    4:Fraction(41,576), 5:Fraction(299,14400),
    6:Fraction(6137,648000), 7:Fraction(2677,504000),
}
for n, target_variance in expected.items():
    triple_indices = list(combinations(range(n), 3))
    quad_indices = list(combinations(range(n), 4))
    den = lcm(comb(n,3),comb(n,4))
    histogram = {}
    for perm in permutations(range(n)):
        score2den = 0
        for inds, k in ((triple_indices, 3), (quad_indices,4)):
            multiplier = den // comb(n,k)
            for index in inds:
                values = [perm[t] for t in index]
                pattern = tuple(1 + sum(z < val for z in values) for val in values)
                score2den += multiplier*pattern_weights_twice.get(pattern,0)
        histogram[score2den] = histogram.get(score2den,0)+1
    count = factorial(n)
    mean = Fraction(sum(val*f for val,f in histogram.items()),2*den*count)
    variance = (Fraction(sum(val*val*f for val,f in histogram.items()),(2*den)**2*count)
                - mean*mean)
    assert mean == Fraction(11,24)
    assert variance == target_variance
    print(f"n={n}: exact mean={mean}, variance={variance}")
print("First Hoeffding projection: zero; canonical second kernel: nonzero")
print(f"One order-chamber integral of K^2: {quadrant}")
print(f"Full Hilbert-Schmidt norm squared: {4*quadrant}")
print(f"Asymptotic n^2 variance coefficient: {8*quadrant}")
print("All exact algebraic checks passed")
