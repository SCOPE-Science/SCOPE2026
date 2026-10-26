#!/usr/bin/env python3
"""Exact, independent shortest-path checks of the Apéry and gap formulas."""
from heapq import heappush, heappop

def ap(m, generators):
    distances = [10**100] * m
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        w, r = heappop(queue)
        if w != distances[r]:
            continue
        for generator in generators:
            s = (r + generator) % m
            if w + generator < distances[s]:
                distances[s] = w + generator
                heappush(queue, (w + generator, s))
    return distances

def coin(x, c, d):
    k, s = divmod(x, d)
    q, r = divmod(s, c)
    return k + q + r

cases = 0
for b in range(2, 18):
    c = b - 1
    d = c*c + c + 1
    m = c*(c*c + 2*c + 2)
    U = [0, 1]
    for n in range(2, 13):
        U.append((b-1)*U[-1] + b*U[-2])
    assert (U[2], U[3], U[4]) == (c, d, m)
    generators = sorted({m, m+1, m+c, m+d})
    for n in range(13):
        assert (m+U[n]) % m in {v % m for v in generators} or n > 3
        if n >= 4:
            t = n - 4
            assert m + U[n] == b*U[t]*(m+d) + (1+(-1)**t)*m
    distances = ap(m, generators)
    assert distances == [coin(x, c, d)*m + x for x in range(m)]
    genus = sum(w//m for w in distances)
    expected_genus = (d*c*(c+1) + (c+1)**2*(2*c*c-c+2))//2 - (2*c+1)
    assert genus == expected_genus
    assert max(distances) - m == (3*c-1)*m-1
    pf = sorted(w-m for r,w in enumerate(distances)
                if r and all(w+g-m >= distances[(r+g)%m] for g in generators))
    expected_pf = sorted(((2*c-1)*m+c*d-1, (3*c-1)*m-1))
    assert pf == expected_pf, (b,pf,expected_pf)
    for x in range(3*m):
        assert coin(x+m,c,d) >= coin(x,c,d)+c
    cases += 1
print(f"PASS: {cases} parameter sets, all Apéry residues, genus, Frobenius, PF and shift tests")
