#!/usr/bin/env python3
"""Bounded exact checks for an odd divisor-power mean congruence.

For odd n and even r, put Q_r(n)=sigma_r(n)/tau(n), viewed in Z_2.
The script computes sigma_r(n) and tau(n) exactly from prime factorization,
cancels common powers of 2, and compares the resulting 2-adic residue mod 8
with the predicted residue.
"""

from math import isqrt

LIMIT = 200_000
R_VALUES = (2, 4, 6, 8, 10)


def smallest_prime_factors(limit: int):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(n: int, spf):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def sigma_r_tau_from_factorization(fac, r: int):
    sigma = 1
    tau = 1
    for p, e in fac:
        sigma *= sum(p ** (r * j) for j in range(e + 1))
        tau *= e + 1
    return sigma, tau


def two_adic_mod8(num: int, den: int):
    while num % 2 == 0 and den % 2 == 0:
        num //= 2
        den //= 2
    if den % 2 == 0:
        raise AssertionError("quotient is not a 2-adic unit")
    return (num % 8) * pow(den % 8, -1, 8) % 8


def integer_square_quotient(num: int, den: int):
    if num % den:
        return False
    q = num // den
    s = isqrt(q)
    return s * s == q


def main():
    spf = smallest_prime_factors(LIMIT)
    checked = 0
    mismatches = []
    rms = []

    for n in range(1, LIMIT + 1, 2):
        fac = factor(n, spf)
        for r in R_VALUES:
            sigma, tau = sigma_r_tau_from_factorization(fac, r)
            actual = two_adic_mod8(sigma, tau)
            if r % 4 == 0:
                predicted = 1
            else:
                predicted = 1 if n % 8 in (1, 7) else 5
            checked += 1
            if actual != predicted:
                mismatches.append((n, r, actual, predicted))
                if len(mismatches) >= 20:
                    break
        if mismatches:
            break

        sigma2, tau = sigma_r_tau_from_factorization(fac, 2)
        if integer_square_quotient(sigma2, tau):
            rms.append(n)

    print(f"odd n checked: {(LIMIT + 1)//2}")
    print(f"(n,r) congruence checks: {checked}")
    print(f"mismatches: {len(mismatches)}")
    if mismatches:
        for row in mismatches:
            print("mismatch", row)
        raise SystemExit(1)
    print(f"odd RMS numbers <= {LIMIT}: {len(rms)}")
    print("odd RMS residues mod 8:", sorted(set(n % 8 for n in rms)))
    print("odd RMS numbers:", " ".join(map(str, rms)))


if __name__ == "__main__":
    main()
