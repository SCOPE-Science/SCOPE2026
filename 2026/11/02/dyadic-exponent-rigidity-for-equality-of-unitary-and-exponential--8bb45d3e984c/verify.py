#!/usr/bin/env python3
"""Exact supplementary tests of the dyadic-exponent divisibility theorem."""
from itertools import count

def divisor_exponents(a):
    return [d for d in range(1, a+1) if a % d == 0]

def main():
    bases = range(2, 60)
    checks = 0
    initial = []
    bounds = 0
    for b in bases:
        for t in range(1, 9):
            a = 1 << t
            den = sum(b ** (1 << j) for j in range(t)) - 1
            num = b**a + 1
            assert den > 0
            if t == 1:
                if num % den == 0:
                    initial.append((b, num // den))
                assert (num % den == 0) == (b in (2, 3))
            else:
                assert num % den != 0
                if t == 2:
                    remainder = (b-1)**2 + 1
                    assert 0 < remainder < den
                else:
                    y = b ** (1 << (t-2))
                    u = sum(b ** (1 << j) for j in range(t-2)) - 1
                    assert 1 <= u and 3*u <= y
                    representative = (y+u)**2 + 1
                    assert den < representative < 2*den
                    remainder = representative - den
                    bounds += 1
                assert num % den == remainder
            if b in (2, 3, 5, 7, 11, 13) and t <= 6:
                sigma_star = (b**a+1)*6
                sigma_exp = 5*sum(b**d for d in divisor_exponents(a))
                assert (sigma_star == sigma_exp) == (t == 1 and b in (2,3))
            checks += 1
    assert initial == [(2,5),(3,5)]
    print('VERIFY_OK integer_base_cases=%d remainder_bounds=%d initial_quotients=%s' % (checks, bounds, initial))

if __name__ == '__main__':
    main()
