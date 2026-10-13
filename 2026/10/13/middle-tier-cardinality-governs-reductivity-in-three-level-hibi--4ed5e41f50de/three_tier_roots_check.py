"""Exact bounded Demazure-root regression for three-tier order polytopes.

The theorem is proved symbolically; bounded character boxes do not prove exhaustiveness
for arbitrary parameters. Requires only Python 3 standard library.
"""
from itertools import product


def verify(a: int, c: int, b: int, bound: int = 2):
    assert a >= 2 and b >= 2 and c >= 1
    n = a + c + b
    A, C, B = tuple(range(a)), tuple(range(a, a + c)), tuple(range(a + c, n))
    rays = []
    for u in A:
        rays.append((('lower', u), ((u, -1),)))
    for w in B:
        rays.append((('upper', w), ((w, 1),)))
    for u in A:
        for v in C:
            rays.append((('lowmiddle', u, v), ((u, 1), (v, -1))))
    for v in C:
        for w in B:
            rays.append((('middlehigh', v, w), ((v, 1), (w, -1))))
    got = set()
    for m in product(range(-bound, bound + 1), repeat=n):
        unique = -1
        valid = True
        for j, (_, ray) in enumerate(rays):
            s = sum(m[i] * d for i, d in ray)
            if s == -1:
                if unique != -1:
                    valid = False
                    break
                unique = j
            elif s < 0:
                valid = False
                break
        if valid and unique != -1:
            got.add(m)
    expected = set()
    for u in A:
        s = [0] * n; s[u] = 1; expected.add(tuple(s))
        if c == 1:
            s[u] = -1; expected.add(tuple(s))
    for w in B:
        s = [0] * n; s[w] = -1; expected.add(tuple(s))
        if c == 1:
            s[w] = 1; expected.add(tuple(s))
    assert got == expected, (a, c, b, got - expected, expected - got)
    return (a, c, b, len(rays), len(got), (n + len(got)))


if __name__ == '__main__':
    triples = (
        (2, 1, 2), (2, 2, 2), (2, 3, 2),
        (2, 1, 3), (3, 1, 2), (3, 1, 3),
        (3, 2, 2), (2, 2, 3), (2, 1, 4),
        (4, 1, 2),
    )
    for abc in triples:
        print('PASS a,c,b=%s,%s,%s rays=%s roots=%s Aut_dimension=%s' % verify(*abc))
    print('PASS all 10 three-tier regressions in character box [-2,2]^n')
