#!/usr/bin/env python3
"""Standalone reproducibility checks for alternating-host absent subsequences.
No external modules. Run: python3 verify.py
"""
from itertools import product

def is_subsequence(pattern, host):
    it = iter(host)
    return all(any(letter == target for letter in it) for target in pattern)

def minimal_absent(pattern, host):
    if is_subsequence(pattern, host):
        return False
    return all(is_subsequence(pattern[:i] + pattern[i+1:], host)
               for i in range(len(pattern)))

def predicted_minimal(pattern, k):
    if not pattern:
        return False
    equal = sum(a == b for a, b in zip(pattern, pattern[1:]))
    cost = len(pattern) + (pattern[0] == '1') + equal
    if cost <= 2*k:
        return False
    if len(pattern) == 1:
        return False
    runs = []
    for letter in pattern:
        if runs and runs[-1][0] == letter:
            runs[-1] = (letter, runs[-1][1]+1)
        else:
            runs.append((letter,1))
    if len(runs) > 1 and runs[0] == ('0',1):
        return False
    if any(length == 1 for _, length in runs[1:-1]):
        return False
    smallest_drop = 1 if len(runs) > 1 and runs[-1][1] == 1 else 2
    return cost - smallest_drop <= 2*k

def counts_by_cost(limit):
    # A: every deletion lowers greedy cost by two; B: one lowers it by one.
    # Coefficients of x^3(1+x+x^2)/(1-x^2-x^3) and
    # x^3(1+x)/(1-x^2-x^3), computed without symbolic algebra.
    aa = [0]*(limit+1)
    bb = [0]*(limit+1)
    for t in range(3,limit+1):
        aa[t] = (aa[t-2] if t >= 2 else 0) + (aa[t-3] if t >= 3 else 0) + (t in (3,4,5))
        bb[t] = (bb[t-2] if t >= 2 else 0) + (bb[t-3] if t >= 3 else 0) + (t in (3,4))
    return aa,bb

def expected_counts(limit_k):
    aa, bb = counts_by_cost(2*limit_k+2)
    vals = [0]
    for k in range(1,limit_k+1):
        vals.append(aa[2*k+1] + bb[2*k+1] + aa[2*k+2])
    return vals

def main():
    vals = expected_counts(100)
    assert vals[1:10] == [3,5,9,16,28,49,86,151,265]
    for k in range(4,101):
        assert vals[k] == 2*vals[k-1]-vals[k-2]+vals[k-3]
    count = 0
    for k in range(1,9):
        w = '01'*k
        got = 0
        short = 0
        for size in range(1,2*k+2):
            for bits in product('01', repeat=size):
                u = ''.join(bits)
                actual = minimal_absent(u,w)
                predicted = predicted_minimal(u,k)
                assert actual == predicted, (k,u,actual,predicted)
                if actual:
                    got += 1
                    if size == k+1:
                        short += 1
                count += 1
        assert got == vals[k], (k,got,vals[k])
        assert short == k+2, (k,short)
    print('VERIFY_OK', 'hosts=8', 'candidates=',count, 'formula_checks=100',
          'counts=',vals[1:10])

if __name__ == '__main__':
    main()
