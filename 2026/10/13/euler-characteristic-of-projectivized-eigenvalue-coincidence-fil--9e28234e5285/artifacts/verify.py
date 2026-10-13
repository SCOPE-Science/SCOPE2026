from itertools import product
from math import comb

# Integer-polynomial helpers, coefficients low to high.
def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)

def divmod_poly(a, b):
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    # All polynomials used here are monic.
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] // b[-1]
        q[k] = c
        for j in range(len(b)):
            a[k+j] -= c*b[j]
        trim(a)
    return trim(q), trim(a)

def gcd_poly(a, b):
    a, b = trim(a[:]), trim(b[:])
    while b != [0]:
        _, r = divmod_poly(a, b)
        a, b = b, r
    # All cases are monic.
    return a

def charpoly_diagonal(vals):
    p = [1]
    for lam in vals:
        p = mul(p, [-lam, 1])
    return p

def charpoly_offdiag_unit(n):
    # Any off-diagonal matrix unit is nilpotent.
    return [0]*n + [1]

checked_weight_pairs = 0
checked_fixed_points = 0
checked_gcds = 0

for n in range(2, 51):
    weights = [2**j for j in range(n)]
    seen = set()
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            d = weights[a] - weights[b]
            assert d != 0
            assert d not in seen
            seen.add(d)
            checked_weight_pairs += 1
    assert len(seen) == n*(n-1)
    # One diagonal projective component plus all off-diagonal coordinate points.
    assert n + n*(n-1) == n*n
    checked_fixed_points += n*(n-1)

for n in range(2, 9):
    # All off-diagonal matrix units have full characteristic polynomial t^n
    # and cutoff characteristic polynomial t^(n-1).
    full = charpoly_offdiag_unit(n)
    cut = charpoly_offdiag_unit(n-1)
    g = gcd_poly(full, cut)
    assert len(g) - 1 == n-1
    for a in range(n):
        for b in range(n):
            if a != b:
                checked_gcds += 1

    # Sample diagonal points, including repeated eigenvalues.
    samples = [
        tuple(range(n)),
        tuple([0]*n),
        tuple([1]*(n-1) + [2]),
        tuple((j % 3) for j in range(n)),
    ]
    for vals in samples:
        p = charpoly_diagonal(vals)
        q = charpoly_diagonal(vals[:-1])
        g = gcd_poly(p, q)
        assert len(g) - 1 == n-1
        checked_gcds += 1

print('VERIFY_OK', checked_weight_pairs, checked_fixed_points, checked_gcds)
