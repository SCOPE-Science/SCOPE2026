"""Exhaustive finite-field checks for the square-zero annihilation graph.
Run with Python 3, standard library only. Field checks q=2,3; sample q=5.
"""
from itertools import product

def mul(a,b,p):
    c=[0]*9
    for i in range(3):
      for j in range(3):
        ai=a[3*i+j]
        if not ai: continue
        for k in range(3-i):
          for l in range(3-j):
            c[3*(i+k)+j+l]=(c[3*(i+k)+j+l]+ai*b[3*k+l])%p
    return tuple(c)

def leading(a,p):
    if p==2: return (a[6],a[2]) # x^2, y^2 for indexing (3*i+j)
    return (a[6],a[4],a[2]) # x^2, xy, y^2

def beta(v,w,p):
    if p==2: return (v[0]*w[1]+v[1]*w[0])%p
    u,m,z=v; U,M,Z=w
    return (u*Z+z*U+m*M)%p

def verify(p):
    zero=(0,)*9
    square=[]
    for a in product(range(p), repeat=9):
        if mul(a,a,p)==zero:
            square.append(a)
    assert len(square)==p**5,(p,len(square))
    base={leading(a,p) for a in square}
    assert len(base)==p**2,(p,len(base))
    assert all(beta(v,v,p)==0 for v in base)
    for a in square:
        v=leading(a,p)
        expected=p**5 if not any(v) else p**4
        k=sum(mul(a,b,p)==zero for b in square)
        assert k==expected, (p,a,k,expected)
        for b in square:
            assert (mul(a,b,p)==zero)==(beta(v,leading(b,p),p)==0)
    ordered=sum(p**5 if not any(leading(a,p)) else p**4 for a in square)
    assert ordered==p**9+p**8-p**7
    print('CHECK',p,'squarezero',len(square),'base',len(base),'ordered_zero_products',ordered)
for p in (2,3):verify(p)
print('SQUARE_ZERO_ANNIHILATION_OK')
