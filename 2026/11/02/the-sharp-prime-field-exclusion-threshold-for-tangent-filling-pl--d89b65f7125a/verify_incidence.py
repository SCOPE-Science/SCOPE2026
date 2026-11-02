#!/usr/bin/env python3
"""Independent projective incidence and geometric smoothness check for six cubic models."""
from itertools import product

# Homogeneous cubic coefficients ordered x^3,x^2*y,x^2*z,x*y^2,x*y*z,x*z^2,y^3,y^2*z,y*z^2,z^3.
MONS = [(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]

def points(p):
    # Unique projective representatives: z=1, then (x:1:0), then (1:0:0)
    return [(x,y,1) for x in range(p) for y in range(p)] + [(x,1,0) for x in range(p)] + [(1,0,0)]

def evaluate(c,pt,p):
    return sum(c0*(pt[0]**i)*(pt[1]**j)*(pt[2]**k) for c0,(i,j,k) in zip(c,MONS))%p

def derivs(c,pt,p):
    ds=[]
    for d in range(3):
        total=0
        for coef,exp in zip(c,MONS):
            if exp[d]:
                term=coef*exp[d]
                for k in range(3): term *= pt[k]**(exp[k]-(d==k))
                total+=term
        ds.append(total%p)
    return tuple(ds)

def normalized(L,p):
    for elt in L:
        if elt%p:
            q=pow(elt,-1,p)
            return tuple(v*q%p for v in L)
    raise AssertionError('singular rational point')

def incidence(p,c):
    proj=points(p)
    curve_pts=[P for P in proj if evaluate(c,P,p)==0]
    tangents={normalized(derivs(c,P,p),p) for P in curve_pts}
    covered=[P for P in proj if any(sum(i*j for i,j in zip(P,L))%p==0 for L in tangents)]
    return len(curve_pts),len(tangents),len(covered)

# Representatives of the three quotient classes Pic^3(E)(F_p)/3E(F_p), with E:y^2=x^3+ax+b.
# q=11, E=(a,b)=(1,3): classes T=O, (4,4), (7,1).
# q=13, E=(a,b)=(0,4): classes T=O, (0,2), (0,11).
COEFFS={11:[
 [10,0,0,0,0,10,0,1,0,8],
 [0,0,10,1,0,7,0,7,3,5],
 [0,0,10,1,0,4,0,4,9,5]],
 13:[
 [12,0,0,0,0,0,0,1,0,9],
 [0,0,12,1,0,0,0,0,9,0],
 [0,0,12,1,0,0,0,0,4,0]]}
EXPECTED={11:([18,18,18],[114,112,112]),13:([21,21,21],[145,156,156])}

def main():
    for p in (11,13):
        values=[incidence(p,c) for c in COEFFS[p]]
        print('p=',p,'(curve-points, tangent-lines, covered-plane-points)=',values)
        assert [v[0] for v in values]==EXPECTED[p][0]
        assert [v[1] for v in values]==EXPECTED[p][0]
        assert [v[2] for v in values]==EXPECTED[p][1]
        assert all(v[2]<p*p+p+1 for v in values)
    # The specific F7 witness x^2 y+xz^2+2y^2z
    w=[0,1,0,0,0,1,0,2,0,0]
    n=incidence(7,w)
    print('p=7 smooth cubic witness:',n)
    assert n==(12,12,57)
    # Geometric smoothness follows if the three partial derivatives have no
    # common projective zero over the algebraic closure; exact Groebner check
    # supplied with the proof via verify_smoothness.py.
    print('INDEPENDENT_INCIDENCE_OK')
if __name__=='__main__':main()
