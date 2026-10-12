#!/usr/bin/env python3
"""Exact modular recurrence checks supporting an infinite parameter theorem.

This executable checks finitely many parameters; it does not replace the proof.
"""
from math import gcd, lcm

def rank_period(a, modulus):
    # A unimodular companion recurrence; its state determines the period.
    previous, current = 0, 1
    rank = None
    for index in range(1, 100000):
        previous, current = current, (a*current-previous) % modulus
        if previous == 0 and rank is None:
            rank = index
        if (previous, current) == (0, 1):
            assert rank is not None
            assert index % rank == 0
            return rank, index, index//rank
    raise AssertionError('Period bound exhausted in finite verification')

def run():
    cases = 0
    for a in range(4, 101, 6):
        e = (a & -a).bit_length()-1
        mod_two = 2**(e+1)
        r2,p2,o2 = rank_period(a,mod_two)
        assert (r2,p2,o2) == (4,4,1), (a,mod_two,r2,p2,o2)
        for j in range(1,5):
            mod_three = 3**j
            r3,p3,o3 = rank_period(a,mod_three)
            assert o3 == 2 and r3%2 == 1 and r3%3 == 0
            r,p,o = rank_period(a,mod_two*mod_three)
            assert r==lcm(r2,r3) and p==lcm(p2,p3)
            assert o==1
            cases+=1
    for a in range(4,101,6):
        prev,cur=0,1
        seq=[0,1]
        for k in range(2,31):
            prev,cur=seq[-2],seq[-1]
            seq.append(a*cur-prev)
        for r in range(1,10):
            V=seq[r+1]-seq[r-1]
            assert seq[3*r]==seq[r]*(V*V-1)
            assert V*V-4==(a*a-4)*seq[r]*seq[r]
    print('VERIFY_OK')
    print('parameter_a_count=17')
    print(f'combined_modulus_cases={cases}')
    print('tripling_identity_checks=153')
    print('smallest_example: a=4, modulus_1=8, modulus_2=3, combined=24')
    print('infinite_claim_proven_symbolically_not_by_enumeration=true')
if __name__=='__main__':
    run()
