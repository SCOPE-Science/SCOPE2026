#!/usr/bin/env python3
"""Exact-rational checks of a one-step cellular-automaton extinction law.
Run using the Python 3 standard library only: python3 verify_one_step_extinction.py
"""
from fractions import Fraction
from math import comb


def theoretical(n, lam):
    t = lam * (1-lam)
    total = sum(Fraction(n*comb(n-2*j,2*j), n-2*j)*t**(2*j)
                for j in range(n//4+1))
    return total / 2**(n-1)


def raw_count(n, lam):
    # Direct enumeration of all initial bit strings and all
    # sitewise Bernoulli choices, with their probabilities; no graph formula.
    zero = Fraction(0)
    for x in range(1<<n):
        for mask in range(1<<n):
            y = 0
            for i in range(n):
                neighbor = (i+1)%n if (mask>>i)&1 else (i-1)%n
                y |= (((x>>i)^(x>>neighbor))&1) << i
            if y == 0:
                nplus = mask.bit_count()
                zero += lam**nplus*(1-lam)**(n-nplus)
    return zero / (1<<n)


def via_rank(n, lam):
    # Alternative finite check: each orientation defines a binary matrix;
    # count zero preimages from the rank, using bit-packed GF(2) elimination.
    total = Fraction(0)
    for mask in range(1<<n):
        rows = []
        for i in range(n):
            neighbor=(i+1)%n if (mask>>i)&1 else (i-1)%n
            rows.append((1<<i)^(1<<neighbor))
        rank = 0
        for bit in range(n):
            pivot = next((j for j in range(rank,n) if rows[j]>>bit & 1),None)
            if pivot is None: continue
            rows[rank],rows[pivot]=rows[pivot],rows[rank]
            for j in range(n):
                if j != rank and rows[j]>>bit & 1: rows[j] ^= rows[rank]
            rank += 1
        nplus = mask.bit_count()
        total += 2**(n-rank)*lam**nplus*(1-lam)**(n-nplus)
    return total / (1<<n)


def via_recurrence(n, lam):
    t = lam*(1-lam)
    s0,s1=Fraction(2),Fraction(1)
    for _ in range(n): s0,s1=s1,s1+t*s0
    u0,u1=Fraction(2),Fraction(1)
    for _ in range(n): u0,u1=u1,u1-t*u0
    return (s0+u0)/2**n


def main():
    tests=0
    for n in range(3,10):
        for lam in (Fraction(0),Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5),Fraction(1)):
            t=theoretical(n,lam)
            a=raw_count(n,lam)
            b=via_rank(n,lam)
            c=via_recurrence(n,lam)
            assert a==b==c==t,(n,lam,a,b,c,t)
            tests+=1
    for n in range(10,50):
        for lam in (Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(6,7),Fraction(1)):
            assert theoretical(n,lam)==via_recurrence(n,lam)
            tests+=1
    for n in range(4,50):
        vals=[theoretical(n,Fraction(j,64)) for j in range(33)]
        assert all(vals[j]<vals[j+1] for j in range(32)),n
        tests+=1
    assert theoretical(3,Fraction(17,23))==Fraction(1,4)
    assert theoretical(4,Fraction(1,2))==Fraction(9,64)
    print(f'PASS: {tests} parameter/size comparisons; direct full one-step bit enumeration for 3<=n<=9; GF(2) matrix rank separate checks; high-n recurrence and monotonicity checks.')

if __name__=='__main__':
    main()
