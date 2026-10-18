#!/usr/bin/env python3
"""Exact recurrence and finite-window checks for three square-window gcd identities."""
from math import gcd

LIMIT=240
B=[0,1]
C=[1,3]
for n in range(2,2*LIMIT+10):
    B.append(6*B[-1]-B[-2]); C.append(6*C[-1]-C[-2])
# Direct independent Pell companion recurrence for the odd-indexed sequence.
Q=[1,1]
for n in range(2,4*LIMIT+20): Q.append(2*Q[-1]+Q[-2])
c=[0]+[Q[2*j-1] for j in range(1,2*LIMIT+9)]
checks=0
for k in range(1,LIMIT+1):
    h=gcd(k,B[k]); goalB=h//2 if k%2==0 else h
    goalC=h; goalc=h*(3 if k%6==3 else 1)
    for name,seq,expected in [('balancing',B,goalB),('Lucas-balancing',C,goalC),('Lucas-cobalancing',c,goalc)]:
        vals=[sum(seq[n+j]**2 for j in range(1,k+1)) for n in range(3)]
        got=gcd(*vals)
        assert got==expected,(name,k,got,expected)
        # Additional independent finite windows, no use of the symbolic formula.
        for n in range(3,11):
            assert sum(seq[n+j]**2 for j in range(1,k+1))%got==0
            checks+=1
    if k<=100:
        for j in range(3):
            assert sum(B[n]**2 for n in range(j+1,j+k+1))*16==B[k]*C[2*j+k+1]-k
            assert sum(C[n]**2 for n in range(j+1,j+k+1))*2==B[k]*C[2*j+k+1]+k
            assert sum(c[n]**2 for n in range(j+1,j+k+1))*2==B[k]*C[2*j+k]-k
            checks+=3
    if k%2==0:
        a=(k&-k).bit_length()-1
        assert (B[k]-3*k)%(2**(a+4))==0
        assert (B[k]*C[k+1]-k)%(2**(a+3))==0
        assert (B[k]*C[k+1]-k)%(2**(a+4))!=0
    else:
        assert (B[k]-k)%16==0
        assert (B[k]*C[k]-k)%4==2
    checks+=4
print('PASS',LIMIT,'window lengths;',checks,'exact checks; all three formulas')
