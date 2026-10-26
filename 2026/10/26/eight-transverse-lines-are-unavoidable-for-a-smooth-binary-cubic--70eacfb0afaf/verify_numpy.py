#!/usr/bin/env python3
"""Independent vectorized exhaustive check for the finite binary-cubic census."""
from pathlib import Path
import numpy as np

def xor_toggle(s, x):
    if x in s: s.remove(x)
    else: s.add(x)

def monomial_restriction(a, b, e):
    # Expand product (a_i*s+b_i*t)^e_i with coefficient xor over GF(2).
    degrees = {0}
    for j, count in enumerate(e):
        for _ in range(count):
            nxt = set()
            for d in degrees:
                if a & (1 << j): xor_toggle(nxt, d+1)
                if b & (1 << j): xor_toggle(nxt, d)
            degrees = nxt
    return sum(1 << d for d in degrees)

def remainder(a,b):
    while b:
        m=a.bit_length()-b.bit_length()
        if m>=0:a ^= b<<m
        else:a,b=b,a
        if m>=0 and not a:return 0
        if m>=0 and a.bit_length()<b.bit_length():a,b=b,a
    return a

def squarefree_binary_cubic(mask):
    # f(s,1) has bit k for s^k; root at infinity occurs 3-deg(f) times.
    if mask==0:return False
    d=mask.bit_length()-1
    if 3-d>1:return False
    der=sum(((mask>>k)&1) << (k-1) for k in range(1,4,2))
    # Euclidean gcd over F2[s]
    a,b=mask,der
    while b:
        while a and a.bit_length()>=b.bit_length():
            a ^= b << (a.bit_length()-b.bit_length())
        a,b=b,a
    return a==1

def main():
    E=[(a,b,c,3-a-b-c) for a in range(4)
       for b in range(4-a) for c in range(4-a-b)]
    assert len(E)==20
    lines=[(a,b) for a in range(1,16) for b in range(a+1,16) if b<(a^b)]
    assert len(lines)==35
    good=np.array([squarefree_binary_cubic(m) for m in range(16)],dtype=np.uint8)
    assert set(np.flatnonzero(good))=={6,7,9,11,13,14}
    F=np.arange(1<<20,dtype=np.uint32)
    Bits=((F[:,None]>>np.arange(20,dtype=np.uint32)) & 1).astype(np.uint8)
    T=np.zeros(F.shape,dtype=np.uint8)
    for a,b in lines:
        R=np.zeros(F.shape,dtype=np.uint8)
        for j,e in enumerate(E):
            r=monomial_restriction(a,b,e)
            if r:R ^= Bits[:,j]*r
        T+=good[R]
    # Only T<=8 forms can challenge the claimed lower bound or attain equality.
    candidate=np.flatnonzero(T<=8)
    B=Bits[candidate]
    bad=np.zeros(len(candidate),dtype=bool)
    for p in range(1,16):
        A=[j for j,e in enumerate(E) if all(not e[i] or (p>>i)&1 for i in range(4))]
        value=np.bitwise_xor.reduce(B[:,A],axis=1)
        grad=[]
        for k in range(4):
            D=[j for j,e in enumerate(E) if e[k]%2
               and all((e[i]-(i==k)==0) or ((p>>i)&1) for i in range(4))]
            grad.append(np.bitwise_xor.reduce(B[:,D],axis=1))
        bad |= (value==0) & np.logical_and.reduce([q==0 for q in grad])
    accepted=candidate[~bad]
    assert len(accepted)==840 and set(T[accepted])=={8}
    cert={int(s) for s in Path("extremal_coefficients.txt").read_text().splitlines()}
    assert len(cert)==840 and cert==set(map(int,accepted))
    assert 0 not in cert
    print("forms checked", (1<<20)-1)
    print("lines checked",len(lines))
    print("squarefree restriction masks",list(np.flatnonzero(good)))
    print("min nonsingular-rational transverse lines",min(T[accepted]))
    print("extremal forms",len(cert))
    print("certificate equality",True)

if __name__=="__main__":main()
