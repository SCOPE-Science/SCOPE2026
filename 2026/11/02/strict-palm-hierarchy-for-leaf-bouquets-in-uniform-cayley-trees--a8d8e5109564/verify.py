"""Exact enumerative checks for leaf-bouquet covariance identities."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

def statistics(code, n):
    degree = [1]*n
    for v in code:
        degree[v] += 1
    edges=[]
    for v in code:
        u=next(i for i in range(n) if degree[i]==1)
        edges.append((u,v))
        degree[u]-=1
        degree[v]-=1
    last=[i for i in range(n) if degree[i]==1]
    edges.append(tuple(last))
    d=[0]*n
    for u,v in edges:
        d[u]+=1;d[v]+=1
    leaves=sum(x==1 for x in d)
    leaf_neighbors=[0]*n
    for u,v in edges:
        if d[u]==1: leaf_neighbors[v]+=1
        if d[v]==1: leaf_neighbors[u]+=1
    return leaves,[sum(comb(z,k) for z in leaf_neighbors if z>=k) for k in range(1,n)]

def p(m):
    if m==1: return Fraction(1)
    return Fraction(m-1,m)**(m-2)

def ex_leaf(n): return n*p(n)

def ex_bouquet(n,k):
    m=n-k
    return Fraction(n*comb(n-1,k),n**(n-2))*(m**(m-2) if m>1 else 1)

def delta(n,k):
    m=n-k
    return Fraction(k) + ((m-1)*p(m) if m>1 else 0) - ex_leaf(n)

def check():
    assertions=0
    for n in range(3,9):
        num=n**(n-2)
        sumL=0;sumB=[0]*(n-1);sumLB=[0]*(n-1)
        for code in product(range(n),repeat=n-2):
            L,B=statistics(code,n)
            sumL+=L
            for i,x in enumerate(B):sumB[i]+=x;sumLB[i]+=x*L
        assert Fraction(sumL,num)==ex_leaf(n); assertions+=1
        for k in range(1,n):
            EB=Fraction(sumB[k-1],num)
            cov=Fraction(sumLB[k-1],num)-Fraction(sumL,num)*EB
            assert EB==ex_bouquet(n,k); assertions+=1
            assert cov==EB*delta(n,k); assertions+=1
            if n>=4: assert cov>0; assertions+=1
        if n>=4:
            d=[delta(n,k) for k in range(1,n)]
            assert all(d[k+1]>d[k] for k in range(n-3)); assertions+=1
            assert d[-1]==d[-2]; assertions+=1
    return assertions

if __name__=='__main__':
    print('Exact assertions passed:',check())
