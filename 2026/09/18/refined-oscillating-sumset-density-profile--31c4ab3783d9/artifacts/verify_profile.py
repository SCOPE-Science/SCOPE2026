from itertools import product
from math import floor, gcd, log, exp, sqrt

# Exact CRT-union check for the set of residue vectors with at most one failed coordinate.
qs = [11, 13, 17]
delta = 0.10
Ds = [set(range(2 * floor(delta*q) + 1)) for q in qs]
Q = 1
for q in qs:
    Q *= q

count = 0
for n in range(Q):
    successes = sum((n % q) in D for q, D in zip(qs, Ds))
    if successes >= len(qs)-1:
        count += 1

sizes = [len(D) for D in Ds]
formula_count = 1
for s in sizes:
    formula_count *= s
for j, q in enumerate(qs):
    term = q - sizes[j]
    for i, s in enumerate(sizes):
        if i != j:
            term *= s
    formula_count += term
assert count == formula_count

print(f"CRT sample: Q={Q}, direct_count={count}, formula_count={formula_count}")

# Refined theorem constant versus the earlier union-bound constant.
for r, d in [(2, 0.10), (3, 0.10), (5, 0.08), (8, 0.05)]:
    theta = 2*d
    refined = r*theta**(r-1) - (r-1)*theta**r
    previous = (r+1)*theta**(r-1)
    assert refined < previous
    print(f"r={r:2d}, delta={d:.3f}: refined={refined:.12g}, previous={previous:.12g}")

# Optimize the refined alpha-envelope in logarithmic coordinates.
a = log(2.0)
for L in [100.0, 400.0, 1600.0, 6400.0]:
    best = None
    best_r = None
    # delta=alpha^(1/r)<1/4 is equivalent to L/r>log 4.
    max_r = int(L/log(4.0))
    for r in range(2, max_r+1):
        delta = exp(-L/r)
        bracket = r - 2*(r-1)*delta
        log_ratio = (r-1)*a + L/r + log(bracket)
        if best is None or log_ratio < best:
            best = log_ratio
            best_r = r
    asymp = 2*sqrt(a*L) + 0.5*log(L/a) - a
    print(f"L={L:7.1f}: best_r={best_r:3d}, log(B/alpha)={best:.12f}, asymptotic={asymp:.12f}, diff={best-asymp:.6g}")
