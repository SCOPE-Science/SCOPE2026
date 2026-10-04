#!/usr/bin/env python3
from fractions import Fraction

def closed_form(m, p, b):
    q = 1 - p
    return Fraction(m - b) + q / p - q ** (b + 1) * (Fraction(m) + q / p)

def direct_initial(m, p, b):
    q = 1 - p
    out = Fraction(0)
    for j in range(b + 1):
        out += p * q ** j * Fraction(m + j - b)
    out += q ** (b + 1)
    return out

def replay(m, p, horizon):
    q = 1 - p
    e = []
    for b in range(min(m, horizon + 1)):
        e.append(direct_initial(m, p, b))
    for b in range(m, horizon + 1):
        e.append(q * e[b - 1] + p * e[b - m])
    return e

def exact_k(m, p):
    q = 1 - p
    mu = q + p * m
    candidates = [b for b in range(m - 1) if mu * q ** b >= 1]
    assert candidates
    return max(candidates)

def run():
    cases = 0
    for m in range(2, 26):
        for den in range(2, 21):
            for num in range(1, den):
                p = Fraction(num, den)
                q = 1 - p
                mu = q + p * m
                k = exact_k(m, p)

                assert 0 <= k <= m - 2
                assert mu * q ** (m - 1) < 1

                for b in range(m):
                    assert direct_initial(m, p, b) == closed_form(m, p, b)

                e = replay(m, p, 12 * m)

                for b in range(1, m):
                    assert e[b] - e[b - 1] == mu * q ** b - 1

                peak = e[k]
                assert all(x <= peak for x in e)

                tie = (k >= 1 and mu * q ** k == 1)
                initial_maxima = [b for b in range(m) if e[b] == peak]
                if tie:
                    assert initial_maxima == [k - 1, k]
                else:
                    assert initial_maxima == [k]

                later_maxima = [b for b in range(m, len(e)) if e[b] == peak]
                assert later_maxima == []

                cases += 1

    print(f"VERIFY_OK cases={cases}")

if __name__ == "__main__":
    run()
