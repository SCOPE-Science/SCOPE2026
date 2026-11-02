"""Finite rank checks for anticanonical restrictions to coordinate subspaces.
This verifies sample parameters only. A separate inequality proof handles all n.
"""
from itertools import product
from math import comb
from fractions import Fraction


def lattice_points(k, m, n):
    degree = n + 1
    caps = [2] * m + [degree] * (k + 1 - m)
    def recur(j, rem, acc):
        if j == k:
            if rem <= caps[j]:
                yield tuple(acc + [rem])
            return
        for v in range(min(caps[j], rem) + 1):
            yield from recur(j + 1, rem - v, acc + [v])
    yield from recur(0, degree, [])


def rank_rational(vectors):
    basis = {}
    for row0 in vectors:
        row = [Fraction(x) for x in row0]
        for pos, b in sorted(basis.items()):
            factor = row[pos]
            if factor:
                row = [v - factor * z for v,z in zip(row,b)]
        nz = next((i for i,x in enumerate(row) if x!=0), None)
        if nz is not None:
            pivot = row[nz]
            basis[nz] = [x / pivot for x in row]
    return len(basis)


def polytope_dim(k, m, n):
    first = None
    basis = {}
    count = 0
    for p in lattice_points(k,m,n):
        count += 1
        if first is None:
            first = p
            continue
        v = [Fraction(p[i]-first[i]) for i in range(k)]
        for pos in sorted(basis):
            factor = v[pos]
            if factor:
                v = [q-factor*b for q,b in zip(v,basis[pos])]
        nz = next((i for i,x in enumerate(v) if x!=0), None)
        if nz is not None:
            pivot=v[nz]; basis[nz]=[x/pivot for x in v]
            if len(basis)==k:
                return k
    return len(basis) if first is not None else -1


def expected(n,t):
    return (n in (2,4)) or (n==3 and t<=1) or (n>=5 and t<=2)


def test():
    cases=0
    for n in range(2,9):
        for t in range(n+2):
            ok=True
            for k in range(1,n+1):
                for m in range(max(0,t-(n-k)),min(t,k+1)+1):
                    if k==1:
                        good = (n+1-m*(n-1)) != 0
                    else:
                        dim=polytope_dim(k,m,n)
                        # In all non-exceptional cases, the actual lattice polytope
                        # is full-dimensional iff the restricted bundle is big.
                        theoretical=(m<k+1 or n+1<2*(k+1))
                        assert (dim==k)==theoretical,(n,t,k,m,dim,theoretical)
                        good=(dim==k)
                    ok &= good
                    cases+=1
            assert ok == expected(n,t),(n,t,ok,expected(n,t))
    print(f'VERIFY_OK: {cases} orbit-subspace tests; all n=2..8, all t')

if __name__=='__main__': test()
