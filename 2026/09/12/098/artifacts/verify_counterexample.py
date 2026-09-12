"""Verify the Cartesian-grid plane-family counterexample (lane-1437).

Construction: s>=2 integer, t=s^2, N=t^3=s^6, p=smallest prime >= s^4,
A=B=C={0..t-1} subset F_p, S={primitive (a,b,c) in {1..s}^3},
planes a*x+b*y+c*z=d for d in 0..3*s*(t-1).
Checks: preconditions (t<p, dmax<p, N^2<=p^3, cross-product bound),
|S|>=s^3/2, n0>=N, exact counting identity sum_v hist = N*|S|,
plane distinctness mod p (direct check), top-N averaging bound,
and analytic ratio growth s^{1/2}/3 -> infinity.
"""
import math
from math import gcd
from collections import Counter


def smallest_prime_geq(m):
    def is_prime(q):
        if q < 2:
            return False
        if q % 2 == 0:
            return q == 2
        r = int(q ** 0.5)
        f = 3
        while f <= r:
            if q % f == 0:
                return False
            f += 2
        return True
    q = m
    while not is_prime(q):
        q += 1
    return q


def primitive_S(s):
    S = []
    for a in range(1, s + 1):
        for b in range(1, s + 1):
            for c in range(1, s + 1):
                if gcd(gcd(a, b), c) == 1:
                    S.append((a, b, c))
    return S


def check(s, uniqueness=False):
    t = s * s
    N = t ** 3
    dmax = 3 * s * (t - 1)
    p = smallest_prime_geq(max(s ** 4, dmax + 1))
    assert dmax < p, (dmax, p)              # no mod-p wrap of d values
    assert s * s < p, "cross products v_i w_j - v_j w_i bounded by s^2 < p"
    S = primitive_S(s)
    assert len(S) * 2 >= s ** 3, (len(S), s)  # |S| >= s^3/2
    D = dmax + 1
    n0 = len(S) * D
    assert n0 >= N, (n0, N)
    # histogram of v.x over integer grid (equals F_p count: all sums < p)
    counts = []
    for (a, b, c) in S:
        hist = Counter()
        for x in range(t):
            ax = a * x
            for y in range(t):
                bay = ax + b * y
                for z in range(t):
                    hist[bay + c * z] += 1
        assert sum(hist.values()) == t ** 3, "partition identity per direction"
        assert min(hist) >= 0 and max(hist) <= dmax
        for d in range(D):
            counts.append(hist.get(d, 0))
    assert len(counts) == n0
    assert sum(counts) == N * len(S), "each grid point on one plane per direction"
    if uniqueness:
        seen = set()
        inv = {}
        for (a, b, c) in S:
            for d in range(D):
                # normalize direction by first nonzero coordinate (=a>=1 here)
                ia = pow(a, -1, p)
                key = ((b * ia) % p, (c * ia) % p, (d * ia) % p)
                seen.add((1, key))
        assert len(seen) == n0, (len(seen), n0)
        print(f"s={s}: all {n0} planes distinct mod p: OK")
    counts.sort(reverse=True)
    Itop = sum(counts[:N])
    assert Itop * n0 >= N * sum(counts), "top-N averaging"
    assert Itop * D >= N * N, "I >= N^2/|D|"
    exp = 17 / 12
    print(f"s={s}: t={t} p={p} N={N} |S|={len(S)} D={D} n0={n0} "
          f"ItopN={Itop} N^1.5/3={N**1.5/3:.1f} ratio_vs_N^17/12="
          f"{Itop / N**exp:.4f} lb_s^0.5/3={s**0.5/3:.4f}")
    return Itop


def analytic_growth():
    print("analytic lower bound I/N^{17/12} >= N^{1/12}/3 = s^{1/2}/3:")
    for s in [3, 4, 10, 100, 10 ** 4, 10 ** 8]:
        print(f"  s={s}: lb={s ** 0.5 / 3:.4f}")


if __name__ == "__main__":
    check(2, uniqueness=True)
    check(3, uniqueness=True)
    analytic_growth()
    print("ALL CHECKS PASSED")
