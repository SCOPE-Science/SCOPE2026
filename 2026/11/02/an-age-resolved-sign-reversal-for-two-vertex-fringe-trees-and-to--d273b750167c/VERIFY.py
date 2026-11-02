#!/usr/bin/env python3
"""Exact finite-instance checks for marked two-vertex fringe trees."""
from fractions import Fraction
from collections import Counter
from itertools import product
from math import factorial, log, exp

def harmonic(k):
    return sum((Fraction(1,j) for j in range(1,k+1)),Fraction())

def expected(n,i):
    p=Fraction((i-1)*(n-i),(n-1)*(n-2))
    g=2*(harmonic(i-1)-harmonic(n-2))+Fraction(n-2,n-1)
    return p,g

def tree_data(parents):
    n=len(parents)-1
    dep=[0]*(n+1)
    sz=[1]*(n+1)
    children=[[] for _ in range(n+1)]
    for j in range(2,n+1):
        v=parents[j]
        dep[j]=dep[v]+1
        children[v].append(j)
    for j in range(n,1,-1):
        sz[parents[j]]+=sz[j]
    path=sum(dep)
    child2={i:children[i][0] for i in range(2,n) if sz[i]==2 and len(children[i])==1 and sz[children[i][0]]==1}
    return path,child2

def main():
    assertions=0
    total_examined=0
    for n in range(3,10):
        sum_p=0
        sz_count={i:0 for i in range(2,n)}
        sum_zp={i:0 for i in range(2,n)}
        child_distributions={(i,j):Counter() for i in range(2,n) for j in range(i+1,n+1)}
        total=factorial(n-1)
        for par in product(*(range(1,j) for j in range(2,n+1))):
            parents=[0,0]+list(par)
            path,cherry=tree_data(parents)
            sum_p+=path
            for i,j in cherry.items():
                sz_count[i]+=1
                sum_zp[i]+=path
                child_distributions[(i,j)][path]+=1
            total_examined+=1
        assert Fraction(sum_p,total)==n*(harmonic(n)-1)
        assertions+=1
        for i in range(2,n):
            p,g=expected(n,i)
            assert Fraction(sz_count[i],total)==p, (n,i,"prob",sz_count[i],p)
            assertions+=1
            cov=Fraction(sum_zp[i],total)-Fraction(sz_count[i]*sum_p,total*total)
            assert cov==p*g,(n,i,"cov",cov,p*g)
            assertions+=1
            dist0=child_distributions[(i,i+1)]
            for j in range(i+1,n+1):
                dist=child_distributions[(i,j)]
                assert sum(dist.values())==total*Fraction(i-1,(n-1)*(n-2))
                assertions+=1
                assert dist==dist0,(n,i,j,"conditional distribution differs")
                assertions+=1
                mean=Fraction(sum(x*c for x,c in dist.items()),sum(dist.values()))
                assert mean==(n-2)*(harmonic(n-2)-1)+2*harmonic(i-1)+1
                assertions+=1
    for n in range(4,300):
        gg=[expected(n,i)[1] for i in range(2,n)]
        assert gg[0]<0 and gg[-1]>0
        assert all(a<b for a,b in zip(gg,gg[1:]))
        assertions+=2
    a=exp(-0.5)
    for n in (500,2000,10000):
        i=round(n*0.45)
        p,g=expected(n,i)
        target=(i/n)*(1-i/n)*(1+2*log(i/n))
        assert abs(float(p*g)-target)<0.012
        assertions+=1
    print(f"PASS: {total_examined} recursive trees enumerated; {assertions} exact and asymptotic diagnostic assertions")

if __name__=='__main__': main()
