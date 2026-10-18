#!/usr/bin/env python3
"""Exact checks for characteristic-seven Picard-curve 7-rank-zero classification."""
from itertools import product
P=7

def add_poly(P1,P2):
    r=P1.copy()
    for m,v in P2.items():
        r[m]=(r.get(m,0)+v)%P
        if r[m]==0: del r[m]
    return r

def mul_poly(P1,P2):
    r={}
    for m,u in P1.items():
        for n,v in P2.items():
            z=tuple(m[i]+n[i] for i in range(4))
            r[z]=(r.get(z,0)+u*v)%P
            if r[z]==0: del r[z]
    return r

# Exponents: x,a,b,c. f=x^4+a*x^2+b*x+c.
f={(4,0,0,0):1,(2,1,0,0):1,(1,0,1,0):1,(0,0,0,1):1}
power={(0,0,0,0):1}
coeff=[]
for k in range(1,5):
    power=mul_poly(power,f)
    if k in (2,4):
        coeff.append((k,power.copy()))

def take_x(poly,e):
    return {(a,b,c):w for (x,a,b,c),w in poly.items() if x==e}

expect={
 (2,6):{(1,0,0):2},
 (4,5):{(2,1,1):5,(1,3,0):4,(0,1,2):5},
 (4,6):{(3,0,1):4,(2,2,0):6,(1,0,2):5,(0,2,1):5},
 (4,12):{(2,0,0):6,(0,0,1):4},
 (4,13):{(0,1,0):4},
}
for k,p in coeff:
    for e in [6] if k==2 else [5,6,12,13]:
        assert take_x(p,e)==expect[(k,e)],(k,e,take_x(p,e),expect[(k,e)])
print('SYMBOLIC_COEFFICIENTS_OK')

# F_343 = F_7[u]/(u^3-2). The polynomial is irreducible
# because 2 is not a cube in F_7.
ZERO=(0,0,0); ONE=(1,0,0)
def field(x): return (x%7,0,0)
def plus(x,y):return tuple((x[i]+y[i])%7 for i in range(3))
def minus(x,y):return tuple((x[i]-y[i])%7 for i in range(3))
def prod(x,y):
    t=[0]*5
    for i in range(3):
        for j in range(3): t[i+j]=(t[i+j]+x[i]*y[j])%7
    for i in [4,3]:
        t[i-3]=(t[i-3]+2*t[i])%7
    return tuple(t[:3])
def exp(x,n):
    z=ONE
    while n:
        if n&1:z=prod(z,x)
        x=prod(x,x);n//=2
    return z
U=(0,1,0)
assert exp(U,3)==field(2)
assert all(pow(n,3,7)!=2 for n in range(7))

def mat_mul(m,n):
    return [[plus(prod(m[i][0],n[0][j]),prod(m[i][1],n[1][j])) for j in range(2)] for i in range(2)]

def H2(b,c):
    return [
      [prod(field(-2),prod(prod(b,b),c)),prod(field(-2),prod(b,prod(c,c)))],
      [prod(field(-3),b),prod(field(-3),c)]
    ]

def C2_zero(b,c):
    h=H2(b,c)
    twisted=[[exp(v,7) for v in row] for row in h]
    z=mat_mul(twisted,h)
    return z==[[ZERO,ZERO],[ZERO,ZERO]]

assert C2_zero(ONE,ZERO)
assert C2_zero(ONE,U)
# The witness with c^3=2 is smooth since Delta=4c^3-6=2.
assert minus(prod(field(4),exp(U,3)),field(6))==field(2)
assert not C2_zero(ONE,ONE)

zero_smooth=[]
zero_singular=[]
for c in product(range(7),repeat=3):
    delta=minus(prod(field(4),exp(c,3)),field(6))
    if C2_zero(ONE,c):
        (zero_smooth if delta!=ZERO else zero_singular).append(c)
assert len(zero_smooth)==4,(len(zero_smooth),zero_smooth)
assert len(zero_singular)==3,(len(zero_singular),zero_singular)
assert set(exp(c,3) for c in zero_smooth)=={ZERO,field(2)}
assert set(exp(c,3) for c in zero_singular)=={field(5)}
print('GF343_CENSUS_OK: smooth rank-zero models b=1:',len(zero_smooth),
      '; singular rank-zero models:',len(zero_singular))

# For b=0, c nonzero, the Cartier 2x2 block has nonzero stable rank.
for c in [ONE,U,exp(U,2)]:
    assert not C2_zero(ZERO,c)
print('TWO_COARSE_CLASSES_AND_A_NUMBER_TWO_OK')
