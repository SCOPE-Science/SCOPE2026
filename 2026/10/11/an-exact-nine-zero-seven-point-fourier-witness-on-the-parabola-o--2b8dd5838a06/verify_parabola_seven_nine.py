#!/usr/bin/env python3
"""Exact eleven-element cyclotomic verification of an explicit seven-atom Fourier sum.

All operations are performed in the integral basis 1,z,...,z^9, with
z^10=-sum(z^0,...,z^9). No nonstandard dependencies are required.
"""
P=11
SUPPORT=(0,1,2,3,4,5,7)
COEFFICIENTS=(
 (14,6,9,12,4,7,10,2,16,8),
 (4,-3,1,5,-2,2,6,-1,3,-4),
 (-4,3,-1,-5,2,-2,5,1,-3,4),
 (9,18,5,3,12,10,8,6,15,13),
 (6,1,7,2,-3,3,9,4,-1,5),
 (-12,-2,-3,-4,-5,-6,4,-8,-9,1),
 (-6,-12,-7,-2,-8,-3,-9,-4,-10,-5),
)
EXPECTED=((0,4),(1,0),(1,1),(1,9),(6,6),(6,7),(6,9),(7,3),(9,9))
ZERO=(0,)*10

def add(u,v):
    return tuple(a+b for a,b in zip(u,v))

def multiply(u,v):
    accumulator=[0]*11
    for i,a in enumerate(u):
        if not a: continue
        for j,b in enumerate(v):
            if b: accumulator[(i+j)%11]+=a*b
    return tuple(accumulator[i]-accumulator[10] for i in range(10))

def zeta_power(k):
    k %= P
    return (-1,)*10 if k==10 else tuple(int(i==k) for i in range(10))

def main():
    assert len(SUPPORT)==len(COEFFICIENTS)==7
    assert len(set(SUPPORT))==7
    assert all(len(c)==10 and c!=ZERO for c in COEFFICIENTS)
    observed=[]
    for a in range(P):
        for b in range(P):
            value=ZERO
            for x,c in zip(SUPPORT,COEFFICIENTS):
                value=add(value,multiply(c,zeta_power(a*x*x+b*x)))
            if value==ZERO: observed.append((a,b))
    assert tuple(observed)==EXPECTED, (observed,EXPECTED)
    print('PASS: seven nonzero coefficients, all 121 Fourier values, exactly nine zeros.')
    print('Zeros:',observed)

if __name__=='__main__': main()
