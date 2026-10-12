"""Exact computational checks of a rook-graph induced-forest enumerator.

Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def multiply(A, B, m, n):
    C = defaultdict(Fraction)
    for (a,b,e,c),v in A.items():
        for (x,y,f,d),w in B.items():
            if a+x<=m and b+y<=n:
                C[(a+x,b+y,e+f,c+d)] += v*w
    return {k:v for k,v in C.items() if v}


def series_formula(m,n):
    P={}
    for r in range(1,min(m,n)+1):
        P[(r,r,2*r-1,1)]=Fraction(1)
    for r in range(1,min(m-1,n)+1):
        P[(r+1,r,2*r,1)]=Fraction(1,2)
    for r in range(1,min(m,n-1)+1):
        P[(r,r+1,2*r,1)]=Fraction(1,2)
    Q={(0,0,0,0):Fraction(1)}
    accum=defaultdict(Fraction)
    for k in range(0,m+n+1):
        for (a,b,e,c),v in Q.items():
            aa,bb=m-a,n-b
            val = v*Fraction(factorial(m)*factorial(n),factorial(aa)*factorial(bb)*factorial(k))
            accum[(e,c)]+=val
        Q=multiply(Q,P,m,n)
        if not Q: break
    assert all(x.denominator==1 for x in accum.values()),accum
    return {k:int(v) for k,v in accum.items() if v}


def brute(m,n):
    E=[(a,m+b) for a in range(m) for b in range(n)]
    res=defaultdict(int)
    for mask in range(1<<(m*n)):
        deg=[0]*(m+n); par=list(range(m+n)); rank=[0]*(m+n)
        edge_count=0; cycle=False
        def root(k):
            while par[k]!=k:
                par[k]=par[par[k]]
                k=par[k]
            return k
        for i,(u,v) in enumerate(E):
            if not (mask>>i)&1: continue
            edge_count+=1
            deg[u]+=1;deg[v]+=1
            if deg[u]>2 or deg[v]>2:
                cycle=True;break
            ru,rv=root(u),root(v)
            if ru==rv:
                cycle=True; break
            if rank[ru]<rank[rv]:ru,rv=rv,ru
            par[rv]=ru
            if rank[ru]==rank[rv]:rank[ru]+=1
        if not cycle:
            selected=[i for i,d in enumerate(deg) if d]
            c=len({root(i) for i in selected})
            res[(edge_count,c)]+=1
    return dict(res)


def max_formula(m,n):
    if m>n: m,n=n,m
    if m==n: return {(2*m-1,1):factorial(m)**2}
    return {(2*m,k): factorial(m)*factorial(n)//(2**k*factorial(k)*factorial(n-m-k)) * comb(m-1,k-1)
            for k in range(1,min(m,n-m)+1)}


def verify():
    checked=[]; subs=0
    for m in range(2,5):
        for n in range(m,6):
            F=series_formula(m,n)
            B=brute(m,n)
            assert F==B,(m,n,F,B)
            best=max(e for e,c in B)
            observed={key:value for key,value in B.items() if key[0]==best}
            assert observed==max_formula(m,n),(m,n,best,observed,max_formula(m,n))
            checked.append((m,n,len(B),best,sum(observed.values())))
            subs+=2**(m*n)
    assert series_formula(2,2)=={(0,0):1,(1,1):4,(2,1):4,(2,2):2,(3,1):4}
    print('VERIFY_OK boards',checked,'edge_subsets',subs)

if __name__=='__main__':verify()
