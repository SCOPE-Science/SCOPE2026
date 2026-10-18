#!/usr/bin/env python3
"""Exact finite verification for conditional concept stability formulas.

Requires Python standard library only. Does not assert an infinite-size proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def moment_formula(a, n, p, power):
    assert a >= 1 and n >= 1 and power in (1, 2)
    den = 1 - p**a
    if power == 1:
        return sum(Fraction(comb(a,t),2**a) * ((1-p**t)/den)**n
                   for t in range(a+1))
    return sum(
        ((1-p**s.bit_count()-p**t.bit_count()+p**(s|t).bit_count())/den)**n
        for s in range(1<<a) for t in range(1<<a)
    ) / (4**a)


def direct_moments(r, m, A, B, p):
    total = Fraction(0)
    moment1 = Fraction(0)
    moment2 = Fraction(0)
    for bits in range(1<<(r*m)):
        ones=bits.bit_count()
        weight=p**ones*(1-p)**(r*m-ones)
        rows=[{j for j in range(m) if bits & (1 << (i*m+j))} for i in range(r)]
        Ad=set(A); Bd=set(B)
        if {j for j in range(m) if all(j in rows[i] for i in Ad)} != Bd:
            continue
        if {i for i in range(r) if Bd<=rows[i]} != Ad:
            continue
        z=0
        AA=tuple(sorted(Ad))
        for zbits in range(1<<len(AA)):
            if {j for j in range(m) if all(j in rows[AA[k]]
                for k in range(len(AA)) if zbits & (1<<k))}==Bd:
                z+=1
        sigma=Fraction(z,1<<len(AA))
        total+=weight
        moment1+=weight*sigma
        moment2+=weight*sigma**2
    return total,moment1/total,moment2/total


def probability_formula(r,m,a,b,p):
    return p**(a*b)*(1-p**a)**(m-b)*(1-p**b)**(r-a)


def run():
    checks=0
    for p in [Fraction(1,3),Fraction(1,2),Fraction(2,3)]:
        for r,m in product(range(1,4),repeat=2):
            for abit in range(1,1<<r):
                A={i for i in range(r) if abit & (1<<i)}
                for bbit in range(1,1<<m):
                    B={j for j in range(m) if bbit & (1<<j)}
                    if len(B)==m: continue  # n>0 in the theorem
                    pr,avg,avg2=direct_moments(r,m,A,B,p)
                    a=len(A);n=m-len(B)
                    assert pr==probability_formula(r,m,a,len(B),p), (r,m,A,B,p,'prob')
                    assert avg==moment_formula(a,n,p,1),(r,m,A,B,p,'mean')
                    assert avg2==moment_formula(a,n,p,2),(r,m,A,B,p,'second')
                    checks+=1
    assert checks>250
    print('VERIFY_OK',checks,'exact full-matrix conditional checks')

if __name__=='__main__':run()
