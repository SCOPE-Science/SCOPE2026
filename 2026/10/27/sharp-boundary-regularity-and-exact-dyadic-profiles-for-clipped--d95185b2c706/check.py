"""Exact finite-cylinder checks for the clipped feedback binary model."""
from fractions import Fraction as F
from itertools import product

EPS = F(1, 4)
ALPHA = F(1, 2)
UPPER = 1 - EPS

def update(p, symbol):
    return min(UPPER, max(EPS, (1 - ALPHA) * p + ALPHA * symbol))

def prefix_probability(p, bits):
    weight = F(1)
    for bit in bits:
        weight *= p if bit else 1-p
        p = update(p,bit)
    return weight

def update_after_run(p, bit, count):
    for _ in range(count):
        p=update(p,bit)
    return p

def exact_tail(p, threshold, nbits, at_least):
    total=F(0)
    for word in product((0,1), repeat=nbits):
        val=F(sum(word[i]*2**(nbits-1-i) for i in range(nbits)),2**nbits)
        if (val >= threshold) if at_least else (val < threshold):
            total += prefix_probability(p, word)
    return total

assert update(UPPER,0)==F(3,8)
h=UPPER+(1-UPPER)*update(UPPER,0)
assert h==F(27,32)
for p in [EPS,F(1,2),UPPER]:
    for n in range(1,7):
        one_run=prefix_probability(p,[1]*n)
        zero_run=prefix_probability(p,[0]*n)
        assert exact_tail(p,1-F(1,2**n),n,True)==one_run
        assert exact_tail(p,F(1,2**n),n,False)==zero_run
        # u=3/4. Event is determined by n+2 initial bits.
        if update_after_run(p,1,n)==UPPER:
            assert exact_tail(p,1-F(3,2**(n+2)),n+2,True)==one_run*h
        if update_after_run(p,0,n)==EPS:
            assert exact_tail(p,F(3,2**(n+2)),n+2,False)==zero_run*h

print('CHECKS_PASS: 36 dyadic endpoint tests and 34 saturated u=3/4 tests; H(3/4)=27/32')
