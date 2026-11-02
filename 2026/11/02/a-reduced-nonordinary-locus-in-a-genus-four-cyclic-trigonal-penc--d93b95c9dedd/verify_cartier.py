#!/usr/bin/env python3
"""Direct monomial-power extraction for Cartier matrices over prime fields.

No special central polynomial identities are used in constructing the matrix.
"""
from math import comb

PRIMES=(7,13,19,31,37,43)
BASIS=((1,0),(2,0),(2,1),(2,2)) # differential x^i dx / y^j, j=1 or 2


def poly_power(e,p):
    # Multinomial expansion of (x^6+a*x^3+1)^e.
    out={}
    for k in range(e+1):
        for ell in range(e-k+1):
            xexp=6*k+3*ell
            aexp=ell
            val=comb(e,k)*comb(e-k,ell)%p
            out[(xexp,aexp)]=val
    return out


def eval_coeff(pol,xexp,a,p):
    return sum(v*pow(a,j,p) for (i,j),v in pol.items() if i==xexp)%p


for p in PRIMES:
    r=(p-1)//3
    f1=poly_power(r,p); f2=poly_power(2*r,p)
    # Coefficient index p*(s+1)-1-i (output x^s from input x^i).
    for a in range(p):
        if (a*a-4)%p==0:continue
        M=[[0]*4 for _ in range(4)]
        for col,(j,i) in enumerate(BASIS):
            expo = r*j
            pol = f1 if j==1 else f2
            for row,(jo,s) in enumerate(BASIS):
                if j!=jo:continue
                M[row][col]=eval_coeff(pol,p*(s+1)-1-i,a,p)
        assert all(M[i][j]==0 for i in range(4) for j in range(4) if i!=j)
        H=eval_coeff(f1,p-1,a,p)
        predicted_rank=2 if H==0 else 4
        assert sum(v!=0 for v in (M[i][i] for i in range(4))) == predicted_rank
        # Frobenius twists do not change which diagonal entries are zero.
    print(f'p={p}: all {p-2} smooth prime-field coefficients checked')
print('CARTIER_EXTRACTION_OK')
