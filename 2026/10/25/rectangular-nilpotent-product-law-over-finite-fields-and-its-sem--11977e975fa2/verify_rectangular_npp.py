#!/usr/bin/env python3
"""Independent finite enumeration for a rectangular nilpotent-product formula.

This file intentionally checks matrix products and nilpotence directly, rather
than using the theorem's counting argument.
"""
import itertools
from collections import Counter


def matrices(q, m, n):
    return list(itertools.product(range(q), repeat=m*n))


def mul(a, b, q, m, n, p):
    return tuple(sum(a[i*n+k]*b[k*p+j] for k in range(n)) % q
                 for i in range(m) for j in range(p))


def nilpotent(a, q, m):
    power = a
    for k in range(1, m+1):
        if not any(power):
            return True
        if k < m:
            power = mul(power, a, q, m, m, m)
    return False


def rank(a, q, m, n):
    rows = [[a[i*n+j] for j in range(n)] for i in range(m)]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c], -1, q)  # q in this checker is prime
        rows[r] = [(z*inv) % q for z in rows[r]]
        for i in range(r+1, m):
            fac = rows[i][c]
            if fac:
                rows[i] = [(u-fac*v) % q for u,v in zip(rows[i],rows[r])]
        r += 1
        if r == m:
            break
    return r


def main():
    cases = [(q,m,n) for q in (2,3,5) for m in (1,2) for n in (1,2)]
    cases += [(2,2,3), (2,3,2), (2,3,3)]
    for q,m,n in cases:
        AA,BB=matrices(q,m,n),matrices(q,n,m)
        nilset={x for x in matrices(q,m,m) if nilpotent(x,q,m)}
        assert len(nilset)==q**(m*m-m)
        total=0
        conditional=Counter()
        for a in AA:
            count=sum(mul(a,b,q,m,n,m) in nilset for b in BB)
            r=rank(a,q,m,n)
            assert count==q**(m*n-r),(q,m,n,a,r,count)
            conditional[r]+=1
            total+=count
        expectation=q**(2*m*n-m)+q**(2*m*n-n)-q**(2*m*n-m-n)
        assert total==expectation,(q,m,n,total,expectation)
        print(f'q={q} m={m} n={n} pair_count={len(AA)*len(BB)} nilpotent_pairs={total} rank_profile={sorted(conditional.items())}: OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
