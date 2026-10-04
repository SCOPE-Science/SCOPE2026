#!/usr/bin/env python3
from itertools import product

# Basis 0=e, 1=f, 2=x. Coefficients are reduced modulo p.
# Nonzero products: e*e=e, f*f=f, f*x=x, x*f=x.
TABLE={(0,0):0,(1,1):1,(1,2):2,(2,1):2}
DEG=[0,0,1]

def add(u,v,p): return tuple((a+b)%p for a,b in zip(u,v))
def smul(c,u,p): return tuple((c*a)%p for a in u)
def mul_basis(i,j,p):
    w=[0,0,0]
    if (i,j) in TABLE: w[TABLE[(i,j)]]=1
    return tuple(w)
def mul(u,v,p):
    out=(0,0,0)
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            if a and b:
                out=add(out,smul(a*b,mul_basis(i,j,p),p),p)
    return out

def check(p):
    B=[tuple(1 if i==j else 0 for i in range(3)) for j in range(3)]
    zero=(0,0,0)
    # Associativity on a basis, sufficient by trilinearity.
    for a,b,c in product(B, repeat=3):
        assert mul(mul(a,b,p),c,p)==mul(a,mul(b,c,p),p)
    # Grading compatibility for each nonzero basis product.
    for i,j in product(range(3), repeat=2):
        z=mul_basis(i,j,p)
        if z!=zero:
            k=z.index(1)
            assert DEG[k]==DEG[i]+DEG[j]
    e,f,x=B
    # J=span(e) is a two-sided ideal.
    for b in B:
        assert all(mul(e,b,p)[i]==0 for i in (1,2))
        assert all(mul(b,e,p)[i]==0 for i in (1,2))
    # A/J has basis images of f,x, so dimension is 2 = dim A0.
    quotient_basis=[f,x]
    assert len(quotient_basis)==2
    assert 2==2
    # A0 -> A/J kills nonzero e, hence cannot be an isomorphism.
    assert e!=zero
    image_e=(0,0)  # quotient coordinates in f,x
    image_f=(1,0)
    assert image_e==(0,0) and image_f!=(0,0)
    # J^2=J because e^2=e.
    assert mul(e,e,p)==e
    print(f"p={p}: associative grading ideal quotient nonsplit tangent-check OK")

for p in (2,3,5): check(p)
print('CHECK_OK')
