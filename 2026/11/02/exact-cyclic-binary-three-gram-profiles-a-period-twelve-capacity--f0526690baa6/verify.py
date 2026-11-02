#!/usr/bin/env python3
"""Checks for the exact count of binary circular 3-gram profiles.

All comparisons are exact integer computations and require only Python's stdlib.
Finite checking supplements, but does not replace, the combinatorial proof.
"""
from fractions import Fraction


def exact_formula(n):
    assert isinstance(n, int) and n >= 1
    tau3 = 2 if n % 3 == 0 else -1
    tau4 = (1 if n % 4 == 0 else -1 if n % 4 == 2 else 0)
    value = (Fraction(6*n**4 + 276*n**2 + 3943, 1728)
             + Fraction(19*(-1)**n, 64)
             + Fraction(tau4, 8)
             + Fraction(4*tau3, 27))
    assert value.denominator == 1, (n, value)
    return value.numerator


def direct_word_profiles(n):
    spectra = set()
    for mask in range(1 << n):
        triple_counts = [0] * 8
        for i in range(n):
            triple = (((mask >> i) & 1) << 2
                      | ((mask >> ((i+1) % n)) & 1) << 1
                      | ((mask >> ((i+2) % n)) & 1))
            triple_counts[triple] += 1
        spectra.add(tuple(triple_counts))
    return spectra


def enumerated_profile_vectors(n):
    """Independent enumeration from balance + connectedness classifications."""
    profiles = set()
    # Isolated loops and the connected 010 <-> 101 alternating cycle.
    for i in (0, 7):
        v = [0]*8
        v[i] = n
        profiles.add(tuple(v))
    if n % 2 == 0:
        v = [0]*8
        v[2] = v[5] = n//2
        profiles.add(tuple(v))
    # 001/100 core, with optional 000 loops and 101/010 two-cycle.
    for b in range(1, n//3 + 1):
        for f in range((n-3*b)//2 + 1):
            a = n-3*b-2*f
            v = [0]*8
            v[0],v[1],v[4],v[2],v[5] = a,b,b,b+f,f
            profiles.add(tuple(v))
    # 011/110 core: reflected case.
    for d in range(1, n//3 + 1):
        for c in range((n-3*d)//2 + 1):
            h = n-3*d-2*c
            v = [0]*8
            v[7],v[3],v[6],v[2],v[5] = h,d,d,c,c+d
            profiles.add(tuple(v))
    # Both bridges: b>0,d>0, t>=max(b,d), a,h>=0.
    for b in range(1, n+1):
        for d in range(1, n+1):
            t = max(b,d)
            while b+d+2*t <= n:
                for a in range(n-b-d-2*t+1):
                    h = n-b-d-2*t-a
                    v = [a,b,t-d,d,b,t-b,d,h]
                    profiles.add(tuple(v))
                t += 1
    return profiles


def check():
    direct_total = 0
    for n in range(1, 19):
        from_words = direct_word_profiles(n)
        from_cases = enumerated_profile_vectors(n)
        assert from_words == from_cases, (n, len(from_words), len(from_cases))
        assert len(from_words) == exact_formula(n), (n,len(from_words),exact_formula(n))
        direct_total += len(from_words)
    for n in range(19, 47):
        by_cases = enumerated_profile_vectors(n)
        assert len(by_cases) == exact_formula(n), (n,len(by_cases),exact_formula(n))
    print('VERIFY_OK literal_binary_words_lengths=1..18 all_eight_gram_coordinates_checked=True')
    print('VERIFY_OK enumerated_profile_cases_lengths=1..46 rational_formula=True')
    print('VERIFY_OK count_n12=',exact_formula(12),'count_n24=',exact_formula(24), 'literal_total=',direct_total)

if __name__ == '__main__':
    check()
