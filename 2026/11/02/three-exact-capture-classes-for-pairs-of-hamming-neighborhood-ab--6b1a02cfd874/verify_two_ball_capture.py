#!/usr/bin/env python3
"""Reproduce exact two-neighborhood hypercube capture-rank checks.

No third-party modules are required. All ranks are computed over prime fields;
the general theorem is established by the accompanying algebraic proof.
"""
from itertools import combinations
from math import comb

PRIMES=(1000003,1000033)

def modrank(matrix,prime):
    a=[[int(v)%prime for v in row] for row in matrix]
    if not a:return 0
    m,n=len(a),len(a[0]);piv=0
    for j in range(n):
        i=next((i for i in range(piv,m) if a[i][j]),None)
        if i is None:continue
        a[piv],a[i]=a[i],a[piv]
        row=a[piv]
        inv=pow(row[j],-1,prime)
        for u in range(piv+1,m):
            factor=a[u][j]*inv%prime
            if factor:
                for v in range(j,n):
                    a[u][v]=(a[u][v]-factor*row[v])%prime
        piv+=1
        if piv==m:break
    return piv

def neighborhood(d,x):
    return (x,)+tuple(x^(1<<b) for b in range(d))

def detectors(d,t):
    y=(1<<t)-1
    return tuple(dict.fromkeys(neighborhood(d,0)+neighborhood(d,y)))

def krawtchouk(d,k,w):
    return sum((-1)**j*comb(w,j)*comb(d-w,k-j)
               for j in range(max(0,k-d+w),min(w,k)+1))

def spectral_rank_gram(d,t,k,prime):
    targets=detectors(d,t)
    gram=[[krawtchouk(d,k,(x^y).bit_count()) for y in targets] for x in targets]
    return modrank(gram,prime)

def expected_rank(d,t,k):
    if k==0 or k==d:return 1
    if k==1 or k==d-1:return d
    s=min(t,d-t)
    if s==0:return d
    if s in (1,2):return 2*d-2
    if min(k,d-k)==2:return 2*d-1
    return 2*d

def expected_total(d,t):
    s=min(t,d-t)
    if s==0:return d*d-d+2
    if s<=2:return 2*d*d-6*d+8
    return 2*d*d-4*d

def direct_walsh_rank(d,t,k,prime):
    frequencies=[sum(1<<a for a in c) for c in combinations(range(d),k)]
    matrix=[[1 if ((x&s).bit_count()%2==0) else -1 for s in frequencies]
            for x in detectors(d,t)]
    return modrank(matrix,prime)

def direct_krylov_rank(d,t,prime):
    n=1<<d
    current=[]
    for x in detectors(d,t):
        v=[0]*n;v[x]=1;current.append(v)
    columns=[]
    for j in range(d+1):
        columns.extend(current)
        next_cols=[]
        for v in current:
            w=[0]*n
            for x,a in enumerate(v):
                if not a:continue
                for b in range(d):
                    z=x^(1<<b)
                    w[z]=(w[z]+a)%prime
            next_cols.append(w)
        current=next_cols
    return modrank([list(row) for row in zip(*columns)],prime)

def main():
    spectral=0
    for d in range(6,14):
        for t in range(1,d+1):
            expected=expected_total(d,t)
            for prime in PRIMES:
                ranks=[spectral_rank_gram(d,t,k,prime) for k in range(d+1)]
                required=[expected_rank(d,t,k) for k in range(d+1)]
                assert ranks==required,(d,t,prime,ranks,required)
                assert sum(ranks)==expected,(d,t,prime,sum(ranks),expected)
                spectral+=1
    print('Two-prime spectral Gram tables:',spectral,'PASS (6<=d<=13, every separation and energy)')
    walsh=0
    for d in range(6,10):
        for t in (1,2,3,d//2,d-2,d):
            for k in range(d+1):
                actual=direct_walsh_rank(d,t,k,PRIMES[0])
                expect=expected_rank(d,t,k)
                assert actual==expect,(d,t,k,actual,expect)
                walsh+=1
    print('Direct independent Fourier evaluations:',walsh,'PASS')
    krylov=0
    for d in (6,7):
        for t in range(1,d+1):
            actual=direct_krylov_rank(d,t,PRIMES[1])
            expected=expected_total(d,t)
            assert actual==expected,(d,t,actual,expected)
            krylov+=1
    print('Direct adjacency-power Krylov ranks:',krylov,'PASS')
    print('Representative classes:')
    for d in (6,7,8,10):
        print('d=',d, 'near=',expected_total(d,1),
              'middle=',expected_total(d,3),
              'antipodal=',expected_total(d,d),
              'number_sites=',1<<d)

if __name__=='__main__':
    main()
