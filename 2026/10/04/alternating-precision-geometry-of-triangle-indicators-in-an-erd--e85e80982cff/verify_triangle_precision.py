#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def classes(n):
    return [frozenset(x) for x in combinations(range(n),3)]

def dist(S,T):
    return 3-len(S & T)

def neighbors(S, verts):
    return [T for T in verts if T != S and len(S & T)==2]

def params(n,p):
    r=p*p/(1+p+p*p)
    Delta=(1-3*r)*(1+(n-7)*r)*(1+(2*n-9)*r)*(1+3*(n-3)*r)
    Q=1+(5*n-26)*r+3*(2*n-9)*(n-7)*r*r
    B=Delta+3*(n-3)*r*r*Q
    b0=B/Delta
    b1=-r*Q/Delta
    b2=4*r*r*(1+3*(n-6)*r)/Delta
    b3=-36*r*r*r/Delta
    return r,Delta,Q,B,(b0,b1,b2,b3)

def run():
    neighbor_class_checks=0
    inverse_equation_checks=0
    sign_checks=0
    partial_formula_checks=0
    full_product_checks=0

    for n in range(6,16):
        verts=classes(n)
        S=verts[0]
        nbr=neighbors(S,verts)
        for e in range(4):
            T=next(T for T in verts if dist(S,T)==e)
            counts=[0,0,0,0]
            for Z in nbr:
                counts[dist(Z,T)]+=1
            expected=[
                [0,3*(n-3),0,0],
                [1,n-2,2*(n-4),0],
                [0,4,2*(n-4),n-5],
                [0,0,9,3*(n-6)]
            ][e]
            assert counts==expected
            neighbor_class_checks+=4

    probs=[Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)]
    for n in range(6,101):
        for p in probs:
            r,Delta,Q,B,b=params(n,p)
            b0,b1,b2,b3=b
            assert 0<r<Fraction(1,3)
            assert Delta>0 and Q>0 and B>0
            assert b0>0 and b1<0 and b2>0 and b3<0
            sign_checks+=8

            assert b0+3*(n-3)*r*b1==1
            assert r*b0+(1+(n-2)*r)*b1+2*(n-4)*r*b2==0
            assert 4*r*b1+(1+2*(n-4)*r)*b2+(n-5)*r*b3==0
            assert 9*r*b2+(1+3*(n-6)*r)*b3==0
            inverse_equation_checks+=4

            rho1=-b1/b0
            rho2=-b2/b0
            rho3=-b3/b0
            assert rho1==r*Q/B and rho1>0
            assert rho2==-4*r*r*(1+3*(n-6)*r)/B and rho2<0
            assert rho3==36*r*r*r/B and rho3>0
            partial_formula_checks+=6

    # Full exact matrix products for representative sizes/probabilities.
    for n in [6,7,8,9]:
        verts=classes(n)
        nbrs={S:neighbors(S,verts) for S in verts}
        for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
            r,Delta,Q,B,b=params(n,p)
            for S in verts:
                for T in verts:
                    value=b[dist(S,T)]
                    value += r*sum(b[dist(Z,T)] for Z in nbrs[S])
                    assert value==(1 if S==T else 0)
                    full_product_checks+=1

    print(
        "VERIFY_OK "
        f"neighbor_class_checks={neighbor_class_checks} "
        f"inverse_equation_checks={inverse_equation_checks} "
        f"sign_checks={sign_checks} "
        f"partial_formula_checks={partial_formula_checks} "
        f"full_product_checks={full_product_checks}"
    )

if __name__=="__main__":
    run()
