#!/usr/bin/env python3
import cmath
import itertools
import math

TOL = 1e-8


def primes_upto(n):
    out = []
    for q in range(2, n + 1):
        if all(q % d for d in range(2, int(q ** 0.5) + 1)):
            out.append(q)
    return out


def dft_values(p, xs, cs):
    rho = cmath.exp(-2j * math.pi / p)
    return [sum(c * (rho ** (k * x)) for x, c in zip(xs, cs)) for k in range(p)]


def zero_count(vals):
    return sum(abs(v) < TOL for v in vals)


def central_label(A, p):
    A = tuple(A)
    for pair1 in itertools.combinations(range(4), 2):
        rest = tuple(i for i in range(4) if i not in pair1)
        i, j = pair1
        r, s = rest
        if (A[i] + A[j] - A[r] - A[s]) % p == 0:
            # Return labels with equal-sum pairs (x1,x4) and (x2,x3).
            return (A[i], A[r], A[s], A[j])
    return None


def one_zero_coeffs(p, xs):
    # The proof only needs finite phase avoidance. For the finite replay, search
    # deterministic unit phases until a witness with exactly one zero is found.
    for j in range(1, 200):
        u = cmath.exp(1j * (j * math.sqrt(2.0) / 17.0))
        cs = (1.0 + 0j, -1.0 + 0j, u, -u)
        if zero_count(dft_values(p, xs, cs)) == 1:
            return cs
    raise AssertionError((p, xs, "no one-zero witness found"))


def main():
    support_checks = 0
    central_checks = 0
    witness_checks = 0
    min_nonzero_margin = float("inf")
    for p in primes_upto(31):
        if p < 5:
            continue
        rho = cmath.exp(-2j * math.pi / p)
        for A in itertools.combinations(range(p), 4):
            support_checks += 1
            vals0 = dft_values(p, A, (1, 1, 1, 1))
            assert zero_count(vals0) == 0, (p, A, "indicator zero")
            witness_checks += 1

            cs1 = one_zero_coeffs(p, A)
            vals1 = dft_values(p, A, cs1)
            assert zero_count(vals1) == 1, (p, A, "one-zero witness")
            nz = [abs(v) for v in vals1 if abs(v) >= TOL]
            if nz:
                min_nonzero_margin = min(min_nonzero_margin, min(nz))
            witness_checks += 1

            lab = central_label(A, p)
            if lab is not None:
                central_checks += 1
                x1, x2, x3, x4 = lab
                alpha = rho ** (x1 - x3)
                cs2 = (1.0 + 0j, -1.0 + 0j, -alpha, alpha)
                vals2 = dft_values(p, lab, cs2)
                assert zero_count(vals2) == 2, (p, A, lab, "two-zero witness", vals2)
                assert abs(vals2[0]) < TOL and abs(vals2[1]) < TOL, (p, A, "zeros not at 0,1")
                witness_checks += 1
    print("VERIFY_OK primes=", len([q for q in primes_upto(31) if q >= 5]),
          "supports=", support_checks,
          "central=", central_checks,
          "witness_checks=", witness_checks,
          "min_nonzero_margin=", f"{min_nonzero_margin:.3e}")


if __name__ == "__main__":
    main()
