#!/usr/bin/env python3
"""Independent determinant, burning-bijection and asymptotic checks for cocktail-party avalanches."""
from itertools import product
from fractions import Fraction
from math import exp
from sympy import Matrix


def adj_cp(k):
    return [[j for j in range(2*k) if j!=i and i//2 != j//2] for i in range(2*k)]


def is_recurrent_h(h,m):
    # H: cocktail-party graph on 2(m-1) vertices, plus universal sink.
    k=m-1;adj=adj_cp(k); D=2*m-3
    x=[z+1 for z in h]; burned=[False]*len(x)
    for _ in range(len(x)):
        j=next((j for j in range(len(x)) if not burned[j] and x[j]>=D),None)
        if j is None:return False
        burned[j]=True; x[j]-=D
        for v in adj[j]:x[v]+=1
    return x==list(h)


def full_graph(m):
    n=2*m
    return [[j for j in range(n) if j!=i and i//2!=j//2] for i in range(n)]


def burn_full(z,adj):
    n=len(adj);D=n-2;x=list(z)
    for j in adj[0]:x[j-1]+=1
    done=[False]*n
    for _ in range(n-1):
        k=next((k for k in range(1,n) if not done[k] and x[k-1]>=D),None)
        if k is None:return False
        done[k]=True;x[k-1]-=D
        for j in adj[k]:
            if j:x[j-1]+=1
    return x==list(z)


def topple_full(z,adj):
    n=len(adj);D=n-2;x=list(z);x[0]+=1; t=[0]*(n-1)
    for _ in range(3*n):
        k=next((k for k in range(1,n) if x[k-1]>=D),None)
        if k is None:return tuple(t)
        x[k-1]-=D;t[k-1]+=1
        for j in adj[k]:
            if j:x[j-1]+=1
    raise AssertionError('Exceeded stabilization bound')


def main():
    for m in range(2,11):
        g=full_graph(m); n=2*m;L=Matrix(n-1,n-1,lambda i,j: n-2 if i==j else (-1 if j+1 in g[i+1] else 0))
        # Evaluate both Laplacian determinants directly, independent of spectral derivation.
        total_formula=(n-2)**m*n**(m-2)
        assert L.det(method='domain-ge')==total_formula
        h_adj=adj_cp(m-1);h_size=n-2
        H=Matrix(h_size,h_size,lambda i,j: n-3 if i==j else (-1 if j in h_adj[i] else 0))
        extreme_formula=(n-3)**(m-1)*(n-1)**(m-2)
        assert H.det(method='domain-ge')==extreme_formula
        # Mean odometer: u twice as often as each of the other vertices.
        t=Matrix([Fraction(2,n-2)]+[Fraction(1,n-2)]*(n-2))
        assert L*t==Matrix([1]+[0]*(n-2))
        print('PASS determinant and Green function m=',m,'N=',n)

    # Independent exhaustive test of the recurrent-sandpile restriction map.
    for m in range(2,5):
        D=2*m-2;g=full_graph(m);h_num=2*m-2;count=0
        for h in product(range(D-1),repeat=h_num):
            if not is_recurrent_h(h,m):continue
            count+=1
            low=(0,)+tuple(x+1 for x in h)
            high=(D-1,)+tuple(x+1 for x in h)
            assert burn_full(low,g)
            assert burn_full(high,g)
            assert topple_full(high,g)==(2,)+(1,)*h_num
        assert count==(2*m-3)**(m-1)*(2*m-1)**(m-2)
        print('PASS bijection m=',m,'H_recurrent=',count)

    for m in (20,50,200,1000):
        n=2*m
        p=((n-3)/(n-2))**(m-1)*((n-1)/n)**(m-2)/(n-2)
        # Empirical check of proven limit, not used to infer the limit.
        assert abs(n*p-exp(-1))<2/m
        print('PASS convergence check m=',m,'scaled_extreme_probability=',float(n*p))
    print('ALL_REDUCTION_TESTS_PASS')

if __name__=='__main__':main()
