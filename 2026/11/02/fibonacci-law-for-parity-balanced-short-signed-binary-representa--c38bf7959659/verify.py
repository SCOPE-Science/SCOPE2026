#!/usr/bin/env python3
"""Reproducible checks for negative-digit parity of short binary signed-digit expansions.
Run: python3 verify.py. Uses only the Python standard library.
"""
from itertools import product
from collections import defaultdict
import re

MAX_DIRECT = 1024
MAX_R = 17

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# Independent literal enumeration: a positive short expansion starts with 1,
# and the next digit (if present) is 0 or 1, all others lie in {-1,0,1}.
counts = defaultdict(lambda: [0, 0])
counts[1][0] = 1
literal_representations = 1
for length in range(2, 12):
    for second in (0, 1):
        for suffix in product((-1, 0, 1), repeat=length-2):
            digits = (1, second) + suffix
            value = sum(digit * (1 << (length - j - 1)) for j, digit in enumerate(digits))
            if 1 <= value <= MAX_DIRECT:
                counts[value][sum(digit == -1 for digit in digits) % 2] += 1
                literal_representations += 1

N = 1 << MAX_R
weight = [0] * N
stern = [0] * N
weight[1] = stern[1] = 1
for n in range(2, N):
    if n % 2 == 0:
        weight[n] = weight[n//2]
        stern[n] = stern[n//2]
    else:
        weight[n] = weight[n//2] - weight[n//2 + 1]
        stern[n] = stern[n//2] + stern[n//2 + 1]

for n in range(1, MAX_DIRECT + 1):
    even, odd = counts[n]
    assert even - odd == weight[n], (n, even, odd, weight[n])
    assert even + odd == stern[n], (n, even, odd, stern[n])

# Verify the recognized regular language and exact Fibonacci shell counts.
pat = re.compile(r'1(?:01*0)*10*')
for n in range(1, N):
    matches = pat.fullmatch(bin(n)[2:]) is not None
    assert (weight[n] == 0) == matches, (n, weight[n], matches)

for r in range(1, MAX_R+1):
    exact_length_zero = sum(weight[n] == 0 for n in range(1 << (r-1), 1 << r))
    cumulative_zero = sum(weight[n] == 0 for n in range(1, 1 << r))
    assert exact_length_zero == (fib(r-1) if r >= 2 else 0), r
    assert cumulative_zero == fib(r+1) - 1, r

# Check the formal four-state quotient automaton, including the absorbing
# class. At the leading 1 the pair is (1,1), representing state P.
# P: a=b!=0; I: b=0; Z: a=0; X: a/b<0 or 0<a/b<1.
for n in range(1, N):
    a, b = weight[n], weight[n+1] if n+1 < N else (0)
    if n == N-1:
        break
    if a == 0: state = 'Z'
    elif b == 0: state = 'I'
    elif a == b: state = 'P'
    else:
        assert a*b < 0 or (0 < a*b and abs(a) < abs(b)), (n,a,b)
        state = 'X'
    qstate = 'P'
    for digit in bin(n)[3:]:
        qstate = {
            'P': {'0':'I','1':'Z'},
            'I': {'0':'P','1':'I'},
            'Z': {'0':'Z','1':'X'},
            'X': {'0':'X','1':'X'},
        }[qstate][digit]
    assert state == qstate, (n, state, qstate)

print('PASS: independent literal signed-digit representations:', literal_representations)
print('PASS: parity-weight recurrence and Stern total through:', MAX_DIRECT)
print('PASS: regular-language classification for all 1<=n<:', N)
print('PASS: exact Fibonacci counts for binary lengths 1..:', MAX_R)
print('PASS: quotient-state automaton checked through:', N-2)
print('Fibonacci shell zero counts r=1..17:', [sum(weight[n] == 0 for n in range(1 << (r-1),1 << r)) for r in range(1, MAX_R+1)])
