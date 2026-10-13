"""Exact finite corroboration of a Grassmannian critical-value discriminant identity.

Run: python3 verify.py. This checks examples, not the general proof.
"""
from itertools import combinations
from math import comb


def check(n, k, lam):
    assert n == len(lam)
    inds = range(n)
    subsets = tuple(combinations(inds, k))
    vals = [k + sum(x*x for x in lam) - 2*sum(lam[i] for i in I)
            for I in subsets]
    lhs = 1
    for i, j in combinations(range(len(vals)), 2):
        lhs *= (vals[i] - vals[j])**2

    delta = 1
    for i, j in combinations(inds, 2):
        delta *= (lam[i]-lam[j])**2
    rhs = (4**comb(len(subsets), 2)) * (delta**comb(n-2, k-1))

    factors = []
    for r in range(2, min(k, n-k)+1):
        sets = tuple(combinations(inds, r))
        tr = 1
        count = 0
        for ii, A in enumerate(sets):
            Aset = set(A)
            for B in sets[ii+1:]:
                if Aset.isdisjoint(B):
                    tr *= sum(lam[a] for a in A)-sum(lam[b] for b in B)
                    count += 1
        assert count == comb(n, r)*comb(n-r, r)//2
        rhs *= tr**(2*comb(n-2*r, k-r))
        factors.append((r,tr))
    assert lhs == rhs, (n,k,lam,lhs,rhs)
    return factors


for n in range(4, 8):
    for k in range(1, n):
        for lam in [tuple(1<<j for j in range(n)),tuple(range(n))]:
            check(n,k,lam)

# The primitive degree-3 resonance factor of the six-value case.
a,b,c,d = 0,1,2,4
E1 = a+b+c+d
E2 = a*b+a*c+a*d+b*c+b*d+c*d
E3 = a*b*c+a*b*d+a*c*d+b*c*d
T = (a+b-c-d)*(a+c-b-d)*(a+d-b-c)
assert T == E1**3-4*E1*E2+8*E3
assert T == 15

# Distinct eigenvalues but coincident critical squared distances.
lam = (0,1,2,3)
assert len(set(lam)) == 4
assert sorted(2+sum(v*v for v in lam)-2*sum(lam[i] for i in ij)
              for ij in combinations(range(4),2)) == [6,8,10,10,12,14]
assert check(4,2,lam)[0][1] == 0
print('VERIFY_OK: exact finite tests n=4..7, all k, resonance and nonresonance; cubic identity.')
