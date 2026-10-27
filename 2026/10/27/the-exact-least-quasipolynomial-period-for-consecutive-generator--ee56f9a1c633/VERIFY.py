#!/usr/bin/env python3
"""Exact-integer checks for the sharp Frobenius-quotient period theorem.

This finite script corroborates the stated formulas and witnesses, but the
infinite theorem is proved by the algebraic argument in RESULT.md.
"""


def direct_quotient_frobenius(a, p):
    """Largest n >= 0 for which p*n is absent from <a,a+1>."""
    frobenius = a*a - a - 1
    return max(n for n in range(1, frobenius // p + 1)
               if (p*n) % a > (p*n) // a)


def residue_minimum(a, p):
    frobenius = a*a - a - 1
    candidates = [(i*a + j, i, j)
                  for i in range(p)
                  for j in range(i+1)
                  if (i*a + j - frobenius) % p == 0]
    cost, i, j = min(candidates)
    return (frobenius - cost) // p, (i, j)


def main():
    full_cases = 0
    gap_witnesses = 0
    zero_branch_cases = 0
    for p in range(2, 51):
        for a in range(p+1, 3*p+15):
            exact, pair = residue_minimum(a, p)
            direct = direct_quotient_frobenius(a, p)
            assert exact == direct, (p,a,exact,direct,pair)
            full_cases += 1
        for a in (2*p, 3*p, 4*p):
            assert residue_minimum(a,p)[0] == a*a//p-a-1
            zero_branch_cases += 1

    for p in range(2, 201):
        for d in range(1, p):
            if p % d:
                continue
            k = p // d
            i, j = d+k-2, d-1
            assert 0 <= j <= i <= p-1
            assert p-1-i == (d-1)*(k-1)
            for a in (p+d, 2*p+d, 3*p+d):
                assert a > p and a % p == d
                assert i <= a-2
                F = a*a-a-1
                assert (F-i*a-j)%p == 0
                proposed_gap = F-i*a-j
                u, v = divmod(proposed_gap, a)
                assert v > u, (p, d, a, proposed_gap)
                lower = proposed_gap//p
                baseline_numerator = a*a - p*a - p
                assert p*lower > baseline_numerator
                assert (p-1-i)*a+(p-1-j) == (d-1)*(k-1)*a+p-d
                gap_witnesses += 1

    print('VERIFY_OK', 'direct_minimum_cases='+str(full_cases),
          'zero_branch_cases='+str(zero_branch_cases),
          'divisor_witnesses='+str(gap_witnesses),
          'exact_integer_checks=PASS')


if __name__=='__main__':
    main()
