#!/usr/bin/env python3
"""Exact rational checks for the rank-two sign-probe XNysTrace joint law.

Reproduces the conceptual leave-one-out pseudoinverse estimator using the
rank of the sketch and the explicit rank-one Nystrom projection. No external
packages are required. Exhaustive finite tests supplement, not replace, the
proof valid for every number of probes.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product


def matrix_from_leave_one_out(a, b, other_signs):
    """A<Omega> for A=diag(a,b), with columns +- (1,s), s in {-1,1}."""
    if len(set(other_signs)) == 2:
        return ((a, Q(0)), (Q(0), b))
    sign = other_signs[0]
    return ((a*a/(a+b), a*b*sign/(a+b)),
            (a*b*sign/(a+b), b*b/(a+b)))


def estimate_and_posterior(a, b, signs):
    m = len(signs)
    assert m >= 2
    values = []
    for i, sign in enumerate(signs):
        other_signs = signs[:i] + signs[i+1:]
        low = matrix_from_leave_one_out(a, b, other_signs)
        # Held-out test vector w=(1, sign); independent global flips cancel.
        residual_energy = (a-low[0][0])+(b-low[1][1])-2*sign*low[0][1]
        values.append(low[0][0]+low[1][1]+residual_energy)
    mean = sum(values, Q(0)) / m
    posterior = sum(((v-mean)**2 for v in values), Q(0))/(m*(m-1))
    return mean, posterior


def expected_law(a, b, m):
    trace = a+b
    c = 2*a*b/(a+b)
    if m == 2:
        return {(trace-c, Q(0)): Q(1,2),
                (trace+c, Q(0)): Q(1,2)}
    return {
        (trace-c, Q(0)): Q(2, 2**m),
        (trace+c/m, c*c/(m*m)): Q(2*m, 2**m),
        (trace, Q(0)): Q(2**m - 2*m - 2, 2**m),
    }


def check(a, b, m):
    all_cases = list(product((-1, 1), repeat=m))
    actual = Counter(estimate_and_posterior(a,b,list(ss)) for ss in all_cases)
    expect = expected_law(a,b,m)
    for key, probability in expect.items():
        assert Q(actual[key], len(all_cases)) == probability, (a,b,m,key)
    assert sum(actual.values()) == len(all_cases)
    assert set(actual).issubset(expect)
    true = a+b
    mse = sum(((mean-true)**2*cnt for (mean,post),cnt in actual.items()), Q(0))/len(all_cases)
    expected_post = sum((post*cnt for (mean,post),cnt in actual.items()), Q(0))/len(all_cases)
    c = 2*a*b/(a+b)
    if m == 2:
        assert mse == c*c and expected_post == 0
    else:
        assert mse == c*c*(m+1)/(m*2**(m-1))
        assert expected_post == c*c/(m*2**(m-1))
        assert mse == (m+1)*expected_post
    assert sum(((mean-true)*cnt for (mean,post),cnt in actual.items()), Q(0)) == 0
    false_zero = sum(cnt for (mean,post),cnt in actual.items() if post==0 and mean!=true)
    assert Q(false_zero,len(all_cases)) == (Q(1) if m==2 else Q(2, 2**m))
    return len(all_cases)


def main():
    cases = 0
    for a,b in ((Q(1),Q(1)), (Q(2),Q(5)), (Q(1,7),Q(13,4)), (Q(7),Q(1,9))):
        for m in range(2, 10):
            cases += check(a,b,m)
    print(f"VERIFY_OK {cases} exhaustive projective-sign configurations")


if __name__ == '__main__':
    main()
