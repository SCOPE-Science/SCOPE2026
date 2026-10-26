#!/usr/bin/env python3
"""Exact finite checks for primitive-root arithmetic progressions in safe-prime fields.

All arithmetic is integral. The finite cutoff in the proof is p<113.
Larger tests are corroborative only.
"""
from collections import Counter
from math import isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n)+1):
        if n % d == 0:
            return False
    return True


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    assert v in (1, p-1)
    return 1 if v == 1 else -1


def primitive(a, p):
    a %= p
    if not a:
        return False
    # For a safe prime p=2q+1, order 2q exactly means neither
    # a^q=1 nor a^2=1. This is independent of chi-based enumeration.
    return pow(a, (p-1)//2, p) != 1 and pow(a, 2, p) != 1


def check_one(p):
    assert prime(p) and prime((p-1)//2)
    prim = {x for x in range(p) if primitive(x, p)}
    assert len(prim) == ((p-1)//2 - 1) if p >= 7 else True
    if p < 11:
        assert all(sum(all((x+i*d) % p in prim for i in range(4))
                       for x in range(p)) == 0 for d in range(1,p))
        return (p, 0, 0, 0, p-1)
    s4 = sum(chi(x*(x+1)*(x+2)*(x+3), p) for x in range(p))
    numer = p - 10 - 4*chi(2,p) + s4
    assert numer % 16 == 0
    b = numer // 16
    qdirect = sum(all(chi(x+i,p) == -1 for i in range(4)) for x in range(p))
    assert b == qdirect
    counts = []
    for d in range(1,p):
        brute = sum(all((x+i*d) % p in prim for i in range(4))
                    for x in range(p))
        e = sum(all(chi(-1+(i-j)*d,p) == -1 for i in range(4) if i != j)
                for j in range(4))
        assert brute == b - e, (p,d,brute,b,e)
        counts.append(brute)
    return p, b, min(counts), max(counts), counts.count(0)


def main():
    safe = [p for p in range(5,1001,2) if prime(p) and prime((p-1)//2)]
    assert [p for p in safe if p<113] == [5,7,11,23,47,59,83,107]
    rows = [check_one(p) for p in safe]
    required = {5:(0,0),7:(0,0),11:(0,0),23:(0,1),
                47:(1,2),59:(1,3),83:(1,5),107:(4,7)}
    for p,b,mx,M,zero in rows:
        if p in required:
            assert (mx,M) == required[p], (p,b,mx,M,zero)
        if p >= 47:
            assert mx > 0 and zero == 0, (p,mx)
    assert len(rows) > 15
    print('PROOF_FINITE_CHECK', [r for r in rows if r[0] < 113])
    print('CORROBORATION safe_primes<=1000:',len(rows),
          'largest:',rows[-1][0])
    print('VERIFY_OK: all safe primes below 113 exhaustive; exact identity and independent primitive-test through 1000')

if __name__ == '__main__':
    main()
