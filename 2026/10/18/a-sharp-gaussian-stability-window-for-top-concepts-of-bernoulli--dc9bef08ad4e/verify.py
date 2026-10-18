"""Independent finite tests for a Bernoulli formal-context stability theorem.

Only standard-library dependencies.  This file enumerates complete incidence
matrices, not merely sample rows or columns; asymptotic results are proved in
RESULT.md, not inferred from these finite tests.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, log1p, log


def exact_formula(m, n, p):
    return sum((comb(m, t) * (1 - p**t + p**m)**n for t in range(m+1)), Fraction(0)) / (2**m)


def direct_stability_numerator(m, columns):
    full = (1 << m) - 1
    common_all = tuple(i for i, col in enumerate(columns) if col == full)
    total = 0
    for subset in range(1 << m):
        common_subset = tuple(i for i, col in enumerate(columns) if (subset & col) == subset)
        total += (common_subset == common_all)
    return total


def enumerate_expectation(m, n, p):
    total = Fraction(0)
    inspected = 0
    for columns in product(range(1 << m), repeat=n):
        ones = sum(col.bit_count() for col in columns)
        probability = p**ones * (1-p)**(m*n-ones)
        total += probability * direct_stability_numerator(m, columns) / (2**m)
        inspected += 1
    return total, inspected


def finite_expectation(m, n, p):
    s = 0.0
    for t in range(m+1):
        q = p**t - p**m
        log_success = (m*log(p)) if t == 0 else log1p(-q)
        s += comb(m,t) * exp(n*log_success) / (2**m)
    return s


def main():
    inspected = 0
    cases = 0
    for p in (Fraction(1,2), Fraction(1,3), Fraction(2,3)):
        for m in range(1,4):
            for n in range(1,4):
                got, cnt = enumerate_expectation(m,n,p)
                want = exact_formula(m,n,p)
                assert got == want, (p,m,n,got,want)
                inspected += cnt
                cases += 1
    for m,n in ((3,4),(4,3)):
        got, cnt = enumerate_expectation(m,n,Fraction(1,2))
        want=exact_formula(m,n,Fraction(1,2))
        assert got==want,(m,n)
        inspected+=cnt
        cases+=1
    # These checks use the exact expectation formula; they do not prove any
    # asymptotic limit.  At the critical scale it trends toward 1/2.
    p=0.5
    previous=None
    crit=[]
    for m in (16,24,32,48,64,96,128):
        n=2**(m//2)
        v=finite_expectation(m,n,p)
        assert 0<v<1
        if m>=24:
            assert v>previous, (m,v,previous)
        previous=v
        crit.append((m,round(v,8)))
    assert abs(crit[-1][1]-0.5)<0.065
    print('VERIFY_OK exact_parameter_cases=', cases, 'complete_binary_matrices=', inspected,
          'all_weighted_probabilities=PASS top_intent_direct_enumeration=PASS')
    print('CRITICAL_EXPECTATIONS p=1/2 log_attributes=(m/2)log2:', crit)
    print('ASYMPTOTICS proof_only=TRUE independent_external_audit=NOT_PERFORMED')

if __name__ == '__main__':
    main()
