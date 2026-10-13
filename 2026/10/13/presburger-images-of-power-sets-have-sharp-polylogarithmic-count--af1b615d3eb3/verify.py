#!/usr/bin/env python3
from math import comb

# Finite replay of the sharpness construction.  For B>M, base-B digits in a
# sum of M powers are digit multiplicities, hence multisets of exponents are
# uniquely encoded without carries.
assertions = 0
for M in range(1, 8):
    B = M + 1
    for L in range(0, 9):
        vals=set()
        def rec(last, left, s):
            global assertions
            if left==0:
                vals.add(s)
                return
            for e in range(last, L+1):
                rec(e, left-1, s+B**e)
        rec(0, M, 0)
        expected=comb(L+M, M)
        assert len(vals)==expected, (M,B,L,len(vals),expected)
        assertions += 1
        # Every value is at most M*B^L, so all counted values lie in the
        # claimed interval for H=M*B^L.
        H=M*(B**L)
        assert max(vals) <= H
        assertions += 1
print(f"VERIFY_OK {assertions} exact assertions")
