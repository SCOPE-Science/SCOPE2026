#!/usr/bin/env python3
"""Direct finite checks for orbit formulas of End(T_n), n >= 5.
Only Python standard library is required.  This script enumerates finite maps
and uses the published (t,e) structural classification; it does not assume
any of the proposed multiset or plane-partition formulae.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial


def euler_product(exponents, N):
    """First N coefficients of product (1-z^k)^(-exponents[k])."""
    assert len(exponents) == N + 1 and exponents[0] == 0
    divisor_sums = [0] * (N + 1)
    for n in range(1, N + 1):
        divisor_sums[n] = sum(k * exponents[k] for k in range(1, n + 1) if n % k == 0)
    coeffs = [1] + [0] * N
    for n in range(1, N + 1):
        numerator = sum(divisor_sums[k] * coeffs[n-k] for k in range(1, n + 1))
        assert numerator % n == 0
        coeffs[n] = numerator // n
    return coeffs


def predicted(N):
    partitions = euler_product([0] + [1] * N, N)
    h = euler_product([0] + [1 + n // 2 for n in range(1, N + 1)], N)
    R = [0] + [sum(h[:n]) for n in range(1, N + 1)]
    R0 = [0] + [sum(partitions[:n]) for n in range(1, N + 1)]
    full = euler_product(R, N)
    without_2cycles = euler_product(R0, N)
    r3 = [full[i] - without_2cycles[i] for i in range(N + 1)]
    plane = euler_product([0] + list(range(1, N + 1)), N)
    r2 = [plane[i] - partitions[i] for i in range(N + 1)]
    return r3, r2, partitions, plane


def compatible_pairs(n):
    """Directly enumerate solutions t^3=t and e^2=e=te=et on [n]."""
    V = range(n)
    for t in product(V, repeat=n):
        t2 = tuple(t[t[i]] for i in V)
        if any(t[t2[i]] != t[i] for i in V):
            continue
        fixed = [i for i in V if t[i] == i]
        if not fixed:
            continue
        # Construct connected components of the directed functional graph of t.
        parent = list(V)
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        for i in V:
            parent[find(i)] = find(t[i])
        components = {}
        for i in V:
            components.setdefault(find(i), []).append(i)
        components = list(components.values())
        for mask in range(1, 1 << len(fixed)):
            roots = {fixed[j] for j in range(len(fixed)) if mask & (1 << j)}
            choices = []
            for comp in components:
                local = roots.intersection(comp)
                choices.append(tuple(local) if local else tuple(sorted(roots)))
            for chosen in product(*choices):
                e = [None] * n
                for comp, target in zip(components, chosen):
                    for i in comp:
                        e[i] = target
                e = tuple(e)
                assert all(e[e[i]] == e[i] and e[t[i]] == e[i] and t[e[i]] == e[i] for i in V)
                yield t, e, t2


def canonical(t, e):
    n = len(t)
    best = None
    for p in permutations(range(n)):
        tnew, enew = [0] * n, [0] * n
        for i in range(n):
            tnew[p[i]] = p[t[i]]
            enew[p[i]] = p[e[i]]
        code = tuple(tnew) + tuple(enew)
        if best is None or code < best:
            best = code
    return best


def direct_orbit_counts(n):
    records = list(compatible_pairs(n))
    lift_squares = {(t2, e) for t, e, t2 in records if t2 != t}
    rank3 = set()
    essential_rank2 = set()
    for t, e, t2 in records:
        if t2 != t:
            rank3.add(canonical(t, e))
        elif t != e and (t, e) not in lift_squares:
            essential_rank2.add(canonical(t, e))
    return len(rank3), len(essential_rank2), len(records)


def partitions_of(n, minimum=1):
    if not n:
        yield ()
    for v in range(minimum, n+1):
        for tail in partitions_of(n-v, v):
            yield (v,) + tail


def representative_and_size(parts):
    n = sum(parts)
    p = list(range(n))
    start = 0
    for length in parts:
        for j in range(length):
            p[start+j] = start + (j+1) % length
        start += length
    counts = Counter(parts)
    z = 1
    for length, count in counts.items():
        z *= length**count * factorial(count)
    return tuple(p), factorial(n)//z


def fixed(t, e, p):
    return all(t[p[i]] == p[t[i]] and e[p[i]] == p[e[i]] for i in range(len(p)))


def burnside(n):
    """Genuinely different check: conjugacy-type Burnside, not canonicalization."""
    records = list(compatible_pairs(n))
    lift_squares = {(t2, e) for t, e, t2 in records if t2 != t}
    rank3 = [(t,e) for t,e,t2 in records if t2 != t]
    rank2 = [(t,e) for t,e,t2 in records if t2 == t and t != e and (t,e) not in lift_squares]
    sums = [0,0]
    for part in partitions_of(n):
        rep,size = representative_and_size(part)
        for j, category in enumerate((rank3,rank2)):
            sums[j] += size * sum(fixed(t,e,rep) for t,e in category)
    assert all(s % factorial(n) == 0 for s in sums)
    return tuple(s//factorial(n) for s in sums), len(records)


def main():
    N=20
    r3,r2,parts,planes = predicted(N)
    expected_rank3 = [15,46,133,362,951,2419]
    expected_rank2 = [17,37,71,138,252,458]
    assert r3[5:11] == expected_rank3
    assert r2[5:11] == expected_rank2
    # All admissible pairs, and all possible square lifts, enumerated independently.
    for n in (3,4,5):
        actual3, actual2, total = direct_orbit_counts(n)
        assert (actual3,actual2) == (r3[n],r2[n]), (n,actual3,actual2)
        print('DIRECT_ORBITS_OK', n, 'pairs',total,'rank3',actual3,'rank2_not_a_square_lift',actual2)
    (actual3,actual2),total=burnside(6)
    assert (actual3,actual2) == (r3[6],r2[6])
    print('BURNSIDE_OK',6,'pairs',total,'rank3',actual3,'essential_rank2',actual2)
    print('MINIMAL_GENERATOR_COUNTS',[(n,3+r3[n]+r2[n]) for n in range(5,11)])
    print('VERIFY_OK')

if __name__=='__main__':main()
