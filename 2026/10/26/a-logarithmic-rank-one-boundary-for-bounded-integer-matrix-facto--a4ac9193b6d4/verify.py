"""Exact finite checks for bounded factorizations of E11 over the integers.

Run: python verify.py
All enumerations use exact integer arithmetic. Finite checks are not the
proof of the asymptotic claim.
"""
from math import gcd


def primitive_shell(h):
    return sum(gcd(u, v) == 1
               for u in range(-h, h + 1)
               for v in range(-h, h + 1)
               if max(abs(u), abs(v)) == h)


def euler_phi(h):
    return sum(gcd(k, h) == 1 for k in range(1, h + 1))


def exact_decomposition(T):
    z = range(-T, T + 1)
    S = 0
    C = 0
    for u in z:
        for v in z:
            if gcd(u, v) != 1:
                continue
            h = max(abs(u), abs(v))
            U = sum(a*u + b*v == 1 for a in z for b in z)
            R = 2 * (T // h) + 1
            S += U * R
            C += U
    return 2 * S - C, S, C


def independent_full_enumeration(T):
    z = range(-T, T + 1)
    pairs = [(a, b) for a in z for b in z]
    total = 0
    # Directly enumerate B and independently count its admissible A rows.
    for e, f in pairs:
        for g, h in pairs:
            first = sum(a*e + b*g == 1 and a*f + b*h == 0
                        for a, b in pairs)
            if not first:
                continue
            second = sum(c*e + d*g == 0 and c*f + d*h == 0
                         for c, d in pairs)
            total += first * second
    return total


def main():
    for T in range(1, 7):
        decomposition, S, C = exact_decomposition(T)
        direct = independent_full_enumeration(T)
        assert decomposition == direct, (T, decomposition, direct)
        assert 2 * S - C == direct
    for h in range(1, 41):
        assert primitive_shell(h) == 8 * euler_phi(h), h
    print("VERIFY_OK heights=1..6 direct_AB_counts=6 "
          "primitive_shells=40 integer_exact=PASS finite_only=YES")


if __name__ == "__main__":
    main()
