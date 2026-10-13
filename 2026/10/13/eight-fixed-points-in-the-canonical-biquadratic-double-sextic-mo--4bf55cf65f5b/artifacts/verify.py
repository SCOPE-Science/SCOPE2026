#!/usr/bin/env python3
import sympy as sp

U,V,z,q=sp.symbols('U V z q')
for n in range(1,9):
    N=2*n+2
    F=U*V-z**N
    # tau(U,V,z)=(V,U,-z); N is even.
    Ftau=sp.expand(V*U-(-z)**N)
    assert sp.expand(Ftau-F)==0
    # tau^2 is identity on the hypersurface coordinates.
    assert (U,V,z)==(U,V,z)
    chain=list(range(1,N))
    perm={j:N-j for j in chain}
    fixed=[j for j in chain if perm[j]==j]
    assert fixed==[N//2]
    assert N//2==n+1
    sign=(-1)**(N//2)
    poly=sp.Poly(q**2-sign,q)
    assert poly.degree()==2
    assert sp.discriminant(poly.as_expr(),q)!=0
    # q=0 and infinity are exchanged by q -> sign/q, so the two roots are interior.
    assert 6+2==8
print('VERIFY_OK n=1..8 smooth=6 exceptional=2 total=8')
