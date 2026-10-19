"""Exact finite-field idempotent commutator counts: reproducibility checker."""
from itertools import product
from collections import Counter
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def count_idempotents(n, k, q):
    return gaussian(n,k,q) * q**(k*(n-k))


def fiber_total(n, s, q, a):
    if s == 0: return int(a == 0)
    if s == n: return int(a == 1)
    top = (q**s-1)*(q**(n-s)-1)*q**(n-2)
    top += q**(n-1)*((q**s-1)*int(a == 1)+(q**(n-s)-1)*int(a == 0))
    den = (q**n-1)*q**(n-1)
    num = count_idempotents(n,s,q)*top
    assert num % den == 0
    return num // den


def expected(n,s,q):
    hist=Counter()
    for a in range(q):
        total=fiber_total(n,s,q,a)
        if s in (0,n):
            if total: hist[a,0]=total
        elif a not in (0,1):
            hist[a,2]=total
        else:
            j=count_idempotents(n-1,s,q) if a==0 else count_idempotents(n-1,s-1,q)
            w=q**s if a==0 else q**(n-s)
            hist[a,0]=j
            hist[a,1]=2*(w-1)*j
            hist[a,2]=total-(2*w-1)*j
            assert hist[a,2]>=0
    assert sum(hist.values())==count_idempotents(n,s,q)
    return hist


def matrix_rank(M,prime):
    a=[list(row) for row in M]
    n=len(a);rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if a[i][col]%prime),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col]%prime,-1,prime)
        for j in range(col,n): a[rank][j]=a[rank][j]*inv%prime
        for i in range(rank+1,n):
            x=a[i][col]
            for j in range(col,n): a[i][j]=(a[i][j]-x*a[rank][j])%prime
        rank+=1
    return rank


def exhaustive(n,prime):
    tally=Counter()
    for entries in product(range(prime),repeat=n*n):
        M=[entries[n*i:n*(i+1)] for i in range(n)]
        if any(sum(M[i][k]*M[k][j] for k in range(n))%prime!=M[i][j] for i in range(n) for j in range(n)):
            continue
        s=matrix_rank(M,prime)
        a=M[0][0]
        c=int(any(M[0][j] for j in range(1,n)))+int(any(M[i][0] for i in range(1,n)))
        tally[s,a,c]+=1
    for s in range(n+1):
        expected_cells=expected(n,s,prime)
        observed_cells=Counter({(a,c):count for (ss,a,c),count in tally.items() if ss==s})
        assert observed_cells==Counter({k:v for k,v in expected_cells.items() if v}), (n,prime,s,observed_cells,expected_cells)
    print('PASS exhaustive',n,prime)


if __name__=='__main__':
    for n,p in [(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)]:
        exhaustive(n,p)
    for q in [2,3,4,5,7,8,9]:
        for n in range(2,9):
            for s in range(1,n):
                expected(n,s,q)
    print('PASS exact arithmetic q=2,3,4,5,7,8,9 and 2<=n<=8')
