"""Exact checks for local components of two noncrossing matchings.
Run: python check_meanders.py
"""
from functools import lru_cache
from fractions import Fraction
from collections import Counter,defaultdict
from math import comb

@lru_cache(None)
def matchings(nodes):
    if not nodes:
        return ((),)
    a=nodes[0]
    out=[]
    for k in range(1,len(nodes),2):
        b=nodes[k]
        for inner in matchings(nodes[1:k]):
            for rest in matchings(nodes[k+1:]):
                out.append(((a,b),)+inner+rest)
    return tuple(out)

def partner(m,N):
    p=[-1]*N
    for a,b in m: p[a]=b;p[b]=a
    return tuple(p)

def catalan(n): return comb(2*n,n)//(n+1)

def q(n,r):
    if r>n: return Fraction(0)
    return Fraction(catalan(n-r),catalan(n))

def statistics(a,b,n):
    N=2*n
    x=sum(a[i]==i+1 and b[i]==i+1 for i in range(N-1))
    plus=minus=0
    for i in range(N-3):
        h=(a[i]==i+1 and a[i+2]==i+3)
        v=(a[i]==i+3 and a[i+1]==i+2)
        k=(b[i]==i+1 and b[i+2]==i+3)
        w=(b[i]==i+3 and b[i+1]==i+2)
        plus+=bool(h and w)
        minus+=bool(v and k)
    return x,plus,minus

def verify(n):
    N=2*n
    p=[partner(m,N) for m in matchings(tuple(range(N)))]
    tally=Counter()
    for a in p:
        for b in p:
            tally[statistics(a,b,n)]+=1
    total=len(p)**2
    mean=lambda f:sum(Fraction(v*f(*key),total) for key,v in tally.items())
    ex=mean(lambda x,u,v:x)
    ep=mean(lambda x,u,v:u)
    em=mean(lambda x,u,v:v)
    expm=mean(lambda x,u,v:u*v)
    explus=mean(lambda x,u,v:x*u)
    exminus=mean(lambda x,u,v:x*v)
    mx=mean(lambda x,u,v:x*x)
    mp=mean(lambda x,u,v:u*u)
    # exact Catalan deletion moments
    assert ex==(2*n-1)*q(n,1)**2,(n,'ex')
    assert ep==em==(2*n-3)*q(n,2)**2,(n,'ep')
    assert mx-ex==(2*n-2)*(2*n-3)*q(n,2)**2,(n,'ex2')
    D=sum(max(0,j-2)+max(0,2*n-j-4) for j in range(1,2*n-2))
    assert D==(2*n-6)*(2*n-3)+2 if n>=3 else D==0,(n,'D')
    if n>=3:
        assert explus==exminus==D*q(n,3)**2,(n,'cross x y')
    if n>=4:
        assert expm==(2*n-6)*(2*n-7)*q(n,4)**2,(n,'cross plus minus')
        assert mp-ep==(2*n-6)*(2*n-7)*q(n,4)**2,(n,'within plus')
    # independent fair 2-way orientations given total Y and X
    h=defaultdict(Counter)
    for (x,u,v),count in tally.items(): h[(x,u+v)][u]+=count
    for (x,y),sub in h.items():
        size=sum(sub.values())
        for j in range(y+1):
            assert sub[j]*2**y==size*comb(y,j),(n,x,y,j,sub,size)
    if n>=4:
        c=xplus_cov=explus-ex*ep
        v=expm-ep*em
        assert c<0 and v<0,(n,c,v)
    return n,total,len(tally),float(ex),float(ep),float((explus-ex*ep) if n>=3 else 0)

if __name__=='__main__':
    for n in range(2,8):print(verify(n))
    print('All exact enumeration and conditional binomial checks passed.')
