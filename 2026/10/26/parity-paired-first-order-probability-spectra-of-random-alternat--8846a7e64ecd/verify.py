"""Finite rank-count checks for alternating bilinear forms over prime fields.
Run with Python 3: python verify.py.
Finite checks illustrate the combinatorial component; they are not an
infinite-dimensional proof or a substitute for the first-order argument.
"""
from collections import Counter
from itertools import product
from math import prod


def matrix_rank(a, q):
    a = [row[:] for row in a]
    n = len(a)
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r,n) if a[i][j] % q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, q)
        a[r] = [(x*inv)%q for x in a[r]]
        for i in range(r+1, n):
            if a[i][j]:
                c = a[i][j]
                a[i] = [(a[i][k]-c*a[r][k])%q for k in range(n)]
        r += 1
    return r


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    a = prod(q**(n-i)-1 for i in range(k))
    b = prod(q**(k-i)-1 for i in range(k))
    return a//b


def nondegenerate_alternating_forms(half_rank, q):
    h = half_rank
    gl = prod(q**(2*h)-q**i for i in range(2*h))
    sp = q**(h*h)*prod(q**(2*i)-1 for i in range(1,h+1))
    assert gl % sp == 0
    return gl//sp


def theoretical_counts(n,q):
    return {m:gaussian(n,n-m,q)*nondegenerate_alternating_forms((n-m)//2,q)
            for m in range(n+1) if (n-m)%2 == 0}


def direct_counts(n,q):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    counts=Counter()
    for z in product(range(q), repeat=len(pairs)):
        a = [[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,z):
            a[i][j]=v
            a[j][i]=(-v)%q
        counts[n-matrix_rank(a,q)]+=1
    return dict(counts)


def expected_kernel_size(n,q):
    # E(q^nullity)=1+(q^n-1)q^{-(n-1)}.
    # Verify the integer-scaled identity from exact rank counts.
    c=theoretical_counts(n,q)
    return sum(q**m*v for m,v in c.items()), q**(n*(n-1)//2)+(q**n-1)*q**((n-1)*(n-2)//2)


def main():
    checked=0
    for q,max_n in [(2,6),(3,5)]:
        for n in range(1,max_n+1):
            got=direct_counts(n,q)
            want=theoretical_counts(n,q)
            assert got==want, (q,n,got,want)
            assert sum(want.values())==q**(n*(n-1)//2)
            lhs,rhs=expected_kernel_size(n,q)
            assert lhs==rhs,(q,n,lhs,rhs)
            checked+=len(want)
    print('ALTERNATING_FORMS_FINITE_COUNT_OK',checked,'rank-cells')

if __name__=='__main__':
    main()
