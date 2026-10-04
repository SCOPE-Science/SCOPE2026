#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

# Bivariate polynomials in (L,R): {(degree_L, degree_R): coefficient}.
def add(p,q):
    out=dict(p)
    for m,c in q.items():
        out[m]=out.get(m,F(0))+c
        if out[m]==0: del out[m]
    return out

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            m=(i+k,j+l)
            out[m]=out.get(m,F(0))+a*b
    return {m:c for m,c in out.items() if c}
def C(c): return {} if c==0 else {(0,0):F(c)}
L={(1,0):F(1)}
R={(0,1):F(1)}
R2=mul(R,R)
ONE=C(1)

def det3(M):
    out={}
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        term=ONE
        for i in range(3): term=mul(term,M[i][perm[i]])
        out=add(out, term if inv%2==0 else neg(term))
    return out

expected=add(add(add(mul(mul(L,L),L), mul(sub(ONE,R2),mul(L,L))), mul(sub(ONE,R),L)), sub(ONE,mul(C(2),R)))
for s in (1,-1):
    # L I - J_s(r)
    M=[
      [sub(L,R2), mul(C(-s),sub(ONE,R)), neg(R)],
      [C(s), L, C(0)],
      [R, C(s), add(L,ONE)],
    ]
    assert det3(M)==expected

# Verify AB-C = R(R^2-R+1).
A=sub(ONE,R2); B=sub(ONE,R); Cc=sub(ONE,mul(C(2),R))
left=sub(mul(A,B),Cc)
right=mul(R,add(sub(R2,R),ONE))
assert left==right

# Evaluate the characteristic polynomial coefficients at rational r.
def coeffs(r):
    return [F(1), F(1)-r*r, F(1)-r, F(1)-2*r]

def conv(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

# Descending-coefficient products for boundary factorizations.
assert coeffs(F(-1)) == conv([F(1),F(1)],[F(1),F(-1),F(3)])
assert coeffs(F(0))  == conv([F(1),F(1)],[F(1),F(0),F(1)])
assert coeffs(F(1))  == [F(1),F(0),F(0),F(-1)]
assert coeffs(F(1,2)) == [F(1),F(3,4),F(1,2),F(0)]

# Routh first-column sign patterns at representatives of every open regime.
def sgn(x): return 1 if x>0 else -1 if x<0 else 0
def routh_signs(r):
    A=F(1)-r*r; B=F(1)-r; C=F(1)-2*r
    assert A!=0
    D=(A*B-C)/A
    return tuple(map(sgn,[F(1),A,D,C]))
assert routh_signs(F(-2)) == (1,-1,1,1)
assert routh_signs(F(-1,2)) == (1,1,-1,1)
assert routh_signs(F(1,4)) == (1,1,1,1)
assert routh_signs(F(3,4)) == (1,1,1,-1)
assert routh_signs(F(2)) == (1,-1,-1,-1)

print("VERIFY_OK")
