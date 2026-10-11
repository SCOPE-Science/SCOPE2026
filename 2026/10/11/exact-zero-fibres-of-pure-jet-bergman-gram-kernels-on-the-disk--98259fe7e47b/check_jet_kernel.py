"""Finite corroboration of unit-disk normalized jet-kernel and Jacobi identities; not an infinite proof."""
from fractions import Fraction
from math import comb, factorial
from scipy.special import roots_jacobi
import sympy as s

x,t=s.symbols('x t')
for m in range(0,13):
    p=s.Poly(sum(comb(m,j)*comb(m+1,j)*t**j for j in range(m+1)),t)
    # Cayley-Jacobi transform, exact polynomial equality.
    q=s.Poly(s.cancel((1-t)**m*s.jacobi(m,0,1,(1+t)/(1-t))),t)
    assert p==q,(m,p,q)
    assert s.expand((1+x)*s.jacobi(m,0,1,x)-s.legendre(m,x)-s.legendre(m+1,x))==0
    assert p.eval(-1)!=0
    # First coefficients from independent differentiated kernel series.
    for j in range(0,9):
        # Series after dividing the m-th derivative by m!: (j+m+1)*binom(j+m,m)^2/pi
        direct=Fraction((j+m+1)*factorial(j+m)**2,factorial(j)**2*factorial(m)**2)
        # Derived rational formula: (m+1)*P_m(t)*(1-t)^(-2m-2)/pi
        closed=sum(Fraction((m+1)*comb(m,k)*comb(m+1,k)*comb(2*m+1+j-k,2*m+1),1) for k in range(min(j,m)+1))
        assert direct==closed,(m,j,direct,closed)
    if m:
        roots,_=roots_jacobi(m,0,1)
        assert all(-1<r<1 for r in roots)
        assert abs(roots).min()>1e-8
        npos=sum(r>0 for r in roots)
        assert npos==(m+1)//2,(m,npos)
print('VERIFY_OK Jacobi transforms and Legendre identities: m=0..12; kernel coefficients: m=0..12, j=0..8; positive Jacobi root counts: m=1..12.')
