#!/usr/bin/env python3
"""Finite regression checks for the integer zero-one defect lemma."""
from itertools import product

for x in range(-10000,10001):
    v=x*(x-1)
    assert v>=0
    assert (v==0)==(x in (0,1))

checked=0
for length in range(0,8):
    for xs in product(range(-3,4), repeat=length):
        s=sum(xs)
        q=sum(x*x for x in xs)
        if s==q and s>=0:
            checked+=1
            assert all(x in (0,1) for x in xs)
            assert xs.count(1)==s
            assert xs.count(0)==length-s

print(f"VERIFY_OK integer_window=-10000..10000 exhaustive_lengths=0..7 values=-3..3 solutions={checked} zero_one_only=true")
