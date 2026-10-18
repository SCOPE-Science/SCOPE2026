#!/usr/bin/env python3
"""Finite-field checks for the rank-one niltriangular commuting-tuple theorem.

All rank checks use literal 2x2 minors of 4x4 matrices.  All commutation
checks use literal matrix products.  F_4 is implemented via T^2+T+1.
"""
from itertools import product

POSITIONS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q

    def add(self, a, b):
        return (a ^ b) if self.q == 4 else ((a + b) % self.q)

    def sub(self, a, b):
        return (a ^ b) if self.q == 4 else ((a - b) % self.q)

    def mul(self, a, b):
        if self.q != 4:
            return a * b % self.q
        v = 0
        while b:
            if b & 1:
                v ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7
        return v


def matrix(z):
    m = [[0] * 4 for _ in range(4)]
    for (i, j), value in zip(POSITIONS, z):
        m[i][j] = value
    return m


def rank_at_most_one(z, f):
    m = matrix(z)
    for r in range(4):
        for s in range(r + 1, 4):
            for i in range(4):
                for j in range(i + 1, 4):
                    if f.sub(f.mul(m[r][i], m[s][j]),
                             f.mul(m[r][j], m[s][i])) != 0:
                        return False
    return True


def commute(a, b, f):
    x, y = matrix(a), matrix(b)
    for i in range(4):
        for j in range(4):
            ab = ba = 0
            for k in range(4):
                ab = f.add(ab, f.mul(x[i][k], y[k][j]))
                ba = f.add(ba, f.mul(y[i][k], x[k][j]))
            if ab != ba:
                return False
    return True


def predicted_count(q, t):
    return (q ** t * (2 * q ** (2 * t) + (q + 1) * (2*q - 1) ** t
                      - 2 * (q + 1) * q ** t + q)
            + (q**3 + q**2 - q) ** t - (2*q**2 - q) ** t)


def line_list(q, f):
    lines = []
    for x, y in product(range(q), repeat=2):
        if (x, y) == (0, 0):
            continue
        if any(f.sub(f.mul(x, v), f.mul(y, u)) == 0
               for u, v in lines):
            continue
        lines.append((x, y))
    assert len(lines) == q + 1
    return lines


def component_memberships(tup, f, lines):
    t = len(tup)
    if all(z[3] == z[4] == z[5] == 0 for z in tup):
        yield 'L'
    if all(z[0] == z[1] == z[3] == 0 for z in tup):
        yield 'R'
    if all(z[0] == z[5] == 0 for z in tup):
        yield 'D'
    if any(z[3] for z in tup):
        return
    for mask in range(1, 2**t - 1):
        if any((z[4] or z[5]) if mask & (1 << i) else (z[0] or z[1])
               for i, z in enumerate(tup)):
            continue
        for u, v in lines:
            # L vectors lie in span(u,v); R vectors lie in its dot orthogonal.
            if all(f.sub(f.mul(z[0], v), f.mul(z[1], u)) == 0
                   if mask & (1 << i)
                   else f.add(f.mul(z[4], u), f.mul(z[5], v)) == 0
                   for i, z in enumerate(tup)):
                yield 'M'+str(mask)
                break


def verify(q, t, check_components=False):
    f = Field(q)
    values = [z for z in product(range(q), repeat=6)
              if rank_at_most_one(z, f)]
    assert len(values) == q * (3*q*q - q - 1)
    adj = {x: tuple(y for y in values if commute(x, y, f))
           for x in values}
    aset = {x: set(v) for x, v in adj.items()}
    if t == 1:
        tuples = ((a,) for a in values)
    elif t == 2:
        tuples = ((a, b) for a in values for b in adj[a])
    elif t == 3:
        tuples = ((a, b, c) for a in values for b in adj[a]
                  for c in adj[b] if c in aset[a])
    else:
        tuples = ((a, b, c, d) for a in values for b in adj[a]
                  for c in adj[b] if c in aset[a]
                  for d in adj[c] if d in aset[a] and d in aset[b])
    lines = line_list(q, f) if check_components else None
    count = 0
    witnesses = set()
    for tup in tuples:
        count += 1
        if check_components:
            memberships = list(component_memberships(tup, f, lines))
            assert memberships, (q, t, tup)
            if len(memberships) == 1:
                witnesses.add(memberships[0])
    assert count == predicted_count(q, t), (q, t, count, predicted_count(q,t))
    if check_components:
        expected = {'L', 'R', 'D'} | {'M'+str(j) for j in range(1, 2**t-1)}
        assert witnesses == expected, (q, t, witnesses, expected)
    print('PASS', 'q=', q, 't=', t, 'rank<=1=', len(values),
          'commuting=', count, 'component_check=',check_components)


if __name__ == '__main__':
    for q, t in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),
                 (4,1),(4,2),(5,1),(5,2)):
        verify(q,t,check_components=(q==2 and t in (2,3)))
    print('VERIFY_OK_TRIANGULAR_RANKONE')
