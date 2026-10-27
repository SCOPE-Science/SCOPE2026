"""Exhaustive finite-field checks for the parabolic regularity distribution.
No nonstandard dependencies. Usage: python checks/check_parabolic_regular.py
"""
from collections import Counter
from itertools import product
from math import prod


def rank(M, q):
    if not M:
        return 0
    A = [list(r) for r in M]
    h, w, piv = len(A), len(A[0]), 0
    for c in range(w):
        z = next((t for t in range(piv, h) if A[t][c] % q), None)
        if z is None:
            continue
        A[z], A[piv] = A[piv], A[z]
        inv = pow(A[piv][c], -1, q)
        A[piv] = [(v * inv) % q for v in A[piv]]
        for t in range(h):
            if t != piv and A[t][c] % q:
                k = A[t][c]
                A[t] = [(u - k * v) % q for u, v in zip(A[t], A[piv])]
        piv += 1
        if piv == h:
            break
    return piv


def blocks(q, a, b):
    for entries in product(range(q), repeat=a*a+a*b+b*b):
        A = [entries[i*a:(i+1)*a] for i in range(a)]
        B = [entries[a*a+i*b:a*a+(i+1)*b] for i in range(a)]
        D = [entries[a*a+a*b+i*b:a*a+a*b+(i+1)*b] for i in range(b)]
        T = [tuple(A[i])+tuple(B[i]) for i in range(a)]
        T.extend(tuple([0]*a)+tuple(D[i]) for i in range(b))
        yield A, D, tuple(T)


def numrank(q, n, r):
    assert 0 <= r <= n
    return prod((q**n-q**t)**2 for t in range(r)) // prod(q**r-q**t for t in range(r))


def mul(A, B, q):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)) for i in range(n))


def verify(q, a, b, witness):
    mats = list(blocks(q,a,b))
    all_ts = [row[2] for row in mats] if witness else None
    got=Counter()
    witnessed=0
    for A,D,T in mats:
        i=a-rank(A,q)
        j=b-rank(D,q)
        cond=(rank(T,q)==(a-i)+(b-j))
        if cond:
            got[(i,j)]+=1
        if witness:
            isreg=any(mul(mul(T,S,q),T,q)==T for S in all_ts)
            if isreg!=cond:
                raise AssertionError((q,a,b,'criterion',T))
            witnessed+=1
    expected={}
    for i in range(a+1):
        for j in range(b+1):
            countA=numrank(q,a,a-i)
            countD=numrank(q,b,b-j)
            countB=q**(a*b-i*j)
            expected[(i,j)]=countA*countD*countB
    if dict(got)!={k:v for k,v in expected.items() if v}:
        raise AssertionError((q,a,b,'distribution',got,expected))
    print('case q=%d a=%d b=%d total=%d regular=%d inverse_witnesses=%d strata=%d' %
          (q,a,b,len(mats),sum(got.values()),witnessed,len(got)))
    return len(mats),sum(got.values()),witnessed


def main():
    # Prime-field cases; formulas themselves cover every finite field F_q.
    cases=[(2,1,1,True),(2,1,2,True),(3,1,1,True),
           (2,2,2,False),(3,1,2,False),(2,2,1,False)]
    totals=[verify(*c) for c in cases]
    print('ALL_PARABOLIC_REGULARITY_CHECKS_PASSED cases=%d matrices=%d regular=%d witnessed=%d'%
          (len(totals),sum(x[0] for x in totals),sum(x[1] for x in totals),sum(x[2] for x in totals)))


if __name__=='__main__':
    main()
