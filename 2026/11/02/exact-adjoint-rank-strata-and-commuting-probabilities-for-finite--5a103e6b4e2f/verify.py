"""Finite-field independent matrix-rank checks for truncated Witt Lie algebras.

Run: python3 verify.py
"""
import itertools
import random
from collections import Counter


def rank_mod_p(matrix, p):
    a = [list(map(lambda v: v % p, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    i = 0
    for j in range(cols):
        pivot = next((u for u in range(i, rows) if a[u][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        inv = pow(a[i][j], -1, p)
        a[i] = [(v * inv) % p for v in a[i]]
        for u in range(rows):
            if u != i and a[u][j]:
                factor = a[u][j]
                a[u] = [(v - factor*w) % p for v,w in zip(a[u],a[i])]
        i += 1
        if i == rows:
            break
    return i


def derivation_adjoint_rank(f,p):
    # basis x^j d/dx. [f d/dx, x^j d/dx] = (f*j*x^(j-1)-x^j f')d/dx
    matrix = [[0] * p for _ in range(p)]
    for i, coeff in enumerate(f):
        for j in range(p):
            k = i + j - 1
            if 0 <= k < p:
                matrix[k][j] = (matrix[k][j] + coeff*(j-i)) % p
    return rank_mod_p(matrix,p)


def expected_dim(f,p):
    if not any(f): return p
    v = next(i for i,x in enumerate(f) if x)
    if v == 0: return 1
    return v if 2*v < p else v-1


def check_exhaustive(p):
    seen=Counter()
    total_commuting=0
    for f in itertools.product(range(p),repeat=p):
        d=p-derivation_adjoint_rank(f,p)
        assert d == expected_dim(f,p),(p,f,d,expected_dim(f,p))
        v=next((i for i,x in enumerate(f) if x),p)
        seen[v,d]+=1
        total_commuting += p**d
    assert seen[p,p]==1
    expected=p**p
    for v in range(p):
        count=(p-1)*p**(p-v-1)
        d=(1 if v==0 else v if 2*v<p else v-1)
        assert seen[v,d]==count, (v,d,seen[v,d],count)
        expected+=count*p**d
    assert total_commuting==expected
    return len(seen),total_commuting


def check_samples(p,count):
    random.seed(20261029+p)
    for v in range(p):
        for _ in range(count):
            f=[0]*v + [random.randrange(1,p)] + [random.randrange(p) for _ in range(p-v-1)]
            got=p-derivation_adjoint_rank(f,p)
            assert got==expected_dim(f,p),(p,f,got)
    return p*count


if __name__=='__main__':
    n,co=check_exhaustive(5)
    x=sum(check_samples(p,31) for p in (7,11,13))
    print(f'VERIFY_OK p=5 all 3125 elements, {n} valuation strata, {co} commuting pairs, {x} additional sampled elements')
