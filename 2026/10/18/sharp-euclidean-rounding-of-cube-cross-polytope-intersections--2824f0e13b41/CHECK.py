"""Finite exact checks accompanying the cube/cross-polytope rounding theorem.

Run: python3 CHECK.py. Uses only Python's standard library. Infinite claims
are established in RESULT.md; these finite checks do not prove the theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt


def dot(x, a, y):
    return sum(x[i] * a[i][j] * y[j]
               for i in range(len(x)) for j in range(len(y)))


def inverse(a):
    n = len(a)
    x = [[a[i][j] for j in range(n)]
         + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if x[i][k])
        x[p], x[k] = x[k], x[p]
        u = x[k][k]
        x[k] = [z/u for z in x[k]]
        for i in range(n):
            if i != k:
                v = x[i][k]
                x[i] = [x[i][j]-v*x[k][j] for j in range(2*n)]
    return [row[n:] for row in x]


def contact_vectors(n, t):
    """All maximum-Euclidean-norm vertices of [-1,1]^n cap t B1."""
    k = min(n, int(t))
    f = t-F(k)
    if k == n:
        return list(product((F(-1), F(1)), repeat=n))
    out = set()
    for full in combinations(range(n), k):
        rem = [j for j in range(n) if j not in full]
        for extra in (rem if f else [None]):
            for signs in product((-1, 1), repeat=k+(extra is not None)):
                v = [F(0)]*n
                for i, s in zip(full, signs): v[i] = F(s)
                if extra is not None: v[extra] = f*signs[-1]
                out.add(tuple(v))
    return sorted(out)


def polar_contacts(n, t):
    if t*t >= n:
        return [tuple(F(s if i==j else 0) for i in range(n))
                for j in range(n) for s in (-1,1)]
    return [tuple(F(s,t) for s in signs)
            for signs in product((-1,1), repeat=n)]


def example_spd(n):
    b = [[F((i*7+j*3+1)%5-2) for j in range(n)] for i in range(n)]
    return [[F(int(i==j)) + sum(b[k][i]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


checks = 0
for n in range(2, 8):
    parameters = [F(1), F(7,5), F(9,4), F(n-1), F(n)]
    parameters = sorted(set(t for t in parameters if 1 <= t <= n))
    for t in parameters:
        k = int(t)
        expected_r2 = F(k)+(t-F(k))**2
        vertices = contact_vectors(n, t)
        assert all(sum(abs(v) for v in x) <= t and max(abs(v) for v in x) <= 1
                   for x in vertices)
        assert all(sum(v*v for v in x) == expected_r2 for x in vertices)
        checks += len(vertices)
        # Signed-permutation invariance gives an isotropic contact covariance.
        cov = [[sum(x[i]*x[j] for x in vertices)/len(vertices)
                for j in range(n)] for i in range(n)]
        assert all(cov[i][j] == (expected_r2/F(n) if i==j else 0)
                   for i in range(n) for j in range(n))
        a = example_spd(n)
        ai = inverse(a)
        outer = max(dot(x,a,x) for x in vertices)
        polar = polar_contacts(n,t)
        inner = max(dot(y,ai,y) for y in polar)
        r_inv2 = max(F(1), F(n)/(t*t))
        polar_cov = [[sum(y[i]*y[j] for y in polar)/len(polar)
                      for j in range(n)] for i in range(n)]
        assert all(polar_cov[i][j] == (r_inv2/F(n) if i==j else 0)
                   for i in range(n) for j in range(n))
        assert outer >= expected_r2 * sum(a[i][i] for i in range(n))/n
        assert inner >= r_inv2 * sum(ai[i][i] for i in range(n))/n
        assert outer*inner > expected_r2*r_inv2
        checks += 6

# Strict monotonicity on either side of sqrt(n), including integer breakpoints.
for n in range(2, 120):
    sq = sqrt(n)
    def dist2(t):
        k = min(n, int(t))
        v = k+(t-k)**2
        return v * max(1, n/(t*t))
    xs = sorted(set([1, n, sq] + [k for k in range(1,n)] +
                    [k+z/8 for k in range(1,n) for z in range(1,8)]))
    left = [z for z in xs if z <= sq]
    right = [z for z in xs if z >= sq]
    assert all(dist2(a) > dist2(b)-1e-12 for a,b in zip(left,left[1:]))
    assert all(dist2(a) < dist2(b)+1e-12 for a,b in zip(right,right[1:]))
    checks += len(xs)

assert abs(sqrt(1+(sqrt(2)-1)**2)-1/__import__('math').cos(__import__('math').pi/8)) < 1e-12
print(f"VERIFY_OK exact_contact_checks={checks} dimensions=2..7 monotonicity_dimensions=2..119")
