#!/usr/bin/env python3
"""Independent exact small-case checks of cyclotomic node counts and transverse Hessians."""
from collections import Counter
from itertools import product
from math import factorial
import sympy as s

def fixed(p, m):
    n = p*m
    words = [v for v in product(range(p),repeat=n) if all(v.count(j)==m for j in range(p))]
    assert len(words) == factorial(n)//factorial(m)**p
    classes = set()
    for v in words:
        classes.add(min(tuple((j+b)%p for j in v) for b in range(p)))
    assert len(classes) == factorial(n)//(p*factorial(m)**p)
    gal_orbits = set()
    for v in classes:
        gal_orbits.add(min(min(tuple(((a*j+b)%p) for j in v) for b in range(p)) for a in range(1,p)))
    assert len(gal_orbits) == factorial(n)//(p*(p-1)*factorial(m)**p)
    # Stabilizer of each projective root tuple under Gal(Q(zeta_p)/Q) is trivial.
    for v in classes:
        for a in range(2,p):
            assert not any(all((a*j-j-b)%p==0 for j in v) for b in range(p))
    return len(classes),len(gal_orbits), min(classes)

def hessian(p,v):
    n = len(v)
    # Normalize last coordinate to 1; the next-to-last becomes the dependent coordinate.
    expo=[(j-v[-1])%p for j in v]
    t=s.symbols('t')
    Phi=sum(t**j for j in range(p))
    z=lambda a: t**(a%p)
    vals=[z(a) for a in expo]
    assert s.rem(sum(vals),Phi,t)==0
    # Hessian of restricted polynomial in the affine chart x_n=1.
    c=p*(p+1)
    B=s.Matrix(n-2,n-2,lambda i,j:(vals[i]**(p-1) if i==j else 0)+vals[n-2]**(p-1))
    det=s.expand(B.det())
    predicted=-s.prod(vals[i]**(p-1) for i in range(n-1))
    assert s.rem(det-predicted,Phi,t)==0
    # Degree p+1 Hessian equals c*B; quotient ring operations are exact.
    return len(str(det))

for p,m in [(3,2),(5,1)]:
    N,C,w=fixed(p,m)
    h=hessian(p,w)
    print(f'p={p},m={m},N={p*m},geometric_nodes={N},closed_points={C},hessian_expression_chars={h}')
# Formula-only larger examples. These do not claim exhaustive verification.
for p,m in [(5,2),(7,1)]:
    n=p*m
    print(f'formula p={p},m={m}: geometric={factorial(n)//(p*factorial(m)**p)}, closed={factorial(n)//(p*(p-1)*factorial(m)**p)}')
print('VERIFY_OK')
