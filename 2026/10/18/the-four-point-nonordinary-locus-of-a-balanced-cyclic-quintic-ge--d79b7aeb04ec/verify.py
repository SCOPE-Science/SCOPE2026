#!/usr/bin/env python3
"""Exact polynomial Cartier calculation over F_11 for a genus-four cyclic cover.

Run with: python3 verify.py. Requires only the Python standard library.
The proof over an algebraic closure is explained in RESULT.md; this program
checks the exact universal polynomial identities used in that proof.
"""
P = 11

def normalize(d):
    return {k: v % P for k, v in d.items() if v % P}

def add(a,b):
    d = dict(a)
    for k,v in b.items(): d[k] = (d.get(k,0)+v)%P
    return normalize(d)

def neg(a): return {k:(-v)%P for k,v in a.items()}

def sub(a,b): return add(a,neg(b))

def mul(a,b):
    d = {}
    for (i,j),c in a.items():
        for (u,v),e in b.items():
            k=(i+u,j+v)
            d[k]=(d.get(k,0)+c*e)%P
    return normalize(d)

def powp(a,n):
    z=ONE
    while n:
        if n&1: z=mul(z,a)
        a=mul(a,a);n//=2
    return z

def scale(a,c):return normalize({k:c*v for k,v in a.items()})

def coeff_x(a,i):return normalize({(0,j):c for (k,j),c in a.items() if k==i})

def degree_x(a):return max(i for i,j in a)

ONE={(0,0):1}; X={(1,0):1}; T={(0,1):1}
F=mul(X,mul(powp(sub(X,ONE),2),powp(sub(X,T),3)))
H=[ONE,sub(X,T),mul(sub(X,ONE),sub(X,T)),mul(sub(X,ONE),powp(sub(X,T),2))]
A=add(sub(powp(T,2),scale(T,5)),scale(ONE,-4))
B=add(add(powp(T,2),scale(T,4)),scale(ONE,-3))
expected=[scale(A,4),scale(B,-5),mul(scale(B,-5),powp(T,4)),mul(scale(A,4),powp(T,2))]
assert degree_x(F)==6
for j,h in enumerate(H,1):
    r=degree_x(h)
    G=mul(h,powp(F,2*j))
    lead=coeff_x(G,10+11*r)
    assert lead==expected[j-1], ('leading coefficient',j,lead,expected[j-1])
    h11=powp(h,11)
    for k in range(r+1):
        actual=coeff_x(G,10+11*k)
        predicted=mul(lead,coeff_x(h11,11*k))
        assert actual==predicted, ('Cartier proportionality',j,k,actual,predicted)
    assert degree_x(G)<10+11*(r+1)
    print('j =',j,'holomorphic basis degree',r,'Cartier coefficients verified')
assert A == normalize({(0,2):1,(0,1):-5,(0,0):-4})
assert B == normalize({(0,2):1,(0,1):4,(0,0):-3})
# x^2 A(1/x) and x^2 B(1/x) are reciprocal quadratics.
reciprocalB=normalize({(0,2-i):v for (k,i),v in B.items()})
assert scale(reciprocalB,-pow(3,-1,P))==A
# Discriminants 8 and 6 are quadratic nonresidues in F_11.
squares={z*z%P for z in range(P)}
assert (25+16)%P==8 and 8 not in squares
assert (16+12)%P==6 and 6 not in squares
# Relatively prime, and no boundary roots: exhaustive F_11 checks + degree 2 irreducible.
for t in range(P):
    av=(t*t-5*t-4)%P
    bv=(t*t+4*t-3)%P
    assert av and bv
# Different irreducible quadratics cannot have common algebraic roots.
assert A!=B
print('Both quadratics separable and irreducible over F_11; their roots are four distinct points in F_121.')
print('VERIFICATION_OK')
