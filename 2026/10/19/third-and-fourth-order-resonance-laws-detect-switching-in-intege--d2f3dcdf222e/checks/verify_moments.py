#!/usr/bin/env python3
"""Independent exact Fourier-coefficient verification for integer expanding circle maps.

No floating-point integrals or dynamical-systems packages are used.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from random import Random


def moments_fourier(slopes):
    frequencies = [1]
    for a in slopes:
        assert isinstance(a, int) and a >= 2
        frequencies.append(frequencies[-1]*a)
    signs = [e for f in frequencies for e in (f, -f)]
    pair = Counter(e + f for e in signs for f in signs)
    m3 = Q(sum(pair[-e] for e in signs), 8)
    m4 = Q(sum(v * pair[-s] for s, v in pair.items()), 16)
    return (Q(0), Q(len(frequencies), 2), m3, m4)


def moments_formula(slopes):
    n = len(slopes)+1
    n2 = sum(a==2 for a in slopes)
    n3 = sum(a==3 for a in slopes)
    n22 = sum(slopes[i]==slopes[i+1]==2 for i in range(len(slopes)-1))
    m3 = Q(3*n2, 4)
    k4 = Q(-3*n, 8) + Q(n3, 2) + Q(3*n22, 2)
    m2 = Q(n, 2)
    return (Q(0), m2, m3, k4 + 3*m2*m2)


def main():
    count = 0
    envelope_checks = 0
    for L in range(0, 11):
        observed = defaultdict(set)
        for slopes in product((2,3), repeat=L):
            actual=moments_fourier(slopes)
            expected=moments_formula(slopes)
            assert actual==expected, (slopes,actual,expected)
            n2=sum(a==2 for a in slopes)
            n22=sum(slopes[i]==slopes[i+1]==2 for i in range(L-1))
            # Invert only the measured third moment and fourth cumulant.
            m3=actual[2]
            k4=actual[3]-3*actual[1]**2
            inferred_n2=Q(4,3)*m3
            inferred_n22=Q(2,3)*(k4+Q(3*(L+1),8)-Q(L-inferred_n2,2))
            assert inferred_n2==n2 and inferred_n22==n22
            observed[n2].add(n22)
            count+=1
        for n2 in range(L+1):
            if n2==0: target={0}
            else: target=set(range(max(0,2*n2-L-1),n2))
            assert observed[n2]==target, (L,n2,observed[n2],target)
            envelope_checks+=1
    rng=Random(20261014)
    for _ in range(250):
        L=rng.randrange(0,17)
        slopes=[rng.choice((2,3,4,5,7,11)) for _ in range(L)]
        assert moments_fourier(slopes)==moments_formula(slopes),slopes
        count+=1
    print('PASS exact Fourier comparisons:',count)
    print('PASS complete sharp-envelopes:',envelope_checks)
    print('Fourier expansions are finite integer counts; no numerical integration.')

if __name__=='__main__': main()
