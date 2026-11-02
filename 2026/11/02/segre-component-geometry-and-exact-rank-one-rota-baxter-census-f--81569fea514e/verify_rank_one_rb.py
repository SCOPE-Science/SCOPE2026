"""Exhaustive finite-field tests of a rank-one Rota--Baxter classification.
Uses polynomial quotient arithmetic and the defining identity, not the theorem's factor criterion.
Usage: python verify_rank_one_rb.py
"""
from itertools import product


def field(q):
    if q in (2, 3):
        return [[(a * b) % q for b in range(q)] for a in range(q)], lambda a, b: (a + b) % q
    if q == 4:
        def m(a, b):
            v = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        v ^= 1 << (i+j)
            if v & 4:
                v ^= 7  # z^2+z+1=0
            return v
        return [[m(a, b) for b in range(q)] for a in range(q)], lambda a,b:a^b
    raise ValueError('unsupported field')


def check(q, n):
    mul, add = field(q)
    vectors = list(product(range(q), repeat=n))
    z = (0,)*n
    nonzero = [v for v in vectors if v != z]
    mats = set()
    seen_good = set()
    for u in nonzero:
        square = [0]*n
        for i,a in enumerate(u):
            if a:
                for j,b in enumerate(u[:n-i]):
                    square[i+j] = add(square[i+j],mul[a][b])
        r = next(i for i,a in enumerate(u) if a)
        for phi in nonzero:
            mat = tuple(mul[u[i]][phi[j]] for i in range(n) for j in range(n))
            if mat in mats:
                continue
            mats.add(mat)
            functional_products = [0]*n
            for j in range(n):
                v=0
                for i in range(n-j):
                    v=add(v,mul[u[i]][phi[i+j]])
                functional_products[j]=v
            ok=True
            for i in range(n):
                for j in range(n):
                    c=add(mul[phi[i]][functional_products[j]],mul[phi[j]][functional_products[i]])
                    for a in range(n):
                        if mul[phi[i]][mul[phi[j]][square[a]]] != mul[c][u[a]]:
                            ok=False
                            break
                    if not ok:break
                if not ok:break
            if ok:
                if r < (n+1)//2 or any(functional_products):
                    raise AssertionError(('criterion mismatch',q,n,u,phi))
                seen_good.add(mat)
            elif r >= (n+1)//2 and not any(functional_products):
                raise AssertionError(('sufficiency mismatch',q,n,u,phi))
    k=n//2
    predicted=k*q**(n-1)-sum(q**i for i in range(k))
    assert len(seen_good)==predicted,(q,n,len(seen_good),predicted)
    print(f'PASS q={q} n={n} rank_one_tested={len(mats)} solutions={len(seen_good)}')
    return len(mats)

if __name__ == '__main__':
    tests=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3)]
    total=sum(check(*case) for case in tests)
    print('RANK_ONE_RB_SEGRE_STRATA_OK',len(tests),total)
