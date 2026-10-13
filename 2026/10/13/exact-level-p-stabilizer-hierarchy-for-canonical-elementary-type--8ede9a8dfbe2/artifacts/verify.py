#!/usr/bin/env python3
from itertools import product


def invmod(a,p):
    return pow(a % p, -1, p)

def carry(x,y,p):
    x%=p; y%=p
    return 1 if x+y>=p else 0

def star_phase(q1,q2,q3,p,s12=1,s13=-1,s23=1):
    # Generic orientation signs; exact signs do not affect the decisive q1=0 slice.
    return (s12*carry(q1,(q2-q1)%p,p)
            +s13*carry(q1,(q3-q1)%p,p)
            +s23*carry(q2,(q3-q2)%p,p)) % p

def reduced_degree_2var(p, func):
    # Interpolate the unique reduced polynomial sum_{0<=a,b<p} c_ab x^a y^b over F_p.
    V=[[pow(x,a,p) for a in range(p)] for x in range(p)]
    A=[row[:] + [1 if i==j else 0 for j in range(p)] for i,row in enumerate(V)]
    for c in range(p):
        r=next(r for r in range(c,p) if A[r][c]%p)
        A[c],A[r]=A[r],A[c]
        z=invmod(A[c][c],p)
        A[c]=[(u*z)%p for u in A[c]]
        for r in range(p):
            if r==c: continue
            z=A[r][c]%p
            if z:
                A[r]=[(A[r][j]-z*A[c][j])%p for j in range(2*p)]
    W=[row[p:] for row in A]
    vals=[[func(x,y)%p for y in range(p)] for x in range(p)]
    tmp=[[sum(W[a][x]*vals[x][y] for x in range(p))%p for y in range(p)] for a in range(p)]
    coeff=[[sum(W[b][y]*tmp[a][y] for y in range(p))%p for b in range(p)] for a in range(p)]
    deg=max(a+b for a in range(p) for b in range(p) if coeff[a][b]%p)
    return deg, coeff

def main():
    for p in (3,5,7,11):
        # For every possible orientation sign pattern, q1=0 leaves only the (0,2,3) face.
        for s12,s13,s23 in product((-1,1), repeat=3):
            for q2,q3 in product(range(p), repeat=2):
                lhs=star_phase(0,q2,q3,p,s12,s13,s23)
                rhs=(s23*carry(q2,(q3-q2)%p,p))%p
                assert lhs==rhs
        # The decisive carry slice has reduced polynomial degree exactly p.
        deg,_=reduced_degree_2var(p, lambda x,y: carry(x,(y-x)%p,p))
        assert deg==p, (p,deg)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
