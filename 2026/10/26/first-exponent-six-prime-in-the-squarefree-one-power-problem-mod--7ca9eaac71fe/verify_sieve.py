#!/usr/bin/env python3
"""Independent whole-interval exact sieve for the first exponent-six prime.

Run with Python 3; no third-party dependencies.  Uses under 450 MB of main sieve arrays.
"""
from math import isqrt
from pathlib import Path
import csv

LIMIT = 189954151
SHIFTS = (1, 2, 4, 8)


def sieve():
    composite = bytearray(LIMIT + 1)
    composite[0] = composite[1] = 1
    small_primes = []
    for q in range(2, isqrt(LIMIT) + 1):
        if composite[q] == 0:
            small_primes.append(q)
            start = q*q
            composite[start:LIMIT+1:q] = b'\1' * ((LIMIT-start)//q+1)

    squareful = bytearray(LIMIT + 1)
    for q in small_primes:
        start = q*q
        squareful[start:LIMIT+1:start] = b'\1' * ((LIMIT-start)//start+1)
    return composite, squareful


def main():
    composite, squareful = sieve()
    failures_four = []
    failures_five = []
    candidates = 0
    for p in range(7, LIMIT + 1, 36):
        if composite[p]:
            continue
        candidates += 1
        if any(p >= s+1 and not squareful[p-s] for s in SHIFTS):
            continue
        failures_four.append(p)
        if p > 32 and squareful[p-32]:
            failures_five.append(p)
    assert candidates == 879429, candidates
    assert failures_four == [4851151,14627383,17026927,19883527,50671051,63716551,64734883,72319651,95075683,96041527,98555227,139820227,140570179,141618283,159658027,165167251,165964327,166059979,171086983,177257851,LIMIT]
    assert failures_five == [LIMIT], failures_five
    assert squareful[LIMIT - 64] == 0
    with Path(__file__).with_name('obstruction_certificate.csv').open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == len(failures_four)
    for row,p in zip(rows, failures_four):
        assert int(row['p']) == p
        for a,field in [(0,'q_for_p_minus_1'),(1,'q_for_p_minus_2'),(2,'q_for_p_minus_4'),(3,'q_for_p_minus_8'),(5,'q_for_p_minus_32')]:
            q=int(row[field]); value=p-(1<<a)
            if q: assert q>=2 and value%(q*q)==0
            else: assert a==5 and squareful[value]==0
    print('CERTIFICATE_OK', 'prime_candidates=', candidates,
          'four_failure_count=', len(failures_four),
          'five_failure_list=', failures_five,
          'first_exponent_six=', LIMIT)
    print('FOUR_FAILURES', ','.join(map(str, failures_four)))


if __name__ == '__main__':
    main()
