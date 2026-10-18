#!/usr/bin/env python3
"""Exact finite rational checks for a split-graph Lipschitz ellipsoid theorem.

The universal theorem follows from a determinant/trace argument; these finite
checks independently replay the proposed projectors, weighted Laplacian,
edge contacts, and boundary transitions. No third-party dependencies.
"""
from fractions import Fraction as F


def proposed(p, q):
    assert p >= 3 and q >= 2
    n, d = p + q, p + q - 1
    if q >= p + 1:
        a, b, c = F(p, d), F(q, d), F(p*q, n*d)
        w, v = F(1, p*q), F(0)
    else:
        a, b, c = F(1, 2), F(p+1, 2*p), F(p+1, 2*n)
        w = F(2, d*(p+1))
        v = F(2*(p+1-q), d*p*(p+1))
    return a, b, c, w, v


def root_widths(p, q, a, b, c):
    clique = 2*a
    cross = F(p-1, p)*a + F(q-1, q)*b + F(p+q, p*q)*c
    return clique, cross


def symmetric_matrices(p, q, a, b, c, w, v):
    n, d = p+q, p+q-1
    S = [[F(0) for _ in range(n)] for _ in range(n)]
    C = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i<p and j<p:
                S[i][j] = a*(F(int(i==j))-F(1,p)) + c*F(q,n*p)
            elif i>=p and j>=p:
                S[i][j] = b*(F(int(i==j))-F(1,q)) + c*F(p,n*q)
            else:
                S[i][j] = -c*F(1,n)
    for i in range(n):
        for j in range(i+1,n):
            wij = v if i<p and j<p else (w if (i<p) != (j<p) else F(0))
            if wij:
                C[i][i]+=wij; C[j][j]+=wij; C[i][j]-=wij; C[j][i]-=wij
    for i in range(n):
        for j in range(n):
            product = sum(S[i][k]*C[k][j] for k in range(n))*d
            wanted = F(int(i==j))-F(1,n)
            assert product==wanted, (p,q,i,j,product,wanted)
    for i in range(n):
        assert sum(S[i])==sum(C[i])==0
    return S, C


def main():
    count=0; cross_checked=0; screened=0; tangent=0; contact=0; matrices=0
    for p in range(3, 21):
        for q in range(2, 21):
            a,b,c,w,v=proposed(p,q)
            cl, cr = root_widths(p,q,a,b,c)
            d=p+q-1
            assert a>0 and b>0 and c>0
            assert p*q*w + F(p*(p-1),2)*v == 1
            assert cr==1 and cl<=1
            # Eigenvalues of weighted graph Laplacian (the design covariance).
            assert a*d*(p*v+q*w)==1
            assert b*d*p*w==1
            assert c*d*(p+q)*w==1
            if q>p+1:
                assert cl<1 and v==0; screened+=1
            elif q==p+1:
                assert cl==1 and v==0; tangent+=1
            else:
                assert cl==1 and v>0; contact+=1
            # Explicit stationarity/dual-leverage certificate in both regimes.
            lam = F(d) if q>=p+1 else F(2*p*q,p+1)
            mu = F(0) if q>=p+1 else F((p-1)*(p+1-q),p+1)
            assert F(p-1,a)==lam*F(p-1,p)+2*mu
            assert F(q-1,b)==lam*F(q-1,q)
            assert F(1,c)==lam*F(p+q,p*q)
            if p<=8 and q<=8:
                symmetric_matrices(p,q,a,b,c,w,v)
                matrices+=1
            count+=1
            cross_checked+=p*q
    assert count==18*19
    print('EXACT_CHECKS_PASS', 'parameter_pairs=',count,
          'cross_edges=',cross_checked,'screened=',screened,
          'boundary_tangent=',tangent,'active=',contact,
          'matrix_identity_cases=',matrices)

if __name__=='__main__':
    main()
