#!/usr/bin/env python3
"""Exact integer certificate for a lower bound on a divisor-sum comparison density."""
from fractions import Fraction
from math import prod
from decimal import Decimal, localcontext

PRIMES=(2,3,5,7,11,13,17,19,23,29,31)
CAPS=(12,8,5,4,2,2,2,2,2,2,2)

def entries(p, cap):
    out=[]
    for a in range(cap+1):
        if a==0:
            num=den=1
        else:
            num=1+p**a
            den=sum(p**d for d in range(1,a+1) if a%d==0)
        out.append((num,den,(p-1)*p**(cap-a)))
    return out

ROWS=[entries(p,e) for p,e in zip(PRIMES,CAPS)]

def certificate():
    accum=[0,0,0,0,0,0,0,0]
    def rec(i,num,den,weight):
        if i==len(ROWS):
            accum[0]+=weight
            accum[1]+=1
            if num>=den:
                accum[2]+=weight; accum[3]+=1
                if num==den:accum[4]+=weight;accum[5]+=1
                else: accum[6]+=weight;accum[7]+=1
            return
        for n,d,w in ROWS[i]:
            rec(i+1,num*n,den*d,weight*w)
    rec(0,1,1,1)
    all_mass,total,good,good_count,equal,eq_count,strict,strict_count=accum
    D=prod(p**(e+1) for p,e in zip(PRIMES,CAPS))
    assert total==7676370
    assert good_count==2837267
    assert eq_count==6
    assert strict_count==2837261
    assert D==36886693308870756519590386924324100736000000
    assert good==28604085934433764658299339805699268088627200
    assert all_mass==36812648176803947776832268851214472613068800
    assert good==equal+strict
    coefficient=Fraction(6*good,D)*prod(Fraction(p*p,p*p-1) for p in PRIMES)
    assert coefficient==Fraction(12117705984441349391635228560689,1593139205846841220399104000000)
    # Archimedes' rational bound pi < 22/7 makes a rigorous rational > 0.77 test.
    assert coefficient/Fraction(22,7)**2 > Fraction(77,100)
    print('VERIFY_OK patterns='+str(total)+' good='+str(good_count)+' equal='+str(eq_count))
    print('coefficient='+str(coefficient))
    print('certified_density_greater_than=0.77')

if __name__=='__main__':certificate()
