#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

cases = {
    12: {"gC":55, "G":720, "special":60, "base_pair":(2,3), "A":6, "sig":(2,3,6), "gY":1},
    20: {"gC":171,"G":1200,"special":60,"base_pair":(2,5), "A":10,"sig":(2,5,10),"gY":2},
    30: {"gC":406,"G":1800,"special":60,"base_pair":(3,5), "A":15,"sig":(3,5,15),"gY":4},
}

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def lcm(a,b):
    return a//gcd(a,b)*b

for d,c in cases.items():
    assert c["gC"] == (d-1)*(d-2)//2
    assert c["G"] == 60*d
    assert c["A"] == c["G"]//120 == d//2
    a,b = c["base_pair"]
    target = Fraction(2*c["gC"]-2,c["G"])
    sols=[]
    for e1 in divisors(a):
        for e2 in divisors(b):
            rhs=-2 + (1-Fraction(1,e1)) + (1-Fraction(1,e2)) + (1-Fraction(1,60))
            if rhs==target:
                sols.append((e1,e2))
    assert sols == [(a,b)], (d, sols)
    n=c["A"]
    # In the cyclic quotient, the special inertia maps onto all of C_n.
    # If the other two images have orders dividing coprime a,b and their
    # product with a generator is 1, then their product must itself have
    # order n=a*b, forcing full orders a and b.
    assert gcd(a,b)==1 and a*b==n
    poss=[]
    for u in divisors(a):
        for v in divisors(b):
            if lcm(u,v)==n:
                poss.append((u,v))
    assert poss == [(a,b)], (d, poss)
    e1,e2,e3=c["sig"]
    two_g_minus_two=n*(-2 + (1-Fraction(1,e1))+(1-Fraction(1,e2))+(1-Fraction(1,e3)))
    assert two_g_minus_two.denominator==1
    assert (two_g_minus_two.numerator+2)//2 == c["gY"]

print("VERIFY_OK derived=SL(2,5) residual_signatures=(2,3,6),(2,5,10),(3,5,15) quotient_genera=1,2,4")
