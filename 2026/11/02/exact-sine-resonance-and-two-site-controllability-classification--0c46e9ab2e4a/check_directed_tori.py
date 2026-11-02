"""Finite checks for the exact two-dimensional oriented-torus controllability theorem.

Usage: python check_directed_tori.py
Uses standard library and mpmath. The theorem is analytic; this tests finite cases.
"""
from math import gcd
from itertools import combinations
import mpmath as mp

mp.mp.dps = 82
TOL = mp.mpf('1e-65')
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def resonance_pairs(m, n):
    return [(r, s) for r in range(1, (m + 1)//2)
                   for s in range(1, (n + 1)//2)]


def values(m, n, q):
    om = mp.e ** (2j * mp.pi / m)
    on = mp.e ** (2j * mp.pi / n)
    return {(j,k): (1-om**j) + q*(1-on**k)
            for j in range(m) for k in range(n)}


def collide(z, w):
    return abs(z - w) < TOL


def check_pair(m, n, r, s):
    q = mp.sin(2*mp.pi*r/m)/mp.sin(2*mp.pi*s/n)
    e = values(m, n, q)
    pairs = set()
    for (j,k), (h,l) in combinations(e, 2):
        if collide(e[(j,k)], e[(h,l)]):
            pair = tuple(sorted(((j,k), (h,l))))
            pairs.add(pair)
            check((j+h == m and k+l == n), 'collision must be conjugate')
            check(abs(mp.im(e[(j,k)])) < TOL, 'collision eigenvalue must be real')
    expected = set()
    for a,b in resonance_pairs(m,n):
        q2 = mp.sin(2*mp.pi*a/m)/mp.sin(2*mp.pi*b/n)
        if abs(q-q2) < TOL:
            expected.add(tuple(sorted(((a,n-b),(m-a,b)))))
    check(pairs == expected, f'collision discrepancy m={m},n={n},r={r},s={s}: {pairs} vs {expected}')
    check(len(pairs)>0, 'each resonance must produce a collision')
    for a,b in expected:
        # No pair of duplicate modes may have the same first or second frequency.
        check(a[0] != b[0] and a[1] != b[1], 'distinct factors required')
    for du in range(m):
        for dv in range(n):
            control = all(not ((2*a*du)%m == 0 and (2*b*dv)%n == 0) for a,b in resonance_pairs(m,n)
                          if abs(q - mp.sin(2*mp.pi*a/m)/mp.sin(2*mp.pi*b/n)) < TOL)
            mode = all(not collide(mp.e**(4j*mp.pi*(mp.mpf(a*du)/m-mp.mpf(b*dv)/n)), 1)
                       for a,b in resonance_pairs(m,n)
                       if abs(q - mp.sin(2*mp.pi*a/m)/mp.sin(2*mp.pi*b/n)) < TOL)
            check(control == mode, 'placement and modal determinant criterion disagree')
    check(all(not((2*a*1)%m == 0 and (2*b*0)%n == 0) for a,b in resonance_pairs(m,n)),
          'adjacent controllers must work')
    return len(expected)


def main():
    for m in range(3, 26):
        for n in range(3, 26):
            if gcd(m,n) != 1:
                continue
            for (j,h) in combinations(range(m),2):
                for (k,l) in combinations(range(n),2):
                    aligned = ((j+h)*n-(k+l)*m) % (m*n) == 0
                    check(aligned == (j+h == m and k+l == n), 'chord direction modular lemma')
    cases = [(3,5),(4,5),(5,6),(5,7),(7,9),(5,11),(9,11),(7,15),(8,9)]
    samples=0
    for m,n in cases:
        # Uniform rates have a simple spectrum for coprime factors.
        e = values(m,n,mp.mpf(1))
        for v,w in combinations(e.values(),2):
            check(not collide(v,w), 'uniform rate collision')
        for r,s in resonance_pairs(m,n):
            check_pair(m,n,r,s)
            samples += 1
    print('PASS',checks,'deterministic checks across',samples,
          'resonant parameter samples and all coprime pairs through 25')


if __name__ == '__main__':
    main()
