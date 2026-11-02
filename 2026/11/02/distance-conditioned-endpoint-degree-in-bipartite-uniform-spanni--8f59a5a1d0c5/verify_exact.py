#!/usr/bin/env python3
"""Standalone exact finite checks for distance-conditioned endpoint degrees in bipartite uniform spanning trees."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def falling(n, t):
    ans = 1
    for j in range(t): ans *= n-j
    return ans


def expected_prob(a,b,t):
    s=t+1
    C=s*(a+b-s)
    return Fraction(falling(a-1,t)*falling(b-1,t)*C, (a*b)**s)


def endpoint_degree_law(a,b,t):
    s=t+1
    B=b-s
    if B == 0:
        return {1:Fraction(1)}
    p=Fraction(1,a)
    q=Fraction(b,s*(a+b-s))
    probs=defaultdict(Fraction)
    for j in range(B):
        z=Fraction(comb(B-1,j))*p**j*(1-p)**(B-1-j)
        probs[1+j]+=z*(1-q)
        probs[2+j]+=z*q
    return {j:v for j,v in probs.items() if v}


def enumerate_bipartite(a,b):
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    n=a+b
    joint=defaultdict(Counter)
    count=0
    for idx in combinations(range(len(edges)), n-1):
        g=[[] for _ in range(n)]
        for z in idx:
            u,v=edges[z];g[u].append(v);g[v].append(u)
        # Find unique path from marked u=0 in A to v=a in B.
        dist=[-1]*n;dist[0]=0;q=[0]
        for u in q:
            for v in g[u]:
                if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
        if len(q)!=n: continue
        t=(dist[a]-1)//2
        joint[t][len(g[0])]+=1
        count+=1
    return count,joint


def exact_checks():
    checks=0
    for a in range(1,6):
        for b in range(1,7):
            if a+b>8 or a*b>18: continue
            total,joint=enumerate_bipartite(a,b)
            assert total == a**(b-1)*b**(a-1)
            checks+=1
            for t in range(min(a,b)):
                ct=sum(joint[t].values()); p=expected_prob(a,b,t)
                assert Fraction(ct,total)==p,(a,b,t,ct,total,p)
                checks+=1
                law=endpoint_degree_law(a,b,t)
                assert sum(law.values(),Fraction())==1
                for degree,pr in law.items():
                    assert Fraction(joint[t][degree],ct)==pr,(a,b,t,degree,joint[t],law)
                    checks+=1
                assert set(joint[t])==set(law)
                checks+=1
            if a>=2 and b>=2:
                for t in range(min(a,b)-1):
                    p0=endpoint_degree_law(a,b,t)
                    p1=endpoint_degree_law(a,b,t+1)
                    for x in set(p0)|set(p1):
                        for y in set(p0)|set(p1):
                            if x>=y:continue
                            # Shorter distance dominates in likelihood-ratio order.
                            assert p1.get(x,Fraction())*p0.get(y,Fraction())>=p1.get(y,Fraction())*p0.get(x,Fraction())
                            checks+=1
    for a in range(2,51):
        for b in range(2,51):
            ps=[expected_prob(a,b,t) for t in range(min(a,b))]
            assert sum(ps)==1
            checks+=1
            e0=Fraction(1)+Fraction(b-1,a)
            deltas=[]
            for t in range(min(a,b)):
                law=endpoint_degree_law(a,b,t)
                d=sum((k*v for k,v in law.items()),Fraction())-e0
                s=t+1
                formula=Fraction(b,s*(a+b-s))-Fraction(s,a)
                assert d==formula,(a,b,t,d,formula)
                deltas.append(d)
                checks+=1
            assert all(x>y for x,y in zip(deltas,deltas[1:])),(a,b,deltas)
            checks+=1
    return checks

if __name__=='__main__':
    print('PASS',exact_checks(),'exact assertions')
