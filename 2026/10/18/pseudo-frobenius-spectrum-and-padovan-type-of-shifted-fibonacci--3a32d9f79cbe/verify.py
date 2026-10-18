#!/usr/bin/env python3
"""Independent exact-arithmetic checks for shifted-Fibonacci semigroup type."""
import heapq

def fibonacci(limit):
    f=[0,1]
    for _ in range(2,limit+1): f.append(f[-1]+f[-2])
    return f

def minimal_fibonacci_count(x,f):
    count=0
    for i in range(len(f)-1,1,-1):
        if f[i]<=x:
            x-=f[i];count+=1
    assert x==0
    return count

def expected_indices(a):
    out=[]
    for mask in range(1<<(a-2)):
        inds=[i for i in range(2,a) if mask>>(i-2)&1]
        if any(y-x==1 for x,y in zip(inds,inds[1:])):continue
        if all(j in inds or j-1 in inds or j+1 in inds for j in range(2,a)) and (2 in inds or inds==list(range(3,a,2)) and (a-1)%2==1):
            out.append(tuple(inds))
    return out

def actual_apery(a,f):
    m=f[a]
    coins=[m+f[i] for i in range(2,a)]
    dist=[10**50]*m;dist[0]=0
    pq=[(0,0)]
    while pq:
        d,r=heapq.heappop(pq)
        if dist[r]!=d:continue
        for g in coins:
            rr=(r+g)%m;nd=d+g
            if nd<dist[rr]:dist[rr]=nd;heapq.heappush(pq,(nd,rr))
    return dist,coins

def check(max_a=19):
    f=fibonacci(max_a)
    P={1:1,2:1,3:1}
    for n in range(4,max_a):P[n]=P[n-2]+P[n-3]
    for a in range(3,max_a+1):
        m=f[a]
        ap,coins=actual_apery(a,f)
        beta=[minimal_fibonacci_count(x,f) for x in range(m)]
        assert all(ap[x]==beta[x]*m+x for x in range(m))
        real=[]
        for x in range(1,m):
            if not any(ap[x]+g==ap[(x+g)%m] for g in coins):
                real.append(ap[x]-m)
        predicted=[]
        for I in expected_indices(a):
            x=sum(f[i] for i in I)
            predicted.append((len(I)-1)*m+x)
        assert sorted(real)==sorted(predicted),(a,real,predicted)
        assert len(real)==P[a-2]+(a%2==0),(a,len(real),P[a-2])
        print('a=%d multiplicity=%d type=%d PASS'%(a,m,len(real)))
    print('VERIFY_OK all a=3..%d, independent Dijkstra Apéry and maximal-element tests'%max_a)

if __name__=='__main__':check()
