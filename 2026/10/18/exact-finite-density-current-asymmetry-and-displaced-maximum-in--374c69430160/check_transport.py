"""Exact finite-state and coefficient tests for deformed exclusion transport.

Standard-library only: run with python check_transport.py.
This verifies finite examples, not the quantified analytic theorem.
"""
from fractions import Fraction
from itertools import product


def polynomial_product(factors):
    c = [Fraction(1)]
    for a in factors:
        d = [Fraction(0)] * (len(c) + 1)
        for i, v in enumerate(c):
            d[i] += v
            d[i + 1] += a * v
        c = d
    return c


def t_int(k, t):
    return sum((t ** j for j in range(k)), Fraction(0))


def coefficients(K, L, t):
    one = polynomial_product([t ** j for j in range(K)])
    whole = polynomial_product([t ** j for j in range(K) for _ in range(L)])
    removed_two_base = polynomial_product([Fraction(1)] * (L - 2) +
        [t ** j for j in range(1, K) for _ in range(L)])
    return one, whole, removed_two_base


def canonical_current(K, L, n, t, q):
    _, Z, removed = coefficients(K, L, t)
    return (1 - q) * t_int(K, t) ** 2 * (removed[n - 1] if 1 <= n <= K * L - 1 else 0) / Z[n]


def state_check(K, L, n, t, q):
    one, Z, _ = coefficients(K, L, t)
    states = [s for s in product(range(K + 1), repeat=L) if sum(s) == n]
    weights = {s: prod_fraction(one[a] for a in s) for s in states}
    assert sum(weights.values()) == Z[n]
    incoming_minus_outgoing = {s: Fraction(0) for s in states}
    current = Fraction(0)
    for s in states:
        mass = weights[s]
        for i in range(L):
            j = (i + 1) % L
            a, b = s[i], s[j]
            fw = t_int(a, t) * (t_int(K, t) - t_int(b, t))
            bw = q * t_int(b, t) * (t_int(K, t) - t_int(a, t))
            if i == 0:
                current += mass * (fw - bw)
            for rate, direction in ((fw, 1), (bw, -1)):
                if rate:
                    moved = list(s)
                    moved[i] -= direction
                    moved[j] += direction
                    moved = tuple(moved)
                    incoming_minus_outgoing[s] -= mass * rate
                    incoming_minus_outgoing[moved] += mass * rate
    assert all(v == 0 for v in incoming_minus_outgoing.values())
    assert current / Z[n] == canonical_current(K, L, n, t, q)
    return len(states)


def prod_fraction(xs):
    ans = Fraction(1)
    for x in xs:
        ans *= x
    return ans


def test_all():
    checks = 0
    sizes = ((2, 3), (2, 4), (3, 3), (3, 4), (4, 3))
    for K, L in sizes:
        N = K * L
        for t in (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)):
            for q in (Fraction(0), Fraction(1, 3)):
                for n in range(1, N):
                    state_check(K, L, n, t, q)
                    checks += 1
                    delta = canonical_current(K, L, n, t, q) - canonical_current(K, L, N - n, t, q)
                    expected = (t - 1) * (2 * n - N)
                    assert (delta > 0) - (delta < 0) == (expected > 0) - (expected < 0)
                    checks += 1
            for z in (Fraction(1, 3), Fraction(1), Fraction(7, 3)):
                w = polynomial_product([t ** j for j in range(K)])
                total = sum(w[a] * z ** a for a in range(K + 1))
                mplus = sum(t_int(a, t) * w[a] * z ** a for a in range(K + 1)) / total
                mminus = sum((t_int(K, t) - t_int(a, t)) * w[a] * z ** a for a in range(K + 1)) / total
                assert mplus == t_int(K, t) * z / (1 + z)
                assert mminus == t_int(K, t) / (1 + z)
                checks += 2
                rho = sum(z * t ** j / (1 + z * t ** j) for j in range(K))
                mean_occ = sum(a * w[a] * z ** a for a in range(K + 1)) / total
                assert rho == mean_occ
                checks += 1
    print('Exact finite checks passed:', checks)
    print('Example: K=3, L=4, t=2, q=0, n=8')
    K,L,t,q,n = 3,4,Fraction(2),Fraction(0),8
    print('J_8=',canonical_current(K,L,n,t,q),'J_4=',canonical_current(K,L, K*L-n,t,q))
    print('Grand-canonical peak density=',sum(t**j/(1+t**j) for j in range(K)))

if __name__ == '__main__':
    test_all()
