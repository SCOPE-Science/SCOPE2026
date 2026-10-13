#!/usr/bin/env python3
"""Exact integer and modular witnesses for the two-digit binomial valuation theorem.
No network access or external packages are needed.
"""
from math import comb
from pathlib import Path
import csv


def primes_to(n):
    return [p for p in range(3, n+1, 2) if all(p%d for d in range(3, int(p**0.5)+1, 2))]


def v_p(n,p):
    assert n != 0
    v=0
    while n%p == 0:
        n//=p
        v+=1
    return v


def modular_comb(N, K, p, e):
    modulus=p**e
    v=0
    unit=1
    for i in range(1,K+1):
        a=N-i+1
        b=i
        while a%p==0:
            a//=p
            v+=1
        while b%p==0:
            b//=p
            v-=1
        unit=unit*(a%modulus)%modulus
        unit=unit*pow(b,-1,modulus)%modulus
    assert v>=0
    return (unit*p**v)%modulus


def exact_value(p,t):
    B=(p-1)//2
    H=(p*p-1)//2
    A=(p**t-1)//2
    return 1-comb(A,B)+comb(A,p*B)-comb(A,H)


def modular_value(p,t):
    B=(p-1)//2
    H=(p*p-1)//2
    A=(p**t-1)//2
    e=4
    mod=p**e
    return (1-modular_comb(A,B,p,e)+modular_comb(A,p*B,p,e)-modular_comb(A,H,p,e))%mod


def run():
    source=Path(__file__).resolve().parent/'CERTIFICATE.tsv'
    with source.open(encoding='utf-8',newline='') as fd:
        table=list(csv.DictReader(fd,delimiter='\t'))
    expected_primes=primes_to(71)
    assert len(table)==len(expected_primes)==19
    for row,p in zip(table,expected_primes):
        assert int(row['prime'])==p
        expect_v=3 if p in (7,71) else 2
        for t in (3,4,5):
            f=exact_value(p,t)
            assert f != 0
            assert v_p(f,p)==expect_v, (p,t,'valuation')
            q=(f//p**2)%p
            assert int(row[f'quotient_t{t}_mod_p'])==q, (p,t,'quotient')
            assert modular_value(p,t)==f%(p**4), (p,t,'independent modular check')
            if p in (7,71):
                expect_unit=1 if p==7 else 5
                assert int(row[f'exception_unit_t{t}_mod_p'])==expect_unit
                assert (f//p**3)%p==expect_unit
            else:
                assert row[f'exception_unit_t{t}_mod_p']=='-'
        assert int(row['valuation'])==expect_v
    print('PASS: 19 odd primes through 71; 57 exact signed sums; 57 independent modular evaluations; all valuation and exceptional-unit witnesses agree')

if __name__=='__main__':
    run()
