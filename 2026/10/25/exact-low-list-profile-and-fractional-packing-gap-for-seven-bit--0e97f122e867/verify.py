#!/usr/bin/env python3
"""Exact-arithmetic verification of short binary two-deletion list-code certificates."""
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

P = Path(__file__).with_name('seven_list_certificates.json')
instances=json.loads(P.read_text(encoding='utf-8'))['instances']
assert [r['L'] for r in instances] == list(range(1,7))

# Rows are the 32 received words of length five, columns the 128 sent words of length seven.
A=[[0]*128 for _ in range(32)]
for x in range(128):
    for keep in combinations(range(7),5):
        y=0
        for j in keep:
            y=(y<<1)|((x>>(6-j))&1)
        A[y][x]=1

expected=[5,11,16,21,26,32]
for rec, claimed in zip(instances, expected):
    L=rec['L']
    witness=[int(s,2) for s in rec['code']]
    assert all(len(s)==7 and set(s)<={'0','1'} for s in rec['code'])
    assert len(set(witness))==len(witness)==claimed
    assert all(sum(A[y][x] for x in witness)<=L for y in range(32))
    d=rec['denominator']
    assert isinstance(d,int) and d>=1
    lam=rec['lambda_numerators']; mu=rec['mu_numerators']
    assert len(lam)==32 and len(mu)==128
    assert all(type(z) is int and z>=0 for z in lam+mu)
    # For every sent word x: sum_{y subseq x} lambda_y + mu_x >= 1.
    assert all(sum(lam[y]*A[y][x] for y in range(32))+mu[x]>=d for x in range(128))
    numerator=L*sum(lam)+sum(mu)
    U=Fraction(numerator,d)
    assert U==Fraction(*rec['rational_upper'])
    assert claimed<=U<claimed+1
    if L==2:
        pd=rec['primal_denominator']; pn=rec['primal_numerators']
        assert len(pn)==128 and all(type(z) is int and 0<=z<=pd for z in pn)
        assert all(sum(A[y][x]*pn[x] for x in range(128))<=2*pd for y in range(32))
        assert Fraction(sum(pn),pd)==U==Fraction(666,59)
    print(f'L={L}: optimal integer size {claimed}; rational dual upper {U}; PASS')
print('VERIFY_OK')
