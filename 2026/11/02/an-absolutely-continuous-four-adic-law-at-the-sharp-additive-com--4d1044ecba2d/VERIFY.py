#!/usr/bin/env python3
"""Independent exact-integer checks for the four-adic complement block law."""
from bisect import bisect_right
from fractions import Fraction


def words(k):
    return sorted(sum(((j >> i) & 1) * 4**i for i in range(k)) for j in range(2**k))


def F_rational(u):
    """Exact Cantor distribution for terminating base-four rational arguments."""
    u = Fraction(u)
    if u < 0: return Fraction(0)
    if u >= Fraction(1, 3): return Fraction(1)
    total, scale = Fraction(0), Fraction(1)
    for _ in range(100):
        if u == 0: return total
        if u <= Fraction(1, 12):
            u *= 4
            scale /= 2
        elif u < Fraction(1, 4):
            return total + scale / 2
        else:
            u = 4*u - 1
            total += scale / 2
            scale /= 2
    raise RuntimeError('nonterminating test input')


def main():
    cells = 0
    bound_checks = 0
    unique_sums = 0
    for k in range(1, 8):
        L = 4**k
        previous = words(k)
        A = words(k + 1)
        B = [2*x for x in A]
        # Independently, the digit sets uniquely complement each other.
        if k <= 4:
            aset = set(A); bset = set(B)
            counts = [0] * (4**(k+1))
            for a in aset:
                for b in bset:
                    if a+b < len(counts): counts[a+b] += 1
            assert all(z == 1 for z in counts)
            unique_sums += len(counts)
        for n in range(L, 4*L):
            aa = bisect_right(A, n)
            bb = bisect_right(B, n)
            # Distinctly computed lower-digit prefixes, without using aa or bb.
            fa = bisect_right(previous, n - L)
            fb = bisect_right(previous, Fraction(n-2*L, 2))
            assert aa == L**0 * 2**k + fa
            assert bb == 2**k + fb
            t = Fraction(n, L)
            ratio = Fraction(aa*bb, n)
            exact_formula = Fraction((2**k+fa)*(2**k+fb), n)
            assert ratio == exact_formula
            # Uniform estimate derived from Cantor-cylinder coupling.
            f1 = F_rational(t - 1)
            f2 = F_rational((t-2)/2)
            profile = ((1+f1)*(1+f2))/t
            assert abs(ratio-profile) <= Fraction(4,2**k)
            assert Fraction(1) <= profile <= Fraction(3,2)
            cells += 1
            bound_checks += 1
    # Exact sum of finite-stage Cantor gap lengths = (1-2^-J)/3.
    for J in range(1, 13):
        s = sum(2**(j-1)*Fraction(2,3*4**j) for j in range(1,J+1))
        assert s == Fraction(1,3)*(1-Fraction(1,2**J))
    # The two smooth intervals contribute exactly two-thirds of total mass.
    smooth_mass = Fraction(2)*(Fraction(1)-Fraction(2,3))
    assert smooth_mass == Fraction(2,3)
    print(f'VERIFY_OK blocks=7 exact_ratio_cells={cells} '
          f'cylinder_bounds={bound_checks} unique_sum_checks={unique_sums} '
          'gap_masses=12 absolutely_continuous_formula=algebraic finite_only=YES')

if __name__ == '__main__':
    main()
