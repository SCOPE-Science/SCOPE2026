"""Independent finite checks of simultaneous square-zero matrix rank triples.
No third-party dependencies.  Run: python verify_rank_triples.py
"""
from collections import Counter
from itertools import product
from math import prod


def rank_matrix(a, n, q):
    rows = [[a[i*n+j] % q for j in range(n)] for i in range(n)]
    rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank, n) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][j], -1, q)
        rows[rank] = [(z*inv)%q for z in rows[rank]]
        for i in range(n):
            if i != rank and rows[i][j]:
                c = rows[i][j]
                rows[i] = [(x-c*y)%q for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return rank


def matmul(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))


def binomq(n,k,q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return _bq(n,k,q)


def _bq(n,k,q):
    numerator=prod(q**(n-i)-1 for i in range(k))
    denominator=prod(q**(k-i)-1 for i in range(k))
    assert numerator%denominator==0
    return numerator//denominator


def surj(m,k,q):
    if m<k or k<0: return 0
    return prod(q**m-q**i for i in range(k))


def prediction(n,q):
    d={}
    for r in range(n+1):
        for s in range(n+1):
            for t in range(min(r,s)+1):
                ell=r+s-t
                m=n-ell
                if ell>n or m<max(r,s):
                    continue
                count=(binomq(n,ell,q)*binomq(ell,r,q)*binomq(r,t,q)
                       *q**((r-t)*(s-t))*surj(m,r,q)*surj(m,s,q))
                if count:
                    d[r,s,t]=count
    return d


def check(n,q):
    square=[]
    zero=(0,)*(n*n)
    for a in product(range(q),repeat=n*n):
        if matmul(a,a,n,q)==zero:
            r=rank_matrix(a,n,q)
            square.append((a,r))
    hist=Counter()
    for a,r in square:
        for b,s in square:
            if matmul(a,b,n,q)==zero and matmul(b,a,n,q)==zero:
                # dim(im A + im B) = rank of horizontal concatenation.
                # Compute rank of n-by-2n augmented matrix by row elimination.
                ab=[list(a[i*n:(i+1)*n]+b[i*n:(i+1)*n]) for i in range(n)]
                pos=0
                for j in range(2*n):
                    ii=next((i for i in range(pos,n) if ab[i][j]%q),None)
                    if ii is None: continue
                    ab[ii],ab[pos]=ab[pos],ab[ii]
                    inv=pow(ab[pos][j],-1,q)
                    ab[pos]=[(z*inv)%q for z in ab[pos]]
                    for i in range(pos+1,n):
                        if ab[i][j]:
                            c=ab[i][j]
                            ab[i]=[(x-c*y)%q for x,y in zip(ab[i],ab[pos])]
                    pos+=1
                    if pos==n: break
                t=r+s-pos
                hist[r,s,t]+=1
    expected=prediction(n,q)
    assert dict(hist)==expected, f'Failed n={n}, q={q}: {hist} != {expected}'
    # Check ranks are symmetric in the two letters and all possible strata appear.
    for (r,s,t),v in expected.items():
        assert expected[(s,r,t)]==v
    print(f'PASS n={n} q={q} squarezero={len(square)} pairs={sum(hist.values())} strata={len(hist)}')
    return hist

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)]:
        check(n,q)
    print('VERIFY_OK_TWO_LOOP_RADICAL_SQUARE_ZERO_RANK_TRIPLES')
