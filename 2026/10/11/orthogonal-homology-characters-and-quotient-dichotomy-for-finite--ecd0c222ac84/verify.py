"""Finite coefficient checks for reflection Euler and quotient character formulas.

This program verifies finitely many parameter values. The written proof,
not this loop, establishes statements for every permitted parameter.
"""
from math import comb


def binom_int(a, k):
    if k == 0:
        return 1
    v = 1
    for i in range(1, k + 1):
        v = v * (a - i + 1) // i
    return v


def chi_config(j, chi_c):
    return binom_int(chi_c, j)


def fixed_exact_size(d, q):
    # A fixed set has j equatorial points and k off-equator pairs, j + 2k = q.
    ce = 2 if d % 2 else 0      # chi(S^{d-1})
    ch = -1 if d % 2 else 1     # compact-support chi(R^d)
    return sum(chi_config(q-2*k, ce) * chi_config(k, ch)
               for k in range(q//2 + 1))


def prediction(d, n):
    if d % 2 == 0:
        return [(n*d, (-1)**n), ((n-1)*d, (-1)**(n-1))]
    return [((n+1)//2 * (d+1)-1, (-1)**((n+1)//2))]


def test():
    cases=0
    for d in range(2, 19):
        for n in range(2, 131):
            fixed = sum(fixed_exact_size(d, j) for j in range(1, n+1))
            homology = prediction(d,n)
            assert len({k for k,_ in homology}) == len(homology)
            chi_total = 1 + sum((-1)**k for k,_ in homology)
            expected_total = 3 if d % 2 == 0 else 0
            assert chi_total == expected_total
            lefschetz = 1 + sum((-1)**k * sign for k, sign in homology)
            assert fixed == lefschetz, (d,n,fixed,lefschetz)
            expected_fixed = (1 if d % 2 == 0 else
                              (2 if n % 4 in (1,2) else 0))
            assert fixed == expected_fixed
            invariants = [(k, (1+sign)//2) for k,sign in homology]
            if d % 2 == 0:
                assert sum(mult for _,mult in invariants) == 1
                assert invariants[n % 2][1] == 1
            else:
                assert sum(mult for _,mult in invariants) == (n % 4 in (0,3))
            quotient_euler = 1 + sum((-1)**k * mult for k,mult in invariants)
            assert quotient_euler * 2 == chi_total + fixed
            cases+=1
    return cases

if __name__ == '__main__':
    print('VERIFY_OK cases=',test())
