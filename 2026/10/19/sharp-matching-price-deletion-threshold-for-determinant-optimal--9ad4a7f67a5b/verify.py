#!/usr/bin/env python3
"""Exact checks for the budgeted matching-price spanning-tree design theorem.

Requires only Python 3 standard library. All determinants and objective values
are evaluated over rational numbers; polynomial identities are exact.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def determinant(M):
    """Exact determinant by rational Gaussian elimination."""
    A = [[F(x) for x in row] for row in M]
    N = len(A)
    result = F(1)
    for c in range(N):
        k = next((r for r in range(c, N) if A[r][c]), None)
        if k is None:
            return F(0)
        if k != c:
            A[c], A[k] = A[k], A[c]
            result = -result
        p = A[c][c]
        result *= p
        for r in range(c+1, N):
            if not A[r][c]:
                continue
            scale = A[r][c] / p
            for j in range(c+1, N):
                A[r][j] -= scale * A[c][j]
            A[r][c] = 0
    return result


def cofactor(n,a,b):
    N=2*n
    M=[[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            w=a if i==j else b
            u,v=i,n+j
            M[u][u]+=w;M[v][v]+=w
            M[u][v]-=w;M[v][u]-=w
    return determinant([row[:-1] for row in M[:-1]])


def spectral(n,a,b):
    d=a+(n-1)*b
    return d * (n*b)**(n-1) * (2*a+(n-2)*b)**(n-1) / n


def Q(n,t,y):
    return 2*t*y*y+(4*(n-1)*t-2*n)*y+(2*n-1)*(n-2)*t-n*(2*n-3)


def threshold(n):
    return F(n*(2*n-3), (2*n-1)*(n-2))


def F_prime(n,t,y):
    return (F(1,y+n-1)+F(2*(n-1),2*y+n-2)
            -F((2*n-1)*t,t*y+n-1))


def connected_tree_enumerator(n,a,b):
    """Independent enumeration, viable for n<=4."""
    edges=[(i,n+j,a if i==j else b) for i in range(n) for j in range(n)]
    tot=F(0)
    for selection in combinations(edges,2*n-1):
        parent=list(range(2*n))
        def root(z):
            while parent[z]!=z:
                z=parent[z]
            return z
        product=F(1);count=2*n;is_tree=True
        for u,v,w in selection:
            if w==0:
                is_tree=False;break
            ru,rv=root(u),root(v)
            if ru==rv:
                is_tree=False;break
            parent[ru]=rv
            count-=1
            product*=w
        if is_tree and count==1:
            tot+=product
    return tot


def run():
    tested=0; enumerated=0; derivatives=0;threshold_cases=0
    for n in range(3,9):
        for a,b in [(F(0),F(1)),(F(1),F(1)),(F(2,3),F(1,5)),(F(7,4),F(3,8))]:
            assert cofactor(n,a,b)==spectral(n,a,b),(n,a,b)
            tested+=1
        if n<=4:
            for a,b in [(F(0),F(1)),(F(2,3),F(1,5)),(F(7,4),F(3,8))]:
                assert connected_tree_enumerator(n,a,b)==spectral(n,a,b),(n,a,b)
                enumerated+=1
    for n in range(3,21):
        tc=threshold(n)
        assert tc>1
        assert Q(n,tc,F(0))==0
        assert Q(n,F(1),F(1))==0
        for t in [F(1,9),F(1),tc,F(3,2),F(3)]:
            for y in [F(0),F(1,7),F(1),F(7,3),F(11)]:
                a=y+n-1; b=2*y+n-2;c=t*y+n-1
                # F_prime is log-derivative of reduced tree-count objective.
                lhs=F(1,a)+F(2*(n-1),b)-F((2*n-1)*t,c)
                rhs=-F(n-1)*Q(n,t,y)/(a*b*c)
                assert lhs==rhs,(n,t,y,lhs,rhs)
                derivatives+=1
            const=(2*n-1)*(n-2)*t-n*(2*n-3)
            linear=4*(n-1)*t-2*n
            if t>=tc:
                assert const>=0 and linear>=0
            else:
                assert const<0
            threshold_cases+=1
    for n in range(3,13):
        B=F(13,7); b=B/(n*(n-1))
        tau=(B**(2*n-1)*(n-2)**(n-1)
             /F(n**(n+1)*(n-1)**(2*n-2)))
        assert spectral(n,F(0),b)==tau
    print('VERIFY_OK exact_cofactor_spectra=%s independent_tree_sums=%s exact_log_derivatives=%s threshold_sign_cases=%s'%(tested,enumerated,derivatives,threshold_cases))

if __name__=='__main__': run()
