"""Exact-rational finite checks of the capped two-summand tail formula.

This is corroboration, not an exhaustive verification of all real-valued laws.
Run with: python check.py
"""
from fractions import Fraction as F


def sharp(L):
    L = F(L)
    if L < F(3, 2):
        return F(0)
    if L <= 2:
        return 1 / (L * (3 - L))
    t = L - 2
    if 2 * t * t <= 1:
        return F(1, 2)
    if L <= 3:
        return (2 * t + 3 * t * t) / (1 + 2 * t) ** 2
    return F(5, 9)


def mean_one_two_atom(a, b):
    if a == 1 or b == 1:
        assert 0 <= a <= 1 <= b
        return [(F(1), F(1))]
    assert 0 <= a < 1 < b
    return [(a, (b - 1) / (b - a)), (b, (1 - a) / (b - a))]


def event(law_x, law_y):
    return sum((px * py for x, px in law_x for y, py in law_y if x + y >= 3), F(0))


def witness(L):
    L = F(L)
    if L < F(3, 2):
        return [(F(1), F(1))], [(F(1), F(1))]
    if L <= 2:
        return mean_one_two_atom(F(0), L), mean_one_two_atom(F(0), 3 - L)
    t = L - 2
    if 2 * t * t <= 1:
        return mean_one_two_atom(F(1), F(1)), mean_one_two_atom(F(0), F(2))
    u = max(F(0), 3 - min(L, F(3)))
    v = min(L, F(3))
    return mean_one_two_atom(u, v), mean_one_two_atom(u, v)


def main():
    checks = 0
    # Verify every rational two-atom pair on a grid for several cap levels.
    for j in range(5, 21):
        L = F(j, 5)
        support = [F(i, 5) for i in range(j + 1)]
        laws = [mean_one_two_atom(a, b) for a in support if a < 1 for b in support if b > 1]
        laws.append(mean_one_two_atom(F(1), F(1)))
        for p in laws:
            for q in laws:
                assert event(p, q) <= sharp(L), (L, p, q)
                checks += 1
    # Every rational point in the exact, attained branches has an explicit witness.
    for j in range(20, 101):
        L = F(j, 20)
        p, q = witness(L)
        assert event(p, q) == sharp(L), (L, p, q, event(p, q), sharp(L))
        assert all(0 <= x <= L for law in (p, q) for x, _ in law)
        assert all(sum((x * z for x, z in law), F(0)) == 1 for law in (p, q))
        checks += 1
    # Verify the key algebraic comparison H(t,t)-1/2=(2t^2-1)/(2(1+2t)^2).
    for j in range(100):
        t = F(j, 99)
        h = (2 * t + 3 * t*t)/(1+2*t)**2
        assert h - F(1, 2) == (2*t*t-1)/(2*(1+2*t)**2)
        checks += 1
    assert sharp(F(3, 2)) == F(4, 9)
    assert sharp(F(2)) == F(1, 2)
    assert sharp(F(3)) == F(5, 9)
    assert sharp(F(5)) == F(5, 9)
    print(f"PASS {checks} exact-rational checks; analytic proof still required")


if __name__ == "__main__":
    main()
