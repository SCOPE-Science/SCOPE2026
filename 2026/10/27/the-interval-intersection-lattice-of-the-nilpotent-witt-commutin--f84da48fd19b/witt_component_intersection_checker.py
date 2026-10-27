#!/usr/bin/env python3
"""Finite-field tests for the Witt nilpotent commuting component-incidence theorem.
Uses prime fields for finite checks; the accompanying proof covers all fields
of characteristic p>3. No external packages or data are required.
"""
from itertools import product
import random


def bracket(f, g, p):
    out = [0] * p
    for a in range(p):
        for b in range(p):
            n = a + b - 1
            if 0 <= n < p:
                out[n] = (out[n] + (b - a) * f[a] * g[b]) % p
    return out


def rank_one_pairs(f, g, start, stop, p):
    """At most rank one for two coefficient rows on [start, stop)."""
    for a in range(start, stop):
        for b in range(a + 1, stop):
            if (f[a] * g[b] - f[b] * g[a]) % p:
                return False
    return True


def component(f, g, i, p):
    if i == 0:
        # Restricted to x^2*k[x]/x^p here: all elements are p-nilpotent.
        return rank_one_pairs(f, g, 2, p, p)
    return (all(f[t] == g[t] == 0 for t in range(i + 1))
            and rank_one_pairs(f, g, i + 1, p - i, p))


def test_p5():
    p = 5
    elements = [(0, 0, *v) for v in product(range(p), repeat=3)]
    cnt_one = cnt_both = cnt_comm = 0
    for f in elements:
        for g in elements:
            in0, in1 = component(f, g, 0, p), component(f, g, 1, p)
            iscomm = not any(bracket(f, g, p))
            assert iscomm == (in0 or in1)
            cnt_one += in1
            cnt_both += in0 and in1
            cnt_comm += iscomm
    assert cnt_one == p**2*(1+(p**2-1)*(p+1))
    assert cnt_both == 1+(p**3-1)*(p+1)
    assert cnt_comm == cnt_one # All g1 commuting pairs comprise C1.
    print('p=5: exhaustive 15625 ordered pairs in g1^2:',
          'component=', cnt_one, 'intersection-with-C0=', cnt_both)


def test_random(p, trials=30000):
    rng = random.Random(916331 + p)
    m = (p-3)//2
    for _ in range(trials):
        f = tuple([0, 0] + [rng.randrange(p) for _ in range(p-2)])
        g = tuple([0, 0] + [rng.randrange(p) for _ in range(p-2)])
        comm = not any(bracket(f, g, p))
        inunion = any(component(f, g, i, p) for i in range(1, m+1))
        assert comm == inunion, (p, f, g)
    # Force samples on each irreducible component, since sparse commuting
    # pairs would be missed by purely uniform random sampling.
    for i in range(1, m+1):
        for _ in range(1500):
            f = [0]*(i+1)+[rng.randrange(p) for _ in range(p-i-1)]
            a = rng.randrange(p)
            g = [a*v % p for v in f]
            for k in range(p-i, p):
                g[k] = (g[k]+rng.randrange(p))%p
            assert component(f,g,i,p)
            assert not any(bracket(f,g,p))
    print(f'p={p}: {trials} random pairs and {1500*m} generated component pairs OK')


if __name__ == '__main__':
    test_p5()
    for prime in (7, 11):
        test_random(prime)
    print('WITT_INTERSECTIONS_OK')
