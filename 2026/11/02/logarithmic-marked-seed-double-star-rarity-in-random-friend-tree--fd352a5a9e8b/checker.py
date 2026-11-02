#!/usr/bin/env python3
"""Reproduce finite exact checks for seed-edge double stars in friend trees."""
from fractions import Fraction as F
from collections import defaultdict
from math import fsum, log

checks = 0

def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1

def split_law(nmax):
    """Exact subprobability distribution for attachments only to the seed pair."""
    p = {(0, 0): F(1)}
    output = {2: p}
    for n in range(2, nmax):
        q = defaultdict(F)
        for (a, b), mass in p.items():
            q[a + 1, b] += mass * (F(a) + F(1, b + 1)) / n
            q[a, b + 1] += mass * (F(b) + F(1, a + 1)) / n
        p = dict(q)
        output[n + 1] = p
    return output

def full_law(nmax):
    """Independent enumeration of every labelled attachment history."""
    p = {(0, 1): F(1)}  # parent list, 1-based with vertex 1 having parent 0
    output = {2: p}
    for n in range(2, nmax):
        q = defaultdict(F)
        for parents, mass in p.items():
            adj = {j: [] for j in range(1, n + 1)}
            for j in range(2, n + 1):
                w = parents[j - 1]
                adj[j].append(w)
                adj[w].append(j)
            for v in range(1, n + 1):
                for w in adj[v]:
                    q[parents + (w,)] += mass * F(1, n * len(adj[v]))
        p = dict(q)
        check(sum(p.values()) == 1, f"full-law normalization n={n+1}")
        output[n + 1] = p
    return output


def star_probability(n, p):
    if n == 2:
        return F(1)
    return p.get((n - 2, 0), F(0)) + p.get((0, n - 2), F(0))

law = split_law(35)
full = full_law(8)
for n in range(3, 9):
    p = law[n]
    r = full[n]
    tagged = defaultdict(F)
    star = F(0)
    for parents, mass in r.items():
        if all(w in (1, 2) for w in parents[2:]):
            a = sum(w == 1 for w in parents[2:])
            b = n - 2 - a
            tagged[a, b] += mass
        adj = {j: 0 for j in range(1, n + 1)}
        for j in range(2, n + 1):
            adj[j] += 1
            adj[parents[j - 1]] += 1
        if max(adj.values()) == n - 1:
            star += mass
    for a in range(n - 1):
        b = n - 2 - a
        check(tagged[(a, b)] == p.get((a, b), F(0)), f"independent marked mass n={n} a={a}")
    check(star == star_probability(n, p), f"independent star event n={n}")
    check(star == F(2, n - 1), f"star probability n={n}")

for n in range(4, 36):
    p = law[n]
    both = sum(v for (a, b), v in p.items() if a >= 1 and b >= 1)
    harmonic = sum((F(1, j) for j in range(2, n - 1)), F(0))
    lower = 2 * harmonic / ((n - 1) * (n - 2))
    check(both >= lower, f"finite lower bound n={n}")
    check(both > 0, f"strict positive n={n}")
    check(sum(p.values()) == F(2, n - 1) + both, f"boundary decomposition n={n}")

# The exact harmonic supersolution is checked on a finite grid. Its general
# validity follows algebraically from the stated g recurrence.
M = 65
g = {M+1: F(1)}
for j in range(M, 0, -1):
    g[j] = g[j+1] / (1 - F(1, j * (j + 1)))
for a in range(1, 25):
    for b in range(1, 25):
        m = a + b + 2
        p1 = (F(a) + F(1, b+1)) / m
        p2 = (F(b) + F(1, a+1)) / m
        h = g[a]*g[b]
        left = p1*g[a+1]*g[b] + p2*g[a]*g[b+1]
        check(left <= (1-F(2,m))*h, f"supersolution a={a} b={b}")

# Non-exhaustive numerical asymptotic probe, distinct from the analytic proof.
p = {0: 1.0}
for n in range(2, 601):
    if n in (100, 300, 600):
        mass = fsum(v for a,v in p.items() if 0 < a < n-2)
        ratio = mass*n*n/log(n)
        check(2.0 < ratio < 6.8, f"asymptotic window n={n}")
    q = defaultdict(float)
    for a,v in p.items():
        b = n-2-a
        q[a+1] += v*(a+1/(b+1))/n
        q[a] += v*(b+1/(a+1))/n
    p = dict(q)

print(f"PASS: {checks} exact comparisons, rational inequalities, and asymptotic probes")
