#!/usr/bin/env python3
"""Self-contained finite checks for the hollow symmetric determinant family.

No finite test substitutes for the all-n characteristic-zero argument.
"""
from itertools import permutations, product
from collections import defaultdict, Counter


def polynomial_data(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    ids = {p:k for k,p in enumerate(pairs)}
    coeffs = defaultdict(int)
    for p in permutations(range(n)):
        if any(p[i] == i for i in range(n)):
            continue
        sign = (-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        e = [0]*len(pairs)
        for i,j in enumerate(p):
            e[ids[min(i,j),max(i,j)]] += 1
        coeffs[tuple(e)] += sign
    det = [(c,e) for e,c in coeffs.items() if c]
    grad = []
    for j in range(len(pairs)):
        grad.append([(c*e[j],tuple(a-(k==j) for k,a in enumerate(e)))
                     for c,e in det if e[j]])
    return pairs,det,grad


def eval_poly(terms, vals, p):
    ans=0
    for c,e in terms:
        v=c
        for x,power in zip(vals,e):
            if power: v *= x**power
        ans += v
    return ans % p


def rank_mod(A,p):
    a=[row[:] for row in A]
    n=len(a); h=0
    for j in range(n):
        t=next((i for i in range(h,n) if a[i][j]%p),None)
        if t is None: continue
        a[h],a[t]=a[t],a[h]
        inv=pow(a[h][j]%p,-1,p)
        for k in range(j,n): a[h][k]=a[h][k]*inv%p
        for i in range(h+1,n):
            c=a[i][j]
            if c:
                for k in range(j,n): a[i][k]=(a[i][k]-c*a[h][k])%p
        h+=1
        if h==n: break
    return h


def enumerate_n5():
    n=5; p=3
    pairs,det,grad=polynomial_data(n)
    assert len(pairs)==10 and len(det)>0
    summary=Counter()
    for vals in product(range(p),repeat=len(pairs)):
        if eval_poly(det,vals,p):
            summary['det_nonzero'] += 1
            continue
        a=[[0]*n for i in range(n)]
        for (i,j),v in zip(pairs,vals):a[i][j]=a[j][i]=v
        rank=rank_mod(a,p)
        singular=all(eval_poly(g,vals,p)==0 for g in grad)
        zero_star=any(all(a[i][j]==0 for j in range(n)) for i in range(n))
        expected=rank<=n-2 or zero_star
        if singular!=expected:
            raise AssertionError(('Jacobian/rank-star discrepancy',vals,rank))
        summary['rank_'+str(rank)]+=1
        summary['singular' if singular else 'smooth'] += 1
        if singular and rank==n-1:
            assert zero_star
            summary['rank_n_minus_1_star'] += 1
    assert sum(v for k,v in summary.items() if k.startswith('rank_') and k!='rank_n_minus_1_star')+summary['det_nonzero']==3**10
    return dict(sorted(summary.items()))


def witness(n):
    # Rank n-2, kernel spanned by e1-e2 and e3-e4.
    assert n>=5
    a=[[0]*n for _ in range(n)]
    for i in (0,1):
        for j in (2,3):a[i][j]=a[j][i]=1
    if n==5:
        for i in range(4):a[i][4]=a[4][i]=1
    else:
        for i in range(4,n):
            for j in range(i+1,n):a[i][j]=a[j][i]=1
    return a


def witness_checks():
    for n in range(5,13):
        a=witness(n)
        assert rank_mod(a,1000003)==n-2
        u=[1,-1,0,0]+[0]*(n-4)
        v=[0,0,1,-1]+[0]*(n-4)
        assert all(sum(a[i][j]*u[j] for j in range(n))==0 for i in range(n))
        assert all(sum(a[i][j]*v[j] for j in range(n))==0 for i in range(n))
        # In directions E12+E21, E34+E43, E13+E31, the
        # restricted 2x2 symmetric bilinear forms are linearly independent.
        forms=[]
        for i,j in ((0,1),(2,3),(0,2)):
            uu=2*u[i]*u[j]
            uv=u[i]*v[j]+u[j]*v[i]
            vv=2*v[i]*v[j]
            forms.append((uu,uv,vv))
        assert forms==[(-2,0,0),(0,0,-2),(0,1,0)]
    return 'explicit transverse 3-dimensional slices verified for n=5..12'


if __name__=='__main__':
    print('characteristic-three exhaustive n=5:',enumerate_n5())
    print(witness_checks())
    print('VERIFY_OK')
