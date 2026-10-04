#!/usr/bin/env python3
"""Finite exact checks for Heisenberg coinvariants under the meridional action."""
from math import gcd
from collections import deque

def mul(x,y,k):
    # A^a B^b C^c, C=[A,B]; BA=AB C^{-1}
    a,b,c=x; d,e,f=y
    return ((a+d)%k,(b+e)%k,(c+f-d*b)%k)

def inv(x,k):
    a,b,c=x
    # solve x*y=1
    return ((-a)%k,(-b)%k,(-c-a*b)%k)

def phi(x,k):
    # phi(A)=B, phi(B)=A^-1 B, phi(C)=C
    # homomorphism evaluated by multiplication
    a,b,c=x
    A=(1,0,0); B=(0,1,0); C=(0,0,1)
    pA=B
    pB=((-1)%k,1,0)
    out=(0,0,0)
    for _ in range(a): out=mul(out,pA,k)
    for _ in range(b): out=mul(out,pB,k)
    for _ in range(c): out=mul(out,C,k)
    return out

def phipow(x,r,k):
    for _ in range(r%6):
        x=phi(x,k)
    return x

def normal_closure(k,r):
    A=(1,0,0); B=(0,1,0)
    gens=[]
    for x in (A,B):
        gens.append(mul(phipow(x,r,k),inv(x,k),k))
    # grow subgroup plus all conjugates by A,B
    S={(0,0,0)}
    changed=True
    ambient_gens=[A,B]
    while changed:
        changed=False
        current=list(S)
        pool=gens+current
        for g in list(pool):
            if g not in S:
                S.add(g); changed=True
            for h in ambient_gens:
                conj=mul(mul(h,g,k),inv(h,k),k)
                if conj not in S:
                    S.add(conj); changed=True
        current=list(S)
        for x in current:
            for y in current:
                z=mul(x,y,k)
                if z not in S:
                    S.add(z); changed=True
    return S

for k in (3,5,7,9,11,15):
    expected=[k**3,1,gcd(k,3),1,gcd(k,3),1]
    got=[]
    for r in range(6):
        N=normal_closure(k,r)
        qsize=k**3//len(N)
        got.append(qsize)
        assert qsize==expected[r], (k,r,qsize,expected[r])
        if r in (2,4) and gcd(k,3)==3:
            A=(1,0,0)
            # phi(A)=A^{-1} in quotient
            witness=mul(phi(A,k),A,k)
            assert witness in N
    assert got==expected

# Verify period six on generators for sample moduli.
for k in (3,5,7,9,11,15):
    for x in ((1,0,0),(0,1,0),(0,0,1)):
        assert phipow(x,6,k)==x

print("VERIFY_OK k=3,5,7,9,11,15 residues=0..5 quotient_sizes=[k^3,1,gcd(k,3),1,gcd(k,3),1] inversion_action=true")
