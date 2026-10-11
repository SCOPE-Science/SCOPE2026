from fractions import Fraction
from itertools import combinations
from math import comb

def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def padd(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

def pfromroots(roots):
    p = [Fraction(1)]
    for r in roots:
        p = pmul(p, [-r, Fraction(1)])
    return p

def peval(p, x):
    y = Fraction(0)
    for c in reversed(p):
        y = y * x + c
    return y

def divide_linear_exact(p, r):
    rev = list(reversed(p))
    qrev = [rev[0]]
    for c in rev[1:-1]:
        qrev.append(c + r * qrev[-1])
    remainder = rev[-1] + r * qrev[-1]
    assert remainder == 0
    return list(reversed(qrev))

def independent(S):
    return all((k + 1) not in S for k in S)

def target_spectrum(d, S):
    n = len(d)
    mu = []
    for i0 in range(n - 1):
        i = i0 + 1
        if i in S:
            mu.append(d[i0])
        elif i + 1 in S:
            mu.append(d[i0 + 1])
        else:
            mu.append((d[i0] + d[i0 + 1]) / 2)
    mu.append(d[-1] if n in S else d[-1] - Fraction(1, 2))
    return mu

def residues(d, mu):
    pD = pfromroots(d)
    pM = pfromroots(mu)
    xsq = []
    for i, di in enumerate(d):
        den = Fraction(1)
        for j, dj in enumerate(d):
            if i != j:
                den *= di - dj
        xsq.append(peval(pM, di) / den)
    return pD, pM, xsq

def reconstructed_charpoly(d, xsq):
    pD = pfromroots(d)
    p = pD[:]
    for di, w in zip(d, xsq):
        quotient = divide_linear_exact(pD, di)
        p = padd(p, [w * c for c in quotient])
    return p

for n in range(2, 11):
    d = [Fraction(3 * (n - i) + 1) for i in range(n)]
    vertices = list(range(2, n + 1))
    for r in range(len(vertices) + 1):
        for tup in combinations(vertices, r):
            S = set(tup)
            if not independent(S):
                continue
            mu = target_spectrum(d, S)
            assert all(d[i] >= mu[i] >= d[i + 1] for i in range(n - 1))
            assert mu[-1] <= d[-1]
            pD, pM, xsq = residues(d, mu)
            assert all(v >= 0 for v in xsq)
            for i, v in enumerate(xsq, start=1):
                assert (v == 0) == (i in S)
            assert reconstructed_charpoly(d, xsq) == pM

for n in range(2, 15):
    vertices = list(range(2, n + 1))
    for r in range(0, n // 2 + 1):
        count = sum(
            1 for tup in combinations(vertices, r)
            if independent(set(tup))
        )
        assert count == comb(n - r, r)

d = [Fraction(10), Fraction(6), Fraction(3), Fraction(1)]
xsq = [Fraction(36, 7), Fraction(0), Fraction(6, 7), Fraction(0)]
assert reconstructed_charpoly(d, xsq) == pfromroots(
    [Fraction(6), Fraction(6), Fraction(1), Fraction(1)]
)
assert xsq[0] / 4 - xsq[2] / 3 == 1
assert xsq[0] / 9 + xsq[2] / 2 == 1
assert sum(xsq) == 6

print("VERIFY_OK")
print("dimensions=2..10 all independent incidence patterns")
print("path_counts=2..14")
print("four_dimensional_spectrum=(6,6,1,1); jacobian=(3,3,-2,-2)")
