"""Exact rational checks of constructive optimal Egyptian-fraction ties."""
from fractions import Fraction
from math import isqrt

def divs(n):
    result=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            result.append(d)
            if d*d!=n: result.append(n//d)
    return sorted(result)

def G(remainder):
    return remainder.denominator//remainder.numerator+1

def check(q, full=False):
    assert q>=3 and q%2
    a=(q+1)//2
    b=a*q
    c=(6*q*a*b)**2+1
    Q=q*c
    S=Fraction(2,q)+Fraction(1,c)
    eps=Fraction(1,72*Q*Q*a*a*b*b)
    theta=S+eps
    assert theta<1
    assert [a,b,c]==[G(theta),G(theta-Fraction(1,a)),G(theta-Fraction(1,a)-Fraction(1,b))]
    assert a*a-a+1<=b and b*b-b+1<=c
    assert c>(6*q*a*b)**2
    tuples=set()
    for d in divs(q*q):
        if d>q: continue
        assert (q+d)%2==0 and (q+q*q//d)%2==0
        u=(q+d)//2
        v=(q+q*q//d)//2
        assert 2<=u<=v<c
        assert Fraction(1,u)+Fraction(1,v)+Fraction(1,c)==S
        tuples.add((u,v,c))
    assert len(tuples)==(len(divs(q*q))+1)//2
    assert (a,b,c) in tuples
    assert len([x for x in tuples if x[0]<x[1]<x[2]])==(len(divs(q*q))-1)//2
    if full:
        equal=set()
        checked=0
        # Any potential competitor in (S,theta) must have x<3a,y<2b.
        for x in range(a,3*a):
            for y in range(x,2*b):
                H=Fraction(1,x)+Fraction(1,y)
                if H>=theta: continue
                eq=S-H
                if eq>0 and eq.numerator==1:
                    z_eq=eq.denominator
                    if z_eq>=y:equal.add((x,y,z_eq))
                upper=theta-H
                low=S-H
                if upper<=0: continue
                z_min=max(y,upper.denominator//upper.numerator+1)
                if low<=0:
                    # Large z would give a better underapproximation: cannot occur here.
                    raise AssertionError(('partial sum exceeds S',q,x,y,H-S))
                z_max=(low.denominator+low.numerator-1)//low.numerator-1
                assert z_max<z_min,(q,x,y,z_min,z_max)
                checked+=1
        assert equal==tuples,(q,equal^tuples)
        return (q,a,b,c,len(tuples),checked)
    return (q,a,b,c,len(tuples))

if __name__=='__main__':
    total=0
    for q in [3,5,7,9,11,15,21,35,105,1155]:
        full=q<=35
        row=check(q,full)
        print(row)
        if full: total+=row[-1]
    print('PASSED: 10 constructions, complete bounded-pair screen for q<=35,',total,'candidate pairs checked')
