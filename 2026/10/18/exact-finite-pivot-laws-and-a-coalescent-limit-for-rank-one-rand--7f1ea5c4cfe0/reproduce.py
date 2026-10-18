"""Exact-arithmetic and Monte Carlo checks for rank-one Jacobi pivot stopping laws.

Run: python reproduce.py (Python 3.10+ standard library only).
This program tests finite cases and identities, not the infinite-dimensional limit proof.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, hypot, pi
from random import Random


def expected_steps(n: int, block: int, initial_support: int) -> Fraction:
    assert 2 <= block <= n and 1 <= initial_support <= n
    e = [Fraction(0)] * (initial_support + 1)
    for s in range(2, initial_support + 1):
        q_success = Fraction(0)
        weighted_lower = Fraction(0)
        for r in range(2, min(block, s) + 1):
            if block - r > n - s:
                continue
            p = Fraction(comb(s, r) * comb(n - s, block - r), comb(n, block))
            q_success += p
            weighted_lower += p * e[s - r + 1]
        assert q_success > 0
        e[s] = (1 + weighted_lower) / q_success
    return e[initial_support]


def simulate_steps(n: int, block: int, seed: int, reps: int) -> float:
    rng = Random(seed)
    total = 0
    for _ in range(reps):
        active = list(range(n))
        count = 0
        while len(active) > 1:
            subset = set(rng.sample(range(n), block))
            selected = [j for j in active if j in subset]
            if len(selected) >= 2:
                survivors = selected[0]
                active = [j for j in active if j not in subset or j == survivors]
            count += 1
        total += count
    return total / reps


def check_rotation(v: list[float], i: int, j: int, rho: float, lam: float) -> None:
    n = len(v)
    assert i < j and v[i] != 0 and v[j] != 0
    h = hypot(v[i], v[j]); c = v[i]/h; s = v[j]/h
    Q = [[float(i == j) for j in range(n)] for i in range(n)]
    Q[i][i] = c; Q[j][i] = s
    Q[i][j] = -s; Q[j][j] = c
    B = [[lam * float(a == b) + rho * v[a] * v[b] for b in range(n)] for a in range(n)]
    rotated = [[sum(Q[a][u] * B[a][b] * Q[b][w] for a in range(n) for b in range(n)) for w in range(n)] for u in range(n)]
    vv = [sum(Q[a][u]*v[a] for a in range(n)) for u in range(n)]
    target = [[lam*float(u == w)+rho*vv[u]*vv[w] for w in range(n)] for u in range(n)]
    assert abs(vv[j]) < 1e-12
    assert abs(vv[i]) > 0
    assert max(abs(rotated[u][w]-target[u][w]) for u in range(n) for w in range(n)) < 1e-11


def main() -> None:
    checked = 0
    for n in range(2, 19):
        for support in range(1, n+1):
            e = expected_steps(n, 2, support)
            assert e == Fraction(n*(n-1)*(support-1), support)
            checked += 1
        for block in range(2, n+1):
            assert expected_steps(n, block, 1) == 0
            assert expected_steps(n, n, n) == 1
            assert expected_steps(n, block, n) <= (n-1)**2
            checked += 3
        if n >= 3:
            assert expected_steps(n, n-1, n) <= expected_steps(n, 2, n)
            checked += 1
    for v in [[1,2,3], [0.2,-0.5,1.5,2.0], [1.0,-2.0,0.0,3.0,4.0]]:
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                if v[i] and v[j]:
                    for rho, lam in [(.2,2.0),(-.01,2.0)]:
                        check_rotation(v,i,j,rho,lam)
                        checked += 1
    # Variance formula from independent geometric stages.
    for n in range(2, 20):
        ps = [Fraction(k*(k-1),n*(n-1)) for k in range(2,n+1)]
        var = sum((1-p)/p**2 for p in ps)
        explicit = (n*(n-1))**2 * sum(Fraction(1,k*k*(k-1)*(k-1)) for k in range(2,n+1)) - (n-1)**2
        assert var == explicit
        checked += 1
    rng = Random(42)
    for n in [4,6,9]:
        for block in [2,3,n]:
            if block > n: continue
            empirical = simulate_steps(n,block,rng.randrange(2**31),6000)
            exact = float(expected_steps(n,block,n))
            # Sampling tolerance intentionally conservative; this is not a proof.
            assert abs(empirical-exact) < max(1.5,.12*exact), (n,block,empirical,exact)
            print(f'n={n}, block={block}: mean samples {empirical:.5f}, exact {exact:.5f}')
            checked += 1
    print(f'PASS: {checked} exact/numeric structural checks; variance limit {pi*pi/3-3:.12f}')

if __name__ == '__main__':
    main()
