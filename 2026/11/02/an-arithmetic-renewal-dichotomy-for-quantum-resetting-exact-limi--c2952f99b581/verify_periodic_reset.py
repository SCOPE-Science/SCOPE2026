"""Finite diagnostics for arithmetic-renewal quantum reset phase cycles.

The universal theorem relies on the discrete renewal theorem and the
unit-circle noncancellation proof, not on these finite diagnostics.
"""
import cmath
import math
from fractions import Fraction


def finite_cycle_pmf(law, steps):
    """Return exact renewal-age probability at every integer update."""
    ages = {0: Fraction(1)}
    distributions = [dict(ages)]
    surv = {}
    for a in range(max(law) + 1):
        s = sum(p for n, p in law.items() if n > a)
        surv[a] = s
    for _ in range(steps):
        nxt = {}
        for a, p_age in ages.items():
            s = surv[a]
            if s == 0:
                raise AssertionError("nonexistent age")
            reset = law.get(a + 1, Fraction(0)) / s
            nxt[0] = nxt.get(0, Fraction(0)) + p_age * reset
            nxt[a + 1] = nxt.get(a + 1, Fraction(0)) + p_age * (1 - reset)
        ages = {a: p for a, p in nxt.items() if p}
        assert sum(ages.values()) == 1
        distributions.append(dict(ages))
    return distributions


def predicted(law, phase):
    d = math.gcd(*law)
    mean = sum(Fraction(n) * p for n, p in law.items())
    assert 0 <= phase < d
    return {a: Fraction(d, 1) / mean * sum(p for n, p in law.items() if n > a)
            for a in range(phase, max(law), d)
            if any(n > a for n in law)}


def offtheta(ages, theta):
    # Offdiagonal of an initial |+><+| state after phase gate diag(1,e^{i theta}).
    return sum(float(p) * cmath.exp(-1j * theta * age) / 2
               for age, p in ages.items())


def run():
    checks = 0
    # Exact benchmark: L=2 or 4 equally likely, mean=3, span=2.
    law = {2: Fraction(1, 2), 4: Fraction(1, 2)}
    assert predicted(law, 0) == {0: Fraction(2, 3), 2: Fraction(1, 3)}
    assert predicted(law, 1) == {1: Fraction(2, 3), 3: Fraction(1, 3)}
    checks += 2
    states = finite_cycle_pmf(law, 240)
    for t in range(100, 241):
        p = predicted(law, t % 2)
        tv = sum(abs(states[t].get(a, 0) - p.get(a, 0)) for a in set(p) | set(states[t])) / 2
        assert float(tv) < 1e-12, (t, tv)
        checks += 1
    theta = math.pi / 2
    even = offtheta(predicted(law, 0), theta)
    odd = offtheta(predicted(law, 1), theta)
    assert abs(even - 1/6) < 1e-12
    assert abs(odd + 1j/6) < 1e-12
    assert abs(2 * abs(odd-even) - math.sqrt(2)/3) < 1e-12
    checks += 3

    # Several random genuinely arithmetic renewal clocks (including aperiodic)
    # confirm the stationary-age predictions, while retaining a nontrivial phase.
    laws = [
        {1: Fraction(1, 3), 3: Fraction(2, 3)},
        {2: Fraction(1, 3), 6: Fraction(2, 3)},
        {3: Fraction(2, 5), 9: Fraction(3, 5)},
        {4: Fraction(1, 2), 12: Fraction(1, 2)},
        {2: Fraction(2, 5), 4: Fraction(1, 5), 6: Fraction(2, 5)},
        {3: Fraction(1, 5), 6: Fraction(2, 5), 12: Fraction(2, 5)},
        {1: Fraction(2, 5), 2: Fraction(3, 5)},
    ]
    for law in laws:
        d = math.gcd(*law)
        for j in range(d):
            p = predicted(law, j)
            assert sum(p.values()) == 1, (law, j, p)
            checks += 1
        traj = finite_cycle_pmf(law, 600)
        for t in range(550, 601):
            p = predicted(law, t % d)
            tv = sum(abs(traj[t].get(a, 0) - p.get(a, 0)) for a in set(p) | set(traj[t])) / 2
            assert float(tv) < 1e-10, (law, t, float(tv))
            checks += 1
        nu = sum(Fraction(n, d) * prob for n, prob in law.items())
        k_law = {n // d: prob for n, prob in law.items()}
        for k in range(0, 99):
            z = cmath.exp(2j * math.pi * k / 99)
            direct = sum(float(sum(prob for n, prob in k_law.items() if n > a))
                         * z**a for a in range(max(k_law))) / float(nu)
            if abs(z-1) > 1e-8:
                closed = (1-sum(float(p)*z**n for n,p in k_law.items())) / ((1-z)*float(nu))
                assert abs(closed-direct) < 1e-10
            assert abs(direct) > 1e-6, (law,k, direct)
            checks += 1
    print(f"PASS {checks} finite diagnostics; exact sample trace-distance amplitude sqrt(2)/3")


if __name__ == '__main__':
    run()
