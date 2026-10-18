#!/usr/bin/env python3
"""Exact transition-density calculation for Motzkin residues modulo eight.

Reproduce with: python3 verification.py
The infinite limit follows from the finite primitive-chain argument in RESULT.md;
the finite checks here verify the rational case table and modular formulas.
"""
from fractions import Fraction
from collections import defaultdict, deque

TABLE = (
 (0,0,0,0,0,0,0,0),
 (0,10,3,2,4,10,1,2),
 (0,3,0,1,8,3,0,1),
 (0,2,1,10,4,2,3,10),
 (0,4,8,4,0,4,8,4),
 (0,10,3,2,4,10,1,2),
 (0,1,0,3,8,1,0,3),
 (0,2,1,10,4,2,3,10),
)

def coefficient_from_digits(n, u=0, v=0):
    """Krattenthaler-Mueller theorem 11 evaluated with extra bit statistics u,v.

    u is added to the Hamming weight and v to the number of adjacent 11 pairs.
    For finite prefixes this represents the common high suffix of n and n+1.
    """
    s=n.bit_count()+u
    e=(n & (n>>1)).bit_count()+v
    r=n & 15
    b=(n>>4)&1
    if r in (0,8): return (2*s*s+4*e+1)%8
    if r in (1,9): return (6*s*s+4*e+3)%8
    if r==2: return (4*s+6)%8
    if r in (3,10): return 4
    if r in (4,12): return (6*s*s+4*e+3)%8
    if r in (5,13): return (2*s*s+4*e+5)%8
    if r==6: return (6*s*s+4*b*s+4*e+2*b+7)%8
    if r==7: return (2*s*s+4*b*s+4*e+2*b+5)%8
    if r==11: return (4*s+2)%8
    k=4
    while (n>>k)&1: k+=1
    q=(n>>(k+1))&1
    if r==14:
        if k%2==0:return ((q+1)*(4*s+6))%8
        return (2*q+4*q*s+2*s*s+4*s+4*e+7)%8
    if k%2==0:return (6*q+4*q*s+4)%8
    return (2*q+4*q*s+2*s*s+4*e+5)%8

def prefix(r,k,q):
    return r+sum(1<<j for j in range(4,k))+(q<<(k+1))

def calculate():
    result=defaultdict(Fraction)
    for r in range(13):
        for bit4 in (0,1):
            w=r+16*bit4
            for u in range(4):
                for v in range(2):
                    result[coefficient_from_digits(w,u,v),coefficient_from_digits(w+1,u,v)] += Fraction(1,32*8)
    for r in (13,14,15):
        for k in range(4,8):
            # Geometric tail k,k+4,... has probability 2^(-k-2)/(1-1/16).
            prob=Fraction(16,15*2**(k+2))
            for q in (0,1):
                w=prefix(r,k,q)
                for u in range(4):
                    for v in range(2):
                        result[coefficient_from_digits(w,u,v),coefficient_from_digits(w+1,u,v)] += prob/8
    return result

def check_markov_chain():
    states=[(u,v,last) for u in range(4) for v in range(2) for last in range(2)]
    def move(z,x):
        u,v,last=z
        return ((u+x)%4,(v+last*x)%2,x)
    # Each state has exactly 2 incoming transitions (counting labels), so uniform is stationary.
    for z in states:
        incoming=sum(move(w,x)==z for w in states for x in (0,1))
        assert incoming==2, (z,incoming)
    # Every state can reach every other: irreducible.
    for start in states:
        q=deque([start]); seen={start}
        while q:
            z=q.popleft()
            for x in (0,1):
                t=move(z,x)
                if t not in seen:seen.add(t);q.append(t)
        assert len(seen)==16
    assert move((0,0,0),0)==(0,0,0) # Aperiodicity.

def check_recurrence():
    M=[1,1]
    for n in range(2,4096):
        num=(2*n+1)*M[n-1]+3*(n-1)*M[n-2]
        assert num%(n+2)==0
        M.append(num//(n+2))
    assert all(coefficient_from_digits(n)==M[n]%8 for n in range(len(M)))

def main():
    check_markov_chain()
    # The local pair classifications are k->k+4 periodic, as used by the geometric sum.
    for r in (13,14,15):
        for k in range(4,16):
            for q in (0,1):
                w1,w2=prefix(r,k,q),prefix(r,k+4,q)
                for u in range(4):
                    for v in range(2):
                        assert (coefficient_from_digits(w1,u,v),coefficient_from_digits(w1+1,u,v)) == (coefficient_from_digits(w2,u,v),coefficient_from_digits(w2+1,u,v))
    D=calculate()
    assert sum(D.values())==1
    assert all(D[a,b]==Fraction(TABLE[a][b],192) for a in range(8) for b in range(8))
    assert sum(v>0 for v in D.values())==44
    assert [sum(D[a,b] for b in range(8)) for a in range(8)] == [Fraction(0),Fraction(1,6),Fraction(1,12),Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,12),Fraction(1,6)]
    assert [sum(D[a,b] for a in range(8)) for b in range(8)] == [Fraction(0),Fraction(1,6),Fraction(1,12),Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,12),Fraction(1,6)]
    check_recurrence()
    print('VERIFY_OK: 16-state chain, rational 8x8 density table, k-periodicity, 4096 coefficients')

if __name__ == '__main__':main()
