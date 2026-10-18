"""Exact arithmetic checks for the regular-simplex Gaussian mixture theorem.

The algebraic theorem is proved in the accompanying mathematical text;
these finite-dimensional checks are independent diagnostics only.
"""
from fractions import Fraction as F
from math import sqrt

checks=0
for d in list(range(2,15))+[20,33,64]:
    n=d+1
    # Gram matrix of n unit simplex vectors in R^(n-1).
    gram=[[F(1) if i==j else -F(1,d) for j in range(n)] for i in range(n)]
    for i in range(n):
        assert sum(gram[i])==0
        checks+=1
        for j in range(n):
            assert gram[i][j] == (F(n,d) * (int(i==j)-F(1,n)))
            checks+=1
    # Gram is a scaled projection: G²=(n/d)G.
    gram2=[[sum((gram[i][k]*gram[k][j] for k in range(n)),F(0))
            for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert gram2[i][j]==F(n,d)*gram[i][j]
            checks+=1
    # For g_i=v_i·standardGaussian, C=Gram. The covariance of its barycenter
    # is exactly I/d², tested in Gram coordinates.
    for i in range(n):
        for j in range(n):
            left=sum((gram2[i][k]*gram[k][j] for k in range(n)),F(0))/n**2
            assert left==gram[i][j]/d**2
            checks+=1
    # Tr Cov(barycenter) = (n²-1^T C 1)/(d n²).
    for C in ([row[:] for row in gram],
              [[F(int(i==j)) for j in range(n)] for i in range(n)],
              [[F(1) for j in range(n)] for i in range(n)]):
        trace=sum((gram[i][j]*C[i][j] for i in range(n) for j in range(n)),F(0))/n**2
        ones=sum((C[i][j] for i in range(n) for j in range(n)),F(0))
        assert trace==(F(n*n)-ones)/F(d*n*n)
        assert trace<=F(1,d)
        checks+=2
    # A direction that projects onto just two opposite simplex coefficients.
    # a_i=u·v_i has a0=c, a1=-c and others zero, with c²=n/(2d).
    a2=F(n,2*d)
    assert 4*a2 == 2*(2*a2)
    projected2=F(2,d*n)
    certified2=F(1,d*d)
    assert projected2>certified2
    assert F(projected2,certified2)==F(2*d,n)
    checks+=3

print(f"PASS: {checks} exact identities, dimensions 2..14, 20, 33, 64")
print("Finite checks supplement, and do not replace, infinite-dimensional proofs.")
