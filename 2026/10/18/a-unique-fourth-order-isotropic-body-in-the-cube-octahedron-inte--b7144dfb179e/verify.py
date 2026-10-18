#!/usr/bin/env python3
"""Exact reproducibility checker for fourth-order isotropy of clipped cubes.

Standard-library only; all certificate arithmetic uses fractions.Fraction.
The mathematical domain is K_c=[-1,1]^3 intersect {sum |x_i|<=c}.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
from decimal import Decimal, getcontext


def add(A,B):
    n=max(len(A),len(B)); return [ (A[i] if i<len(A) else F(0))+(B[i] if i<len(B) else F(0)) for i in range(n)]
def scale(A,s): return [s*t for t in A]
def mul(A,B):
    C=[F(0)]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): C[i+j]+=a*b
    return C
def power(A,n):
    C=[F(1)]
    for _ in range(n): C=mul(C,A)
    return C
def ev(P,x):
    v=F(0)
    for a in reversed(P): v=v*x+a
    return v

def integrated_monomial(exponents, clips):
    """Even monomial exponents only: eight octants times exact inclusion/exclusion.
    clips=0 for 0<c<=1, 1 for 1<=c<=2, 2 for 2<=c<=3,
    3 for c>=3. Geometric formula is restricted to its piece.
    """
    ans=[F(0)]
    for m in range(clips+1):
        for shifted in combinations(range(3),m):
            pieces=[list(range(e+1)) if i in shifted else [e] for i,e in enumerate(exponents)]
            for idx in product(*pieces):
                coefficient=F(8*(-1)**m)
                for i,e in enumerate(exponents):
                    if i in shifted: coefficient*=comb(e,idx[i])
                degree=sum(idx)+3
                coefficient*=F(factorial(idx[0])*factorial(idx[1])*factorial(idx[2]),factorial(degree))
                ans=add(ans,scale(power([-F(m),F(1)],degree),coefficient))
    return ans

def bernstein_transform(P,degree,a,b):
    """(1+z)^degree * P((a+b*z)/(1+z)); coefficient signs on z>0.
    On z>0, the argument runs over (a,b).
    """
    out=[F(0)]
    for k,p in enumerate(P):
        out=add(out,scale(mul(power([F(a),F(b)],k),power([F(1),F(1)],degree-k)),p))
    return out

def normalized(P):
    Q=P[:]
    while len(Q)>1 and Q[-1]==0:Q.pop()
    return Q


def run():
    M40=integrated_monomial((4,0,0),1)
    M22=integrated_monomial((2,2,0),1)
    P=normalized(add(M40,scale(M22,-3)))
    expected=[F(6,105),F(98,105),F(-294,105),F(210,105),F(70,105),F(-126,105),F(42,105),F(-4,105)]
    # Expectation above is expansion of -(2/105)*(2c^7-21c^6+63c^5-35c^4-105c^3+147c^2-49c-3).
    assert P==expected,(P,expected)
    assert ev(P,F(1))==F(2,105)
    assert ev(P,F(2))==-F(2,7)
    Q=bernstein_transform(P,7,1,2)
    assert Q==[F(2,105),F(4,15),F(8,5),F(4),F(4),F(4,5),-F(4,5),-F(2,7)],Q
    # Exactly one coefficient sign-change + endpoint signs => precisely one root in (1,2) by Descartes' rule.
    assert sum((Q[i]>0) != (Q[i+1]>0) for i in range(len(Q)-1))==1
    P23=normalized(add(integrated_monomial((4,0,0),2),scale(integrated_monomial((2,2,0),2),-3)))
    R=bernstein_transform(P23,7,2,3)
    assert R==[-F(2,7),-F(16,5),-F(68,5),-F(88,3),-F(104,3),-F(112,5),-F(112,15),-F(16,15)],R
    assert all(v<0 for v in R)
    # c<=1 scales a regular octahedron: moment defect 2*c^7/105>0.
    assert ev(P,F(1))==F(2,105)
    # c>=3 is a cube with defect -16/15.
    assert ev(P23,F(3))==-F(16,15)

    lo,hi=F(1699,1000),F(17,10)
    assert ev(P,lo)>0 and ev(P,hi)<0
    # Sixth-order isotropy requires M_600=5*M_420. Certify this fails at the unique fourth-order root.
    P6=normalized(add(integrated_monomial((6,0,0),1),scale(integrated_monomial((4,2,0),1),-5)))
    sixth=bernstein_transform(P6,9,lo,hi)
    assert all(v<0 for v in sixth),sixth
    print('SIXTH_DEFECT_BERNSTEIN_ALL_NEGATIVE',len(sixth))
    # Exact-sign bisection gives a rational isolating interval, not a floating-point proof.
    for j in range(90):
        mid=(lo+hi)/2
        if ev(P,mid)>0:lo=mid
        else:hi=mid
    getcontext().prec=35
    approx=(Decimal(lo.numerator)/Decimal(lo.denominator)+Decimal(hi.numerator)/Decimal(hi.denominator))/2
    print('C_STAR_APPROX',str(approx))
    print('ENDPOINT_DEFECTS',ev(P,F(1)),ev(P,F(2)),ev(P23,F(3)))
    print('FIRST_INTERVAL_SIGN_PATTERN',''.join('+' if x>0 else '-' for x in Q))
    print('SECOND_INTERVAL_SIGN_PATTERN',''.join('+' if x>0 else '-' for x in R))
    print('VERIFY_OK exact_moment_polynomials root_uniqueness fourth_isotropy sixth_anisotropy')

if __name__=='__main__':run()
