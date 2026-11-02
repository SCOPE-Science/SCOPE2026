#!/usr/bin/env python3
"""Exact Cartier polynomial identities for y^5-y=x^8+a*x^4+b*x^6.

All arithmetic is in F_5[A,B], with A^5=a, B^5=b.
The coefficient field is represented by sparse monomials A^i B^j.
"""
from math import comb
P=5

def clean(POL):
    return {m:c%P for m,c in POL.items() if c%P}

def add(f,g):
    ans=dict(f)
    for m,c in g.items():ans[m]=(ans.get(m,0)+c)%P
    return clean(ans)

def scale(f,c):return clean({m:c*v for m,v in f.items()})

def mul(f,g):
    ans={}
    for (a,b),v in f.items():
        for (c,d),w in g.items():
            key=(a+c,b+d)
            ans[key]=(ans.get(key,0)+v*w)%P
    return clean(ans)

def poly_x_mul(f,g):
    ans={}
    for i,v in f.items():
        for j,w in g.items():ans[i+j]=add(ans.get(i+j,{}),mul(v,w))
    return {i:v for i,v in ans.items() if v}

def crt(i,j,f_powers):
    """C(x^i y^j dx) via y^j=(y^5-f)^j."""
    ans={}
    for k in range(j+1):
        sign=comb(j,k)*(-1)**(j-k)
        for e,v in f_powers[j-k].items():
            if (i+e)%5 != 4:continue
            xpower=(i+e-4)//5
            root={}
            for (a,b),c in v.items():
                assert a%5==b%5==0
                root[(a//5,b//5)]=c
            key=(xpower,k)
            ans[key]=add(ans.get(key,{}),scale(root,sign))
    return {key:val for key,val in ans.items() if val}

A={(1,0):1};B={(0,1):1};ONE={(0,0):1}
f={8:ONE,4:{(5,0):1},6:{(0,5):1}}
fp=[{0:ONE}]
for j in range(3):fp.append(poly_x_mul(fp[-1],f))
BASIS=[(i,j) for j in range(4) for i in range((26-8*j)//5+1)]
assert len(BASIS)==14
images={q:crt(*q,fp) for q in BASIS}
expected={
    (4,0):{(0,0):ONE},
    (0,1):{(0,0):scale(A,-1)},
    (1,1):{(1,0):scale(ONE,-1)},
    (3,1):{(1,0):scale(B,-1)},
    (0,2):{(2,0):scale(B,2),(0,1):scale(A,-2)},
    (1,2):{(1,0):mul(A,A),(1,1):scale(ONE,-2)},
    (2,2):{(2,0):add(scale(A,2),mul(B,B))},
    (0,3):{(2,0):scale(mul(mul(A,A),B),2),
           (4,0):scale(ONE,-1),(2,1):B,(0,2):scale(A,2)},
}
for q in BASIS:
    assert images[q]==expected.get(q,{}), (q,images[q],expected.get(q,{}))
# The four permanent pivot columns are indexed by (4,0),(1,1),(1,2),(0,3).
# The remaining rank is a two-by-two block with columns (0,2),(2,2).
minor=add(scale(mul(A,add(scale(A,2),mul(B,B))),2),{})
assert minor == {(2,0):4,(1,2):2},minor
# Frobenius sends the two factors to a and 2a+b^2, respectively.
assert {(5*a,5*b):c for (a,b),c in minor.items()}=={(10,0):4,(5,10):2}
# The +1-involution eigenspace has six basis forms (i odd), and rank exactly 2.
assert len([q for q in BASIS if q[0]%2])==6
assert {q for q in BASIS if q[0]%2 and images[q]}=={(1,1),(3,1),(1,2)}
print('SYMBOLIC_CARTIER_AND_PRYM_OK')
