#!/usr/bin/env python3
"""Exact finite checks of geometric-delay plateau identities.

No finite check substitutes for the ergodic or almost-sure arguments in RESULT.md.
"""
from fractions import Fraction
from itertools import product

cases=0
for base in (2,3,4,5):
    threshold=lambda k:(base**k-1)//(base-1)
    for length in range(2,8):
        symbols=[((7*j*j+3*j+length)%11)//6 for j in range(length)]
        # Actual delayed shift index, not a block-formula shortcut.
        e=[0]
        for n in range(threshold(length)-1):
            e.append(e[n//base]+1)
        assert len(e)==threshold(length)
        for k in range(length):
            assert all(e[n]==k for n in range(threshold(k),threshold(k+1)))
        for j in range(1,length+1):
            empirical=Fraction(sum(symbols[e[n]] for n in range(threshold(j))),threshold(j))
            geometric=Fraction(sum(base**i*symbols[i] for i in range(j)),threshold(j))
            assert empirical==geometric
            # With older past digits set to zero, the truncated backward
            # transform differs by at most base^(-j).
            window=sum((Fraction(base-1,base**r)*symbols[j-r]
                        for r in range(1,j+1)),Fraction(0,1))
            assert abs(geometric-window)<=Fraction(1,base**j)
            cases+=1

# All digit words: exact normalized finite geometric measure moments.
moment_cases=0
for base in (2,3,4,5):
    for depth in range(1,8):
        weights=[Fraction(base-1,base**r) for r in range(1,depth+1)]
        for numerator in range(1,4):
            p=Fraction(numerator,4)
            m1=m2=Fraction(0)
            for digits in product((0,1),repeat=depth):
                probability=Fraction(1)
                for bit in digits:
                    probability*=p if bit else 1-p
                val=sum((w*bit for w,bit in zip(weights,digits)),Fraction(0))
                m1+=probability*val
                m2+=probability*val*val
            sum_w=sum(weights)
            sum_w2=sum(w*w for w in weights)
            assert m1==p*sum_w
            assert m2-m1*m1==p*(1-p)*sum_w2
            moment_cases+=1
print('PLATEAU_AND_DISCOUNT_IDENTITY_PASS',cases)
print('EXACT_BERNOULLI_FINITE_MOMENT_PASS',moment_cases)
print('INFINITE_LIMIT_THEOREMS_REQUIRE_ANALYTIC_PROOF')
