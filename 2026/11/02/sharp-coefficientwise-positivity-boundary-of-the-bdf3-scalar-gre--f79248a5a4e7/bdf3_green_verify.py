"""Exact arithmetic verification of a BDF3 Green-sequence positivity theorem.

Run: python3 bdf3_green_verify.py
Uses only Python's standard library. The proof's infinite-step argument
is the inductive recurrence identity and the stated root comparison;
finite evaluations do not substitute for those arguments.
"""
from fractions import Fraction as F
from math import comb


def clean(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    return clean([(p[i] if i < len(p) else 0) +
                  (q[i] if i < len(q) else 0)
                  for i in range(max(len(p), len(q)))])


def scale(c, p):
    return clean([c * v for v in p])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return clean(out)


def sub(p, q):
    return add(p, scale(-1, q))


def sh(p, k):
    return clean([0] * k + list(p))


def evalp(p, y):
    a = 0
    for c in reversed(p):
        a = a * y + c
    return a


def bernstein(p, left, right):
    """Exact coefficients of p(left+(right-left)t) in Bernstein basis."""
    left, right = F(left), F(right)
    q = (F(0),)
    affine = (left, right - left)
    for c in reversed(p):
        q = add(mul(q, affine), (F(c),))
    n = len(p) - 1
    q = tuple(F(q[i]) if i < len(q) else F(0) for i in range(n + 1))
    return tuple(sum((q[i] * F(comb(k, i), comb(n, i))
                      for i in range(k + 1)), F(0))
                 for k in range(n + 1))


def positive(p, left, right, label):
    b = bernstein(p, left, right)
    assert all(c > 0 for c in b), (label, b)
    return min(b)

x = (0, 1)
P = (-2, 351, -11664, 104976)
Q = (4, -2673, 204120, -4723920, 34012224)
W = (-16, -3888, 66339)
lo, mid, hi = F(1, 16), F(76, 1215), F(256, 3915)
assert lo < mid < hi < F(1, 11)
assert evalp(Q, lo) < 0 < evalp(Q, mid)
assert all(c > 0 for c in bernstein(tuple(i * Q[i] for i in range(1, 5)), lo, hi))

G = [(1,), (0, 18), (0, -9, 324)]
for _ in range(3, 18):
    G.append(add(sub(scale(18, sh(G[-1], 1)), scale(9, sh(G[-2], 1))),
                 scale(2, sh(G[-3], 1))))
assert G[6] == sh(Q, 2)
assert G[5] == scale(18, sh(P, 2))

# The new order-eight and order-seven recurrences, cross-multiplied.
for n in range(5):
    lhs8 = scale(18, mul(P, G[n+8]))
    rhs8 = add(add(mul(Q, G[n+7]), mul(sh(W, 2), G[n+1])),
               scale(-18, mul(sh((-76, 1215), 3), G[n])))
    assert lhs8 == rhs8, ('order8', n)
    lhs7 = scale(2, mul((-1, 81), G[n+7]))
    rhs7 = add(add(mul((-4, -117, 2916), G[n+6]),
                   mul((0, -76, 1215), G[n+4])),
               scale(16, sh(G[n], 2)))
    assert lhs7 == rhs7, ('order7', n)

# Strict Bernstein positivity on the broad rational bounding interval.
for n in (2, 3, 4, 5, 7):
    k = {2: 1, 3: 1, 4: 2, 5: 2, 7: 3}[n]
    assert all(c == 0 for c in G[n][:k])
    positive(G[n][k:], lo, hi, f'G{n} / x^{k}')
positive(P, lo, hi, 'P')
positive(W, lo, mid, 'W')
positive((-4, -117, 2916), mid, hi, 'a numerator')
assert lo > F(1, 81)
# Additional signs are immediate from x>0, Q>=0 for x>=root,
# (76-1215x)>=0 for x<=mid, and (1215x-76)>=0 for x>=mid.

# The source-range root-amplitude inequality also has an exact certificate.
D = (2, -9, 18)
E = (1, -3, 3)
Fpol = (4, -12, 21)
T = (-8, 12, 42, -135, 126)
assert sub(mul(D, Fpol), scale(32, E)) == scale(3, T)
r0 = F(8, 15)
assert evalp(T, r0) == F(344, 5625)
positive(tuple(i * T[i] for i in range(1, len(T))), r0, F(1), 'T prime')
assert r0 ** 3 / evalp(D, r0) == hi
assert 27**2 - 4*189 < 0  # d^2-27d+189 has no real zeros.
assert 9**2 - 4*16*2 < 0  # D(r)-2*r^2 is strictly positive.

# For the large-parameter root dominance, check exact algebra at r=1/2.
r = F(1, 2)
D = 18*r*r - 9*r + 2
assert D == 2 and D/r**3 == 16
assert (F(1, lo) - 11) / 6 == F(5, 6)

# This is only a decimal approximation; rational isolating signs and
# derivative positivity above certify existence and uniqueness.
a, b = lo, mid
for _ in range(90):
    c = (a+b)/2
    if evalp(Q, c) > 0:
        b = c
    else:
        a = c
rt = (a+b)/2
assert evalp(Q, a) < 0 < evalp(Q, b)
mu = (1/rt - 11)/6
print('PASS: exact polynomial recurrences, interval positivity, isolated root')
print('x_star ≈', f'{float(rt):.16f}')
print('mu_star ≈', f'{float(mu):.16f}')
print('Earlier sufficient bound mu<=', str((F(1, hi)-11)/6))
