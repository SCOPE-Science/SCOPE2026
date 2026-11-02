"""Independent checks of induced-forest enumerators for Cartesian clique products.
Uses native graph adjacency and cycle detection, not line-graph characterization,
then verifies exact labeled component assembly, maximum counts and phase cases.
"""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from math import comb,factorial

# Induced forest on rook graph: adjacency by same row or same column.
def direct_counts(m,n):
    v=m*n
    nbr=[0]*v
    for i in range(v):
        a,b=divmod(i,n)
        for j in range(v):
            c,d=divmod(j,n)
            if i!=j and (a==c or b==d): nbr[i]|=1<<j
    pol=[0]*(v+1)
    for mask in range(1<<v):
        # Kruskal union-find over edges of induced subgraph.
        parent=list(range(v))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        valid=True
        for i in range(v):
            if not (mask>>i)&1: continue
            adj=nbr[i]&mask&~((1<<(i+1))-1)
            while adj:
                bit=adj&-adj; adj-=bit; j=bit.bit_length()-1
                ri,rj=find(i),find(j)
                if ri==rj: valid=False;break
                parent[ri]=rj
            if not valid:break
        if valid:pol[mask.bit_count()]+=1
    return pol

# Connected bipartite path counts by the two part sizes. Weights z^(a+b-1).
def path_count(a,b):
    if (a,b) in ((1,0),(0,1)):return 1
    if a>=1 and a==b:return factorial(a)*factorial(b)
    if a>=1 and b>=1 and abs(a-b)==1:return factorial(a)*factorial(b)//2
    return 0

@lru_cache(None)
def component_counts(m,n):
    if (m,n)==(0,0):return (1,)
    totals=[0]*(m*n+1)
    if m:
        for a in range(1,m+1):
            for b in range(n+1):
                k=path_count(a,b)
                if not k: continue
                weight=comb(m-1,a-1)*comb(n,b)*k
                for t,z in enumerate(component_counts(m-a,n-b)):
                    if t+a+b-1<len(totals):totals[t+a+b-1]+=weight*z
    else:
        for b in range(1,n+1):
            k=path_count(0,b)
            if not k:continue
            weight=comb(n-1,b-1)*k
            for t,z in enumerate(component_counts(0,n-b)):
                if t+b-1<len(totals):totals[t+b-1]+=weight*z
    return tuple(totals)

# Count ordinary linear forests on n labeled right vertices with m edges.
def linear_forests_n_m(n,m):
    if m>n-1:return 0
    if m==0:return 1
    c=n-m
    # Path component formula: ordinary labeled path on k vertices is k!/2 for k>=2.
    # Formula L(n,m) = n!/c! sum_j binom(c,j) * 2^-j * binom(m-1,j-1).
    from fractions import Fraction
    val=sum((Fraction(comb(c,j)*comb(m-1,j-1),2**j)
             for j in range(1,min(c,m)+1)),start=Fraction())
    z=Fraction(factorial(n),factorial(c))*val
    assert z.denominator==1
    return z.numerator


def expected_top(m,n):
    if m>n:m,n=n,m
    if m==n:return 2*m-1,factorial(m)**2
    return 2*m,factorial(m)*linear_forests_n_m(n,m)

cases=[]
for m,n in [(1,1),(1,2),(1,4),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),(3,6),(4,5)]:
    # independent native graph testing whenever possible
    poly=component_counts(m,n)
    top=max(i for i,x in enumerate(poly) if x)
    t,c=expected_top(m,n)
    assert (top,poly[top])==(t,c),(m,n,top,poly[top],t,c)
    if m*n<=16:
        direct=direct_counts(m,n)
        assert tuple(direct[:len(poly)])==poly,(m,n,direct,poly)
        assert all(v==0 for v in direct[len(poly):])
    cases.append((m,n,top,poly[top],sum(poly)))
print('VERIFY_OK',len(cases),'cases',component_counts.cache_info())
for x in cases:print(' ',x)

# Independent arithmetic expansion of the claimed rational multivariate EGF.
from fractions import Fraction

def polyprod(A,B,M,N):
    out={}
    for (i,j,k),u in A.items():
        for (a,b,c),v in B.items():
            if i+a<=M and j+b<=N:
                idx=(i+a,j+b,k+c)
                out[idx]=out.get(idx,Fraction())+u*v
    return out

def egf_coefficient(M,N):
    P={}
    for r in range(min(M,N)):
        a=b=r+1
        if a<=M and b<=N:P[(a,b,2*r+1)]=Fraction(1)
    for r in range(1,max(M,N)+1):
        for a,b in ((r+1,r),(r,r+1)):
            if a<=M and b<=N:P[(a,b,2*r)]=Fraction(1,2)
    # All terms in P consume at least one of each shore, so at most min(M,N) factors.
    ep={(0,0,0):Fraction(1)}
    term={(0,0,0):Fraction(1)}
    for h in range(1,min(M,N)+1):
        term=polyprod(term,P,M,N)
        term={key:value/Fraction(h) for key,value in term.items()}
        for idx,value in term.items():ep[idx]=ep.get(idx,Fraction())+value
    out=[0]*(M*N+1)
    for (a,b,k),value in ep.items():
        val=value*Fraction(factorial(M),factorial(M-a))*Fraction(factorial(N),factorial(N-b))
        assert val.denominator==1,(M,N,a,b,k,val)
        out[k]+=int(val)
    return tuple(out)

for mm,nn in [(2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(4,5),(5,5)]:
    a=egf_coefficient(mm,nn)
    b=component_counts(mm,nn)
    assert a==b,(mm,nn,a,b)
print('EGF_VERIFY_OK 8 exact rational coefficient expansions')
