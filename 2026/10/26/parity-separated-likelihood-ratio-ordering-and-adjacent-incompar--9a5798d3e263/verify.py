from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

def odf(m):
    assert m>=-1 and m%2==1
    z=1
    while m>0:z*=m; m-=2
    return z

def dist(n,k):
    assert n>=2 and 0<=k<=n-1
    N=2*n-2
    d={}
    for h in range(k+1):
        if (k-h)&1:continue
        a=(k-h)//2; b=(N-k-h)//2
        if b<0:continue
        count=factorial(k)*factorial(N-k)//(factorial(h)*2**(a+b)*factorial(a)*factorial(b))
        d[h]=Fraction(count,odf(N-1))
    assert sum(d.values())==1
    return d

def outranks(p,q):
    return all(sum(z for j,z in q.items() if j>=h)>=sum(z for j,z in p.items() if j>=h) for h in range(max(max(p),max(q))+1))

def build_counts(N):
    # Matchings of 2n points; distinguish partner of 0 then count crossings of the resulting chord.
    raw={}
    a=list(range(N))
    pairs=[]
    def rec(rest):
        if not rest:
            x=next(q for p,q in pairs if p==0)
            k=min(x-1,N-x-1)
            h=sum((0<i<x) ^ (0<j<x) for i,j in pairs if i!=0 and j!=0)
            raw[(k,h)]=raw.get((k,h),0)+1
            return
        i=rest[0]
        for index in range(1,len(rest)):
            j=rest[index]
            pairs.append((i,j))
            rec(rest[1:index]+rest[index+1:])
            pairs.pop()
    rec(tuple(a))
    return raw

counter=0
for n in range(2,8):
    for k in range(n):
        p=dist(n,k)
        assert sum(j*p_j for j,p_j in p.items())==Fraction(k*(2*n-k-2),2*n-3)
        counter+=1
        if k+2<n:
            q=dist(n,k+2)
            assert outranks(p,q)
            for j in p:
                g=Fraction((k+2)*(k+1)*(2*n-2-k-j),(2*n-2-k)*(2*n-3-k)*(k+2-j))
                assert q[j]/p[j]==g
                counter+=1
            assert all(q[j+2]/p[j+2]>q[j]/p[j] for j in p if j+2 in p)
            counter+=1
        if 1<=k<n-1:
            q=dist(n,k+1)
            assert not outranks(p,q) and not outranks(q,p)
            counter+=1
    raw=build_counts(2*n)
    for k in range(n):
        den=sum(v for (a,b),v in raw.items() if a==k)
        for j,p in dist(n,k).items():
            assert Fraction(raw.get((k,j),0),den)==p
            counter+=1
print('VERIFIED:',counter,'checks, including exhaustive matchings through 14 endpoints')
