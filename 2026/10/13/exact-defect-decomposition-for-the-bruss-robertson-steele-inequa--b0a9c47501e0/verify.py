#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

VALUES=(F(1,2),F(1),F(3,2),F(2),F(5,2))
BUDGETS=(F(1),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4),F(5))
THRESHOLDS=(F(3,4),F(1),F(5,4),F(3,2),F(7,4),F(2),F(9,4))

def packing(xs,s):
    order=sorted(range(len(xs)), key=lambda i:(xs[i],i))
    total=F(0)
    A=[]
    for i in order:
        if total+xs[i] <= s:
            total += xs[i]
            A.append(i)
        else:
            break
    return set(A),total

exact_cases=0
equality_cases=0
for n in range(1,6):
    for xs in product(VALUES, repeat=n):
        for s in BUDGETS:
            A,SA=packing(xs,s)
            N=len(A)
            for t in THRESHOLDS:
                B={i for i,x in enumerate(xs) if x<=t}
                SB=sum((xs[i] for i in B),F(0))
                phi=F(len(B))+(s-SB)/t
                lhs=phi-F(N)
                mismatch=sum((abs(xs[i]-t) for i in A.symmetric_difference(B)),F(0))
                rhs=(s-SA+mismatch)/t
                assert lhs == rhs
                assert rhs >= 0
                exact_cases += 1
                if all(x != t for x in xs) and SB == s:
                    assert A == B
                    assert SA == s
                    assert lhs == 0
                    equality_cases += 1
print(f"VERIFY_OK exact_cases={exact_cases} equality_cases={equality_cases}")
