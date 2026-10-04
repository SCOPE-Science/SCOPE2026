from fractions import Fraction
from math import comb, factorial
from itertools import product

def multinomial(counts):
    d=sum(counts)
    out=factorial(d)
    for c in counts:
        out//=factorial(c)
    return out

def B(r,Q):
    if r==0:
        return 1
    ans=0
    def rec(i,left,counts):
        nonlocal ans
        if i==Q-1:
            cc=counts+[left]
            m=multinomial(cc)
            ans += m*m
            return
        for a in range(left+1):
            rec(i+1,left-a,counts+[a])
    rec(0,r,[])
    return ans

def C_formula(d,q):
    ssum=Fraction(0)
    for s in range(2,d+1):
        term=Fraction(comb(d,s)**2 * B(d-s,q-2) * s*(s-1) * comb(2*s,s), 2*s-1)
        ssum += term
    return Fraction(q**(2-d),4) * ssum if d<=2 else Fraction(ssum, 4*q**(d-2))

def M_of_tuple(t,q):
    counts=[0]*q
    for a in t:
        counts[a]+=1
    return multinomial(counts)

def tangent_C_direct(d,q):
    p=Fraction(1,q)
    H00=Fraction(0)
    H01=Fraction(0)
    for t in product(range(q), repeat=d):
        counts=[0]*q
        for a in t:
            counts[a]+=1
        M=M_of_tuple(t,q)
        H00 += M * counts[0]*(counts[0]-1) * p**(d-2)
        H01 += M * counts[0]*counts[1] * p**(d-2)
    # Along h=t(e0-e1), F''=2(H00-H01)=-4C.
    return -(H00-H01)/2

cases=[(2,3),(2,5),(3,5),(3,7),(4,5),(4,7),(5,7)]
for d,q in cases:
    a=C_formula(d,q)
    b=tangent_C_direct(d,q)
    assert a==b, (d,q,a,b)
    assert a>0
print("VERIFY_OK cases=%d exact_rational_hessian_matches=1" % len(cases))
