#!/usr/bin/env python3
"""Direct induced-four-path enumeration for matching-deleted complete bipartite graphs.
No structural cograph characterization is used in the brute-force part.
"""
from itertools import combinations
from collections import Counter
from math import comb

def mul(p,q):
    c=Counter()
    for (i,j),a in p.items():
        for (k,l),b in q.items():c[i+k,j+l]+=a*b
    return c

def powers(n,which):
    return Counter({(k,0) if which=='u' else (0,k):comb(n,k) for k in range(n+1)})

def cograph_formula(a,b,t):
    p=Counter({(0,0):1})
    for _ in range(t):p=mul(p,{(0,0):1,(1,0):1,(0,1):1})
    p=mul(mul(p,powers(a-t,'u')),powers(b-t,'v'))
    for k,c in powers(a-1,'u').items():p[k[0]+1,1]+=t*c
    for k,c in powers(b-1,'v').items():p[1,k[1]+1]+=t*c
    p[1,1]-=t
    p[2,2]+=comb(t,2)
    return +p

def facets_formula(n):
    p=Counter({(k,n-k):comb(n,k) for k in range(2,n-1)})
    p[1,n]+=n
    p[n,1]+=n
    p[2,2]+=comb(n,2)
    return +p

def enumerate_graph(a,b,t,facets=False):
    N=a+b
    E=[[False]*N for _ in range(N)]
    for i in range(a):
        for j in range(b):
            if i==j and i<t:continue
            E[i][a+j]=E[a+j][i]=True
    p4=[]
    for q in combinations(range(N),4):
        deg=[sum(E[i][j] for j in q) for i in q]
        if sorted(deg)==[1,1,2,2]:
            p4.append(sum(1<<i for i in q))
    C=Counter();M=Counter();valid=bytearray(1<<N)
    amask=(1<<a)-1
    for s in range(1<<N):
        good=not any((s&q)==q for q in p4)
        valid[s]=good
        if good:C[(s&amask).bit_count(),(s>>a).bit_count()]+=1
    if facets:
        for s in range(1<<N):
            if not valid[s]:continue
            if all(s&(1<<j) or not valid[s|(1<<j)] for j in range(N)):
                M[(s&amask).bit_count(),(s>>a).bit_count()]+=1
    assert C==cograph_formula(a,b,t),('face-count',a,b,t,C,cograph_formula(a,b,t))
    if facets:
        assert M==facets_formula(a),('facet-count',a,b,t,M,facets_formula(a))
    return 1<<N,len(p4)

def main():
    profiles=total=paths=0
    for a in range(1,7):
        for b in range(1,7):
            for t in range(min(a,b)+1):
                c,p=enumerate_graph(a,b,t,facets=(a==b==t and a>=3))
                profiles+=1;total+=c;paths+=p
    for n in (7,8):
        c,p=enumerate_graph(n,n,n,facets=True)
        profiles+=1;total+=c;paths+=p
    comparisons=0
    for a in range(3,31):
        for b in range(3,31):
            for t in range(min(a,b)):
                A=cograph_formula(a,b,t)
                B=cograph_formula(a,b,t+1)
                assert all(A[k]>=B[k] for k in set(A)|set(B)),(a,b,t)
                comparisons+=1
    print(f'VERIFICATION_OK bivariate_profiles={profiles} direct_subsets={total} explicit_P4_masks={paths} crown_facets_orders=3..8 coefficientwise_tests={comparisons}')

if __name__=='__main__':main()
