"""Exact finite checks of multipartite random spanning-tree cross-part leaf covariance.
The exhaustive calculations are not a proof for arbitrary graph orders.
Run: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from math import prod


def decode_prufer(code,n):
    deg=[1]*n
    for x in code: deg[x]+=1
    edges=[]
    for x in code:
        y=next(i for i in range(n) if deg[i]==1)
        edges.append((x,y));deg[x]-=1;deg[y]-=1
    rest=[i for i in range(n) if deg[i]==1]
    return edges+[(rest[0],rest[1])]


def formula(parts,i=0,j=1):
    n=sum(parts);r=len(parts)
    assert n>=2 and r>=2 and all(v>=1 for v in parts) and i!=j
    def p(t):
        v=Fraction(n-1,n)**(r-2)
        for k,a in enumerate(parts):
            if k!=t: v*=Fraction(n-a-1,n-a)**(a-1)
        return v
    q=Fraction(1) if r==2 else Fraction(n*(n-2),(n-1)**2)**(r-2)
    for k,a in enumerate(parts):
        if k not in (i,j) and a>1:
            d=n-a
            q*=Fraction(d*(d-2),(d-1)**2)**(a-1)
    pi,pj=p(i),p(j)
    return pi,pj,pi*pj*q,Fraction(parts[i]*parts[j])*pi*pj*(q-1),q


def count_trees(parts):
    n=sum(parts);r=len(parts)
    return n**(r-2)*prod((n-a)**(a-1) for a in parts)


def enumerate_case(parts):
    r=len(parts);n=sum(parts)
    starts=[0]
    for x in parts: starts.append(starts[-1]+x)
    part=[next(i for i in range(r) if starts[i]<=u<starts[i+1]) for u in range(n)]
    counts=0;mom=[0]*6
    for word in product(range(n),repeat=n-2):
        edges=decode_prufer(word,n)
        if any(part[a]==part[b] for a,b in edges):continue
        counts+=1
        deg=[0]*n
        for a,b in edges:deg[a]+=1;deg[b]+=1
        la=sum(deg[v]==1 for v in range(starts[0],starts[1]))
        lb=sum(deg[v]==1 for v in range(starts[1],starts[2]))
        Ia=(deg[starts[0]]==1);Ib=(deg[starts[1]]==1)
        for i,x in enumerate((Ia,Ib,Ia*Ib,la,lb,la*lb)):mom[i]+=x
    assert counts==count_trees(parts),(parts,counts,count_trees(parts))
    pi,pj,pij,cov,q=formula(parts)
    actual=[Fraction(x,counts) for x in mom]
    expect=[pi,pj,pij,parts[0]*pi,parts[1]*pj,parts[0]*parts[1]*pij]
    for a,b in zip(actual,expect):assert a==b,(parts,actual,expect)
    assert actual[5]-actual[3]*actual[4]==cov
    assert (cov==0)==(r==2 or pi*pj==0)
    return counts,9


def algebra_checks():
    cases=0
    for r in range(2,7):
        for parts in product(range(1,6),repeat=r):
            if sum(parts)>14:continue
            pi,pj,pij,cov,q=formula(parts)
            assert 0<=pi<=1 and 0<=pj<=1 and 0<=pij<=min(pi,pj)
            assert (cov==0)==(r==2 or pi*pj==0)
            assert cov<=0
            if r>=3:assert cov<0
            cases+=1
    return cases*5

if __name__=='__main__':
    shapes=[(1,1),(1,2),(1,3),(2,2),(2,3),(3,3),
            (1,1,1),(1,1,2),(1,2,2),(2,2,2),
            (1,1,3),(1,2,3),(1,1,1,1),(1,1,1,2),
            (1,1,2,2),(1,1,1,1,1),(2,1,2,1),(1,1,1,1,1,1),(2,2,2,2),(1,1,1,1,1,1,1,1)]
    trees=assertions=0
    for p in shapes:
        t,a=enumerate_case(p);trees+=t;assertions+=a
    assertions+=algebra_checks()
    print(f'VERIFY_OK trees={trees} assertions={assertions} cases={len(shapes)}')
