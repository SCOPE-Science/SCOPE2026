#!/usr/bin/env python3
"""Independent finite checks of the stated ladder optimum formula."""
from itertools import combinations

def prediction(n):
    m=(n+4)//5; e=5*m-n
    a=[1]
    for lim in (2, 2)+tuple(4 for _ in range(m-1)):
        b=[0]*(len(a)+lim)
        for j,x in enumerate(a):
            for d in range(lim+1): b[j+d]+=x
        a=b
    return 2*m,a[e]**2,a[e]

def path_centers(n):
    m=(n+4)//5
    count=0
    for cc in combinations(range(1,n+1),m):
        if all(any(abs(c-i)<=2 for c in cc) for i in range(1,n+1)):
            count+=1
    return count

def brute_ladder(n):
    vertices=[(i,r) for i in range(n) for r in range(2)]
    N=len(vertices)
    nb=[sum(1<<j for j,w in enumerate(vertices) if abs(v[0]-w[0])+abs(v[1]-w[1])==2) for v in vertices]
    for k in range(1,N+1):
        count=0
        for combo in combinations(range(N),k):
            mask=sum(1<<i for i in combo)
            if all((mask>>i)&1 or (mask&nb[i]) for i in range(N)):
                count+=1
        if count:return k,count
    raise AssertionError('Empty graph?')

for n in range(1,21):
    V=[(i,r) for i in range(n) for r in range(2)]
    for u in V:
        for v in V:
            at2=(abs(u[0]-v[0])+abs(u[1]-v[1])==2)
            samecomp=(u[0]+u[1])%2==(v[0]+v[1])%2
            predicted=samecomp and (1<=abs(u[0]-v[0])<=2)
            assert at2==predicted,(n,u,v)
for n in range(1,19):
    _,val,side=prediction(n)
    assert path_centers(n)==side,(n,side,path_centers(n))
for n in range(1,10):
    a=prediction(n)[:2]
    b=brute_ladder(n)
    assert a==b,(n,a,b)
    print(f'n={n} minimum_size={a[0]} minimum_sets={a[1]}')
for m in range(1,31):
    for e in range(5):
        n=5*m-e
        if n>0:
            _,cnt,_=prediction(n)
            if e==0:assert cnt==1
            if e==1:assert cnt==(m+1)**2
print('VERIFY_OK: metric decomposition n<=20; path-center counts n<=18; exhaustive ladders n<=9; periodic identities m<=30')
