#!/usr/bin/env python3
"""Exact finite checks for midpoint representability and joint unit-residue laws."""
from math import gcd

def phi(a):
    return sum(gcd(a,r)==1 for r in range(1,a))

def decision(u,v):
    if u <= 1 or v <= 0 or gcd(u,v) != 1:
        raise ValueError('requires u>1, v>=1, and coprimality')
    inv = pow(v, -1, u)
    return inv % 2

def direct_decision(a,b):
    n = (a-1)*(b-1)//2
    return int(any((n-a*x) >= 0 and (n-a*x)%b == 0 for x in range(n//a+1)))

pairs_checked=0
for a in range(3,34,2):
    for b in range(2,110):
        if gcd(a,b)==1:
            assert decision(a,b)==direct_decision(a,b), (a,b)
            pairs_checked+=1

power_pairs_checked=0
for a in (3,5,7,9):
    for b in range(2,29):
        if gcd(a,b)==1:
            assert decision(a*a,b*b)==direct_decision(a*a,b*b), (a,b)
            power_pairs_checked+=1

squares_checked=0
joint_sample={}
for a in range(3,62,2):
    counts=[[0,0],[0,0]]
    for b in range(1,a*a):
        if gcd(a,b)==1:
            x=decision(a,b)
            y=decision(a*a,b*b)
            counts[x][y]+=1
    assert counts[0] == counts[1], (a,counts)
    s=sum((r*r%a)%2 for r in range(1,a) if gcd(r,a)==1)
    q=(a-1)*phi(a)//2+s
    assert counts[0][1]+counts[1][1]==q, (a,counts,q)
    assert sum(map(sum,counts))==a*phi(a)
    if a in (3,5,7,9,11,13,15,25,35):joint_sample[a]=counts
    squares_checked+=1

high_powers_checked=[]
for a,k in [(3,2),(3,4),(3,6),(5,2),(5,4),(7,4),(9,4),(11,4)]:
    mod=a**k
    counts=[[0,0],[0,0]]
    for b in range(1,mod):
        if gcd(a,b)==1:
            counts[decision(a,b)][decision(mod,pow(b,k))]+=1
    assert counts[0]==counts[1],(a,k,counts)
    high_powers_checked.append((a,k,counts[0]))

print('VERIFY_OK')
print('direct_diophantine_and_inverse_parity_pairs:',pairs_checked)
print('direct_squared_diophantine_pairs:',power_pairs_checked)
print('complete_square_moduli_a:',squares_checked,'range=3..61 odd')
print('square_joint_examples:',joint_sample)
print('even_exponent_joint_samples:',high_powers_checked)
for a, powers in [(3,(2,4,6)), (5,(2,4)), (7,(2,4))]:
    modulus=a**max(powers)
    profiles={}
    for b in range(1,modulus):
        if gcd(a,b)>1:continue
        vector=tuple(decision(a**k,b**k) for k in powers)
        key=(decision(a,b),vector)
        profiles[key]=profiles.get(key,0)+1
    for vector in {key[1] for key in profiles}:
        assert profiles.get((0,vector),0)==profiles.get((1,vector),0),(a,vector)
print('full_even_power_vector_independence: a=3 k=2,4,6; a=5,7 k=2,4')
print('Infinite proof is separate; these checks are finite only.')
