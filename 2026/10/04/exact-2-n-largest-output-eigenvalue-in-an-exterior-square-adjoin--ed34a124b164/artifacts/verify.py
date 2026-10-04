#!/usr/bin/env python3
from fractions import Fraction as F


def sharp_family(n):
    x = [F(n-2, n), F(n-2, n)] + [F(-2, n)] * (n-2)
    assert sum(x) == 0
    hx = sum(t*t for t in x)
    pair_sq = [(x[i] + x[j])**2 for i in range(n) for j in range(i+1, n)]
    hl = sum(pair_sq)
    assert hl == F(n-2) * hx
    op2 = max(pair_sq)
    assert op2 / hl == F(2, n)
    coherent = F(1, n-2)
    gap = F(2, n) - coherent
    assert gap == F(n-4, n*(n-2)) and gap > 0

    # Slater transition matrix Gamma=P with rank(P)=2.
    gamma0_sq = F(2) - F(4, n)
    assert gamma0_sq / F(n-2) == F(2, n)

    # L(E_{1n}) is a partial permutation with n-2 unit entries.
    nonzero_entries = n - 2
    assert F(1, nonzero_entries) == coherent


def sos_identity(alpha, u):
    assert sum(a*a for a in alpha) == 1
    left = sum(a*v for a, v in zip(alpha, u))**2
    left += sum((1 - 2*a*a) * v*v for a, v in zip(alpha, u))
    right = F(0)
    for r in range(len(alpha)):
        for s in range(r+1, len(alpha)):
            right += (alpha[s]*u[r] + alpha[r]*u[s])**2
    assert left == right
    assert right >= 0


for n in range(5, 13):
    sharp_family(n)

sos_identity([F(3,5), F(4,5)], [F(7,11), F(-2,13)])
sos_identity([F(1,3), F(2,3), F(2,3)], [F(5,17), F(-3,19), F(7,23)])
print("VERIFY_OK")
