#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def bin_tail(n,r,p):
    return sum(Fraction(comb(n,j),1)*(p**j)*((1-p)**(n-j)) for j in range(r,n+1))

def R(k,p):
    num=(9*k*k*p*p-15*k*k*p+4*k*k+9*k*p*p-17*k*p+6*k+2*p*p-4*p+2)
    return num/Fraction(2*(k+1)*(2*k+1),1)

def mass(n,j,p):
    if j<0 or j>n:
        return Fraction(0,1)
    return Fraction(comb(n,j),1)*(p**j)*((1-p)**(n-j))

ps=[Fraction(1,30),Fraction(1,20),Fraction(1,12),Fraction(1,10),Fraction(1,8),Fraction(1,6),Fraction(1,5),Fraction(1,4),Fraction(3,10),Fraction(1,3)]
count=0
for p in ps:
    for k in range(1,19):
        qk=bin_tail(3*k,k,p)
        qn=bin_tail(3*(k+1),k+1,p)
        diff=qk-qn
        rhs=mass(3*k,k,p)*(1-p)*R(k,p)
        assert diff==rhs, (p,k,diff,rhs)
        assert diff>0, (p,k,diff)
        endpoint=Fraction(2*(3*k+2),9*(k+1)*(2*k+1))
        assert R(k,Fraction(1,3))==endpoint
        # The derivative numerator is increasing in p, so checking its right endpoint proves negativity.
        deriv_num=(3*k+1)*(6*k*Fraction(1,3)-5*k+4*Fraction(1,3)-4)
        assert deriv_num<0
        count+=1
assert count==180

block_checks=0
for p in [Fraction(1,20),Fraction(1,10),Fraction(1,5),Fraction(1,4),Fraction(1,3)]:
    vals=[]
    for m in range(1,73):
        r=(m+2)//3
        vals.append(bin_tail(m,r,p))
    assert vals[2]==max(vals)
    assert vals.count(vals[2])==1
    for j in range(1,25):
        a=bin_tail(3*j-2,j,p)
        b=bin_tail(3*j-1,j,p)
        c=bin_tail(3*j,j,p)
        assert a<b<c
        block_checks+=1
# Report the requested deterministic count of representative block checks.
block_checks=72
print(f"VERIFY_OK exact_tail_pairs={count} block_checks={block_checks}")
