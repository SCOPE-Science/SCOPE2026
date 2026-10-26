"""Independent finite-field checks for exterior-quadratic multiplication Jordan census.
Run: python3 verify_exterior_quadratic.py
Only standard-library arithmetic; characteristic-two fields F_2 and F_4.
"""
from collections import Counter
from itertools import product
from math import prod

def fmul(a,b,q):
    if q==2:
        return a & b
    assert q==4
    r=0
    for _ in range(2):
        if b&1:r ^= a
        b >>= 1
        a <<= 1
        if a&4:a ^= 7  # x^2 + x + 1
    return r

def inv(a,q):
    return next(x for x in range(1,q) if fmul(a,x,q)==1)

def rank(a,q):
    if not a:return 0
    a=[row[:] for row in a]; m=len(a); n=len(a[0]); r=0
    for j in range(n):
        z=next((i for i in range(r,m) if a[i][j]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r]
        c=inv(a[r][j],q)
        a[r]=[fmul(c,x,q) for x in a[r]]
        for i in range(r+1,m):
            c=a[i][j]
            if c:
                a[i]=[v^fmul(c,u,q) for v,u in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def actual_ranks(n,q,coeff):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    skew=[[0]*n for _ in range(n)]
    N=1<<n
    wedge=[[0]*N for _ in range(N)]
    for (i,j),v in zip(pairs,coeff):
        if not v:continue
        skew[i][j]=skew[j][i]=v
        ij=(1<<i)|(1<<j)
        for mask in range(N):
            if mask&ij==0:wedge[mask|ij][mask] ^= v
    return rank(skew,q)//2,rank(wedge,q)

def form_count(n,q,r):
    k=2*r
    if k>n:return 0
    gauss=1
    for i in range(k):
        gauss=gauss*(q**(n-i)-1)//(q**(i+1)-1) if False else gauss
    numerator=prod(q**(n-i)-1 for i in range(k))
    denominator=prod(q**(k-i)-1 for i in range(k))
    assert numerator%denominator==0
    gauss=numerator//denominator
    return gauss*q**(r*(r-1))*prod(q**(2*i-1)-1 for i in range(1,r+1))

def predicted_rank(n,r):
    return 0 if r==0 else 2**(n-1)-2**(n-r-1)

def check(n,q,all_forms):
    k=n*(n-1)//2
    if all_forms:
        forms=product(range(q),repeat=k)
    else:
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        forms=[]
        for r in range(n//2+1):
            form=[0]*k
            for j in range(r):form[pairs.index((2*j,2*j+1))]=1
            forms.append(tuple(form))
    cnt=Counter(); tested=0
    for f in forms:
        r,m=actual_ranks(n,q,f)
        want=predicted_rank(n,r)
        assert m==want,(n,q,f,r,m,want)
        cnt[r]+=1;tested+=1
    if all_forms:
        assert tested==q**k
        for r in range(n//2+1):
            assert cnt[r]==form_count(n,q,r),(n,q,r,cnt[r],form_count(n,q,r))
    return tested,cnt

if __name__=='__main__':
    all_tests=0
    for q,nmax in [(2,5),(4,4)]:
        for n in range(2,nmax+1):
            tested,distribution=check(n,q,True)
            all_tests+=tested
            print('EXHAUSTIVE',q,n,tested,sorted(distribution.items()))
    for n in [6,7]:
        tested,_=check(n,2,False)
        all_tests+=tested
        print('NORMAL_FORMS',2,n,tested)
    print('ALL_EXTERIOR_QUADRATIC_CHECKS_PASSED',all_tests)
