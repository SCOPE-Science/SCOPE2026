"""Exact finite checks for the cocktail-party transportation-ball facet incidence theorem.

Run with Python 3.10+; requires only the standard library. No external inputs.
"""
from collections import Counter, deque
from itertools import product
from math import comb, factorial
from fractions import Fraction


def edges_of_graph(m):
    return [(i, j) for i in range(2*m) for j in range(i+1, 2*m)
            if i//2 != j//2]


def directly_enumerate_facets(m):
    """Use integer dual potentials and a graph-connectivity rank test, not orbit formulas."""
    n = 2*m
    edges = edges_of_graph(m)
    out = {}
    for f in product((0, 1, 2), repeat=n):
        if min(f) != 0 or max(f) == 0:
            continue
        if any(abs(f[i]-f[j]) > 1 for i, j in edges):
            continue
        adj = [[] for _ in range(n)]
        incidence = 0
        for i, j in edges:
            if abs(f[i]-f[j]) == 1:
                adj[i].append(j)
                adj[j].append(i)
                incidence += 1
        visited = {0}
        queue = deque([0])
        while queue:
            for j in adj[queue.popleft()]:
                if j not in visited:
                    visited.add(j)
                    queue.append(j)
        if len(visited) == n:
            out[f] = incidence
    return out


def predicted_incidence_polynomial(m):
    hist = Counter()
    for a in range(m+1):
        for b in range(m-a+1):
            c = m-a-b
            # Constants and singleton/complement-singleton potentials are not vertices.
            if (a == m and b == c == 0) or (b == m and a == c == 0):
                continue
            if (a == m-1 and b == 0 and c == 1) or \
               (b == m-1 and a == 0 and c == 1):
                continue
            weight = factorial(m)//(factorial(a)*factorial(b)*factorial(c))*2**c
            hist[m*m-(a-b)**2-c] += weight
    hist[4*m-4] += 2*m
    return +hist


def generators(f, m):
    for pair in range(m):
        w = list(f)
        i = 2*pair
        w[i], w[i+1] = w[i+1], w[i]
        yield tuple(w)
    for pair in range(m-1):
        w = list(f)
        i = 2*pair
        w[i:i+4] = w[i+2:i+4] + w[i:i+2]
        yield tuple(w)
    top = max(f)
    yield tuple(top-x for x in f)


def brute_orbit_sizes(facets, m):
    rest = set(facets)
    sizes = []
    while rest:
        first = rest.pop()
        orbit = {first}
        queue = deque([first])
        while queue:
            for nxt in generators(queue.popleft(), m):
                assert nxt in facets
                if nxt not in orbit:
                    orbit.add(nxt)
                    queue.append(nxt)
        rest.difference_update(orbit)
        sizes.append(len(orbit))
    return sorted(sizes)


def predicted_orbit_sizes(m):
    out = [2*m]   # The unique three-level orbit.
    for a in range(m+1):
        for b in range(a, m-a+1):
            c = m-a-b
            if (a == 0 and b == m and c == 0) or \
               (a == 0 and b == m-1 and c == 1):
                continue
            size = factorial(m)//(factorial(a)*factorial(b)*factorial(c))
            size *= 2**c*(1 if a == b else 2)
            out.append(size)
    return sorted(out)


def verify(m):
    actual = directly_enumerate_facets(m)
    hist_actual = +Counter(actual.values())
    hist_predicted = predicted_incidence_polynomial(m)
    assert hist_actual == hist_predicted, (m, hist_actual, hist_predicted)
    F = 4**m-2*m-2
    assert len(actual) == F == sum(hist_predicted.values())
    assert brute_orbit_sizes(actual, m) == predicted_orbit_sizes(m)
    orbit_formula = (comb(m+2, 2) + (m//2)+1)//2 - 1
    assert len(predicted_orbit_sizes(m)) == orbit_formula
    S1 = sum(j*k for j, k in hist_actual.items())
    S2 = sum(j*j*k for j, k in hist_actual.items())
    target1 = m*(m-1)*4**m
    target2 = 4**m*(m*m*(m-1)**2 + Fraction(m*(m-1), 2)) + 16*m*(m-1)**2
    assert S1 == target1
    assert S2 == target2
    maximum = m*m-(m%2)
    assert max(actual.values()) == maximum
    if m % 2 == 0:
        maxcount = comb(m, m//2)
    else:
        maxcount = 2*comb(m, (m-1)//2) + 2*m*comb(m-1, (m-1)//2)
        if m == 3:
            maxcount += 2*m
    assert hist_actual[maximum] == maxcount
    print(f'm={m}: facets={F}, orbits={orbit_formula}, max_incidence={maximum}, '
          f'max_facets={maxcount}, distribution={sorted(hist_actual.items())}')


if __name__ == '__main__':
    for m in (3, 4, 5, 6):
        verify(m)
    print('ALL EXACT FACET, ORBIT, INCIDENCE, AND MOMENT CHECKS PASSED')
