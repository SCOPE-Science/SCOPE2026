"""Exact F_5 arithmetic for coefficient-normalized smooth Ciani quartics.

No nonstandard dependencies. Run: python3 verify_modular.py
The enumeration treats equations up to common nonzero scalar, not isomorphism.
"""
from itertools import product
from collections import Counter

P = 5
MONOMIALS = [(4,0,0),(0,4,0),(0,0,4),(2,2,0),(2,0,2),(0,2,2)]
POINTS = [(1,i,j) for i in range(P) for j in range(P)] + [(0,1,i) for i in range(P)] + [(0,0,1)]

def normalize(v):
    lam = pow(next(a for a in v if a%P),-1,P)
    return tuple(a*lam%P for a in v)

LINES = sorted({normalize(point) for point in POINTS})
assert len(LINES)==31

def line_basis(line):
    a,b,c=line
    if c:
        return (1,0,-a*pow(c,-1,P)%P),(0,1,-b*pow(c,-1,P)%P)
    if b:
        return (1,-a*pow(b,-1,P)%P,0),(0,0,1)
    return (0,1,0),(0,0,1)

def multiply(u,v):
    w={}
    for i,a in u.items():
        for j,b in v.items():w[i+j]=(w.get(i+j,0)+a*b)%P
    return {i:a for i,a in w.items() if a}

def restrict(monomial,line):
    u,v=line_basis(line)
    poly={0:1}
    for j,e in enumerate(monomial):
        for _ in range(e):poly=multiply(poly,{0:u[j],1:v[j]})
    return tuple(poly.get(j,0) for j in range(5))

LINE_ROWS = {line:tuple(restrict(exp,line) for exp in MONOMIALS) for line in LINES}

# Projective Veronese map from nonzero binary quadratics to square quartics.
SQUARE_TYPES={}
for a,b,c in POINTS:
    sq=normalize((a*a,2*a*b,b*b+2*a*c,2*b*c,c*c))
    disc=(b*b-4*a*c)%P
    SQUARE_TYPES[sq]=0 if disc==0 else (1 if disc in (1,4) else 2)
assert len(SQUARE_TYPES)==31

def smooth(coeff):
    a,b,c,d,e,f=coeff
    if a*b*c==0:return False
    if (d*d-4*a*b)%P==0 or (e*e-4*a*c)%P==0 or (f*f-4*b*c)%P==0:return False
    # The gradient's three equations in X^2,Y^2,Z^2.
    determinant=(2*a*(4*b*c-f*f)-d*(2*c*d-e*f)+e*(d*f-2*b*e))%P
    return determinant!=0

def signature(coeff):
    count=[0,0,0]
    for rows in LINE_ROWS.values():
        binary=tuple(sum(a*row[j] for a,row in zip(coeff,rows))%P for j in range(5))
        if any(binary):
            kind=SQUARE_TYPES.get(normalize(binary))
            if kind is not None:count[kind]+=1
    return tuple(count)

EXPECTED={
    (0,0,0):126,(0,0,2):120,(0,2,0):168,(2,0,0):72,
    (0,0,4):28,(0,2,2):48,(0,4,0):72,(2,0,2):24,
    (4,0,0):30,(2,0,4):36,(2,2,2):24,(2,4,0):12,
    (0,2,6):24,(8,0,0):9,(0,0,16):7
}
EXPECT_EXTREMIZERS={
    (1,1,1,0,0,0),(1,1,3,1,0,0),(1,1,3,4,0,0),
    (1,2,2,0,0,2),(1,2,2,0,0,3),
    (1,3,1,0,1,0),(1,3,1,0,4,0)
}

def main():
    strata=Counter()
    extrema=[]
    for coeff in product(range(P),repeat=6):
        if not any(coeff) or next(x for x in coeff if x)!=1:continue
        if not smooth(coeff):continue
        sig=signature(coeff)
        strata[sig]+=1
        if sum(sig)==16:extrema.append(coeff)
    assert sum(strata.values())==800
    assert strata==EXPECTED
    assert set(extrema)==EXPECT_EXTREMIZERS
    totals=Counter()
    for sig,n in strata.items():totals[sum(sig)]+=n
    assert totals=={0:126,2:360,4:202,6:72,8:33,16:7}
    print('SIGNATURES:',sorted(strata.items()))
    print('TOTAL_BITANGENTS:',sorted(totals.items()))
    print('SIXTEEN_BITANGENTS:',sorted(extrema))
    print('MODULAR_VERIFY_OK')

if __name__=='__main__':main()
