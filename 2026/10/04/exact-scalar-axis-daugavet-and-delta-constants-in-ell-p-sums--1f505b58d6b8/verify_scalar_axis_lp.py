from fractions import Fraction

checks = 0

for p in range(2, 7):
    for den in range(2, 31):
        for num in range(0, den + 1):
            t = Fraction(num, den)
            # Transverse witness in powered form: t^p + R^p = 1.
            Rp = 1 - t**p
            assert t**p + Rp == 1
            checks += 1

            if 0 < t < 1:
                # Strict quantitative separation: (1-t^p)^(1/p) > 1-t.
                assert Rp > (1 - t)**p
                checks += 1

                # Delta upper-bound scalar optimization.
                # On s >= t, F_t(s) <= F_t(t) = 1-t^p.
                for j in range(0, 41):
                    s = t + (1 - t) * Fraction(j, 40)
                    F = (s - t)**p + 1 - s**p
                    assert F <= Rp
                    checks += 1

                # On [t-eta,t], use F_t(s) <= 1-(t-eta)^p+eta^p.
                eta = min(t / 3, Fraction(1, 17))
                bound = 1 - (t - eta)**p + eta**p
                for j in range(0, 41):
                    s = (t - eta) + eta * Fraction(j, 40)
                    F = (t - s)**p + 1 - s**p
                    assert F <= bound
                    checks += 1

                # Daugavet coordinate slice near s=1: F decreases for s>=t.
                eta2 = min((1 - t) / 3, Fraction(1, 19))
                left = 1 - eta2
                for j in range(0, 41):
                    s = left + eta2 * Fraction(j, 40)
                    F = (s - t)**p + 1 - s**p
                    Fleft = (left - t)**p + 1 - left**p
                    assert F <= Fleft
                    checks += 1

# Endpoint powered identities.
for p in range(2, 7):
    assert 1 - Fraction(0, 1)**p == 1
    assert 1 - Fraction(1, 1)**p == 0
    checks += 2

print(f"VERIFY_OK {checks}")
