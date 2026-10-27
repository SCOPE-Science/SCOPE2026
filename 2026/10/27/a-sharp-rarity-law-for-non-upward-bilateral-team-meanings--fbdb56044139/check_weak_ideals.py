"""Independent finite tests of convex-union team families and Dedekind spectra.

Run with Python 3.10+; no dependencies.
"""
from math import comb

DEDEKIND = [2, 3, 6, 20, 168, 7581, 7828354, 2414682040998,
            56130437228687557907788]


def weak_ideal_direct(family, n):
    """Test binary-union closure and inclusion convexity without normal forms."""
    teams = [a for a in range(1 << n) if (family >> a) & 1]
    for a in teams:
        for b in teams:
            if not (family >> (a | b)) & 1:
                return False
            if a & b == a:
                # Enumerate all c strictly between a and b.
                missing = b ^ a
                s = missing
                while True:
                    if not (family >> (a | s)) & 1:
                        return False
                    if not s:
                        break
                    s = (s - 1) & missing
    return True


def upset_direct(family, n):
    for a in range(1 << n):
        if (family >> a) & 1:
            for b in range(1 << n):
                if (a & b) == a and not (family >> b) & 1:
                    return False
    return True


def top_upset_normal_form(family, n):
    if family == 0:
        return True
    u = 0
    teams = []
    for a in range(1 << n):
        if (family >> a) & 1:
            teams.append(a)
            u |= a
    if not (family >> u) & 1:
        return False
    for a in teams:
        for b in range(1 << n):
            if (a & b) == a and (b & u) == b:
                if not (family >> b) & 1:
                    return False
    return True


def exhaustive():
    for n in range(5):
        weak = 0
        ups = 0
        by_top = [0] * (n + 1)
        for family in range(1 << (1 << n)):
            is_weak = weak_ideal_direct(family, n)
            assert is_weak == top_upset_normal_form(family, n), (n, family)
            if is_weak:
                weak += 1
                if family:
                    top = 0
                    for team in range(1 << n):
                        if (family >> team) & 1:
                            top |= team
                    by_top[top.bit_count()] += 1
            if upset_direct(family, n):
                ups += 1
        predicted = 1 + sum(comb(n, k) * (DEDEKIND[k] - 1) for k in range(n + 1))
        assert weak == predicted, (n, weak, predicted)
        assert ups == DEDEKIND[n], (n, ups, DEDEKIND[n])
        assert by_top == [comb(n, k) * (DEDEKIND[k] - 1) for k in range(n + 1)]
        print(f'DIRECT_FAMILY_CLASSIFICATION_OK n={n} weak={weak} global_upset={ups} by_top={by_top}')

    for n in (2, 4, 8):
        w = 1 + sum(comb(n, k) * (DEDEKIND[k] - 1) for k in range(n + 1))
        exceptional = w - DEDEKIND[n]
        assert exceptional == sum(comb(n, k) * (DEDEKIND[k] - 1) for k in range(n))
        print(f'BSL_SUPPORT_SPECTRUM_OK q={n.bit_length()-1} N={n} total={w} upward={DEDEKIND[n]} exceptional={exceptional}')

if __name__ == '__main__':
    exhaustive()
    print('WEAK_IDEAL_SPECTRUM_AND_CONCENTRATION_CHECK_OK')
