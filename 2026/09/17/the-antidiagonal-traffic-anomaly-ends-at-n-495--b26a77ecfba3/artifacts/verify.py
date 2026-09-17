#!/usr/bin/env python3
"""Exact finite certificate for SCOPE-20260917-002.

Checks the finite portion 496 <= n <= 2999 of the proposed proof of
Gil--Liang--Odetola--Weiner Conjecture 7.4 (arXiv:2609.01562).
All comparisons R_n(k) < 1 are done with Python integers, not floating point.
"""

from math import comb, pi, e, sqrt, exp


def P(n: int, k: int) -> int:
    """Sign polynomial controlling R_n(k+2)/R_n(k)."""
    return n*n - 5*n - 2 - n*(2*k*k + 7*k) - k


def candidate_mode_k(n: int) -> int:
    """First positive admissible k with P(n,k) <= 0.

    Positive admissible k have the same parity as n.  By strict decrease of
    P(n,k) in k, this is a global maximizer of R_n(k) over k>0.
    """
    k = 1 if n % 2 else 2
    while P(n, k) > 0:
        k += 2
    return k


def R_numden(n: int, k: int):
    """Exact numerator/denominator of R_n(k)."""
    assert 0 <= k <= n - 2 and (n-k) % 2 == 0
    a = (n-k)//2
    num = (k+1)*(n-k)*(2*n-1) * comb(n, a)**2
    den = n*(n-1) * comb(2*n, n)
    return num, den


def R_float(n: int, k: int) -> float:
    num, den = R_numden(n, k)
    return num / den


def envelope(n: int) -> float:
    """Analytic upper envelope used for the n>=3000 tail."""
    Cn = (1 + 1/(2*(n-1))) * sqrt(1 + 1/(2*n))
    return (
        2/sqrt(pi*e)
        * (sqrt(2*n+3)+1)/sqrt(n)
        * Cn
        * exp(1/(sqrt(2*n+3)+1) + 1/(n+1))
    )


def main():
    failures = []
    tight = (0.0, None, None)

    for n in range(496, 3000):
        k = candidate_mode_k(n)
        num, den = R_numden(n, k)
        if num >= den:
            failures.append((n, k, num-den))
        value = num / den
        if value > tight[0]:
            tight = (value, n, k)

        # Even n has a central obstruction k=0, excluded from rho by symmetry.
        # Check it too, exactly, for completeness.
        if n % 2 == 0:
            cnum, cden = R_numden(n, 0)
            if cnum >= cden:
                failures.append((n, 0, cnum-cden))

    assert not failures, failures[:5]

    # Sharpness at n=495.
    k495 = candidate_mode_k(495)
    num495, den495 = R_numden(495, k495)
    assert num495 > den495

    assert envelope(3000) < 0.995

    print("Exact finite certificate: PASS")
    print("Checked all n = 496,...,2999 using integer arithmetic.")
    print(f"Tightest finite case: n={tight[1]}, k={tight[2]}, R={tight[0]:.15f}")
    print(f"Sharpness witness: n=495, k={k495}, R={num495/den495:.15f} > 1")
    print(f"Analytic tail envelope at n=3000: E(3000)={envelope(3000):.15f} < 0.995")
    print("The proof note shows E(n) decreases, hence E(n)<1 for every n>=3000.")


if __name__ == "__main__":
    main()
