"""Exact rational coefficient and path-state checks for walk maximum/local time."""
from fractions import Fraction as F
from math import comb
from collections import defaultdict


def convol(a, b, n):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[:n + 1 - i]):
            if y:
                out[i + j] += x * y
    return out


def series_formula(n):
    # P(S_j = 0) and E[z^{tau_1}] are the central-binomial and Catalan series.
    u = [F(0)] * (n + 1)
    r = [F(0)] * (n + 1)
    for k in range(n // 2 + 1):
        u[2 * k] = F(comb(2 * k, k), 4 ** k)
        if 2 * k + 1 <= n:
            r[2 * k + 1] = F(comb(2 * k, k), (k + 1) * (2 ** (2 * k + 1)))

    # r/(1-r) + r^2/(1-r^2) - r^3/(1-r^3), expanded to order n.
    q = [F(0)] * (n + 1)
    g = [F(0)] * (n + 1)
    power = [F(1)] + [F(0)] * n
    for k in range(1, n + 1):
        power = convol(power, r, n)
        for j in range(n + 1):
            q[j] += power[j]
            if k % 2 == 0:
                g[j] += power[j]
            if k % 3 == 0:
                g[j] -= power[j]
    ug = convol(u, [x + y for x, y in zip(q, g)], n)
    numerator = [x - y for x, y in zip(ug, q)]
    mixed = [sum(numerator[:k + 1]) for k in range(n + 1)]
    first = [sum(u[1:k + 1]) for k in range(n + 1)]
    uless = [x - (i == 0) for i, x in enumerate(u)]
    sq_numer = convol(uless, [2 * x - (i == 0) for i, x in enumerate(u)], n)
    second = [sum(sq_numer[:k + 1]) for k in range(n + 1)]
    return mixed, first, second


def enumerate_paths(n):
    states = {(0, 0, 0): 1}
    out = [(F(0), F(0), F(0), F(0))]
    for step in range(1, n + 1):
        next_states = defaultdict(int)
        for (pos, top, visits), count in states.items():
            for inc in (-1, 1):
                nxt = pos + inc
                next_states[(nxt, max(top, nxt), visits + (nxt == 0))] += count
        states = next_states
        scale = 2 ** step
        out.append((
            F(sum(c * m * l for (_, m, l), c in states.items()), scale),
            F(sum(c * m for (_, m, l), c in states.items()), scale),
            F(sum(c * l for (_, m, l), c in states.items()), scale),
            F(sum(c * l * l for (_, m, l), c in states.items()), scale),
        ))
    return out


def verify(n=16):
    exact = enumerate_paths(n)
    mixed, first, second = series_formula(n)
    for i, ((dmix, dmax, dloc, dloc2), gmix, gloc, gloc2) in enumerate(zip(exact, mixed, first, second)):
        assert (dmix, dloc, dloc2) == (gmix, gloc, gloc2), (i, dmix, gmix, dloc, gloc, dloc2, gloc2)
        if i in (2, 4, 8, 12, 16):
            print(f'n={i}: E[M*L]={dmix}, E[L]={dloc}, E[L^2]={dloc2}, cov={dmix-dmax*dloc}')
    print(f'PASS: all three generating-function coefficient identities agree with independent path-state enumeration, n=0..{n}.')

if __name__ == '__main__':
    verify()
