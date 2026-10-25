#!/usr/bin/env python3
"""Exact finite-field certificate for 68 lines on an explicit characteristic-2 quartic.

Run beside lines.txt with Python 3, using only the standard library.
"""
from collections import Counter
from pathlib import Path

FIELD_SIZE = 64
MODULUS = 0b1000011  # z^6 + z + 1; integers encode binary polynomials in z.


def poldeg(v):
    return v.bit_length() - 1


def polrem(a, b):
    while a and poldeg(a) >= poldeg(b):
        a ^= b << (poldeg(a) - poldeg(b))
    return a


def polmul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def polpowmod(a, n, m):
    result = 1
    while n:
        if n & 1:
            result = polrem(polmul(result, a), m)
        a = polrem(polmul(a, a), m)
        n >>= 1
    return result


def polgcd(a, b):
    while b:
        a, b = b, polrem(a, b)
    return a


def prove_irreducible():
    # Rabin's criterion for degree 6, with prime divisors 2 and 3.
    x = 0b10
    assert polpowmod(x, 64, MODULUS) == x
    assert polgcd(MODULUS, polpowmod(x, 8, MODULUS) ^ x) == 1
    assert polgcd(MODULUS, polpowmod(x, 4, MODULUS) ^ x) == 1


def mul(a, b):
    assert 0 <= a < FIELD_SIZE and 0 <= b < FIELD_SIZE
    return polrem(polmul(a, b), MODULUS)


def power(a, n):
    result = 1
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] ^= mul(x, y)
    return out


def product(*terms):
    result = [1]
    for t in terms:
        result = poly_mul(result, t)
    return result


def xor(*polys):
    result = [0] * max(map(len, polys))
    for p in polys:
        for i, val in enumerate(p):
            result[i] ^= val
    return result


def restriction(A, B):
    # coefficient at s^i t^(4-i) in F(s A+t B), i=0,...,4.
    x0, x1, x2, x3 = ([B[i], A[i]] for i in range(4))
    return xor(product(x0,x1,x1,x2), product(x1,x1,x1,x1),
               product(x1,x2,x2,x2), product(x0,x0,x0,x3),
               product(x0,x2,x3,x3))


def tangent_column(A, B, da, db):
    x0, x1, x2, x3 = ([B[i], A[i]] for i in range(4))
    d0, d1, d2, d3 = ([db[i], da[i]] for i in range(4))
    # Characteristic-2 first variation of the quartic F.
    return xor(product(d0,x1,x1,x2), product(x0,x1,x1,d2),
               product(d1,x2,x2,x2), product(x1,x2,x2,d2),
               product(x0,x0,d0,x3), product(x0,x0,x0,d3),
               product(d0,x2,x3,x3), product(x0,d2,x3,x3))


def rank(rows):
    if not rows:
        return 0
    data = [r.copy() for r in rows]
    count = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(count,len(data)) if data[i][col]), None)
        if pivot is None:
            continue
        data[count], data[pivot] = data[pivot], data[count]
        inv = power(data[count][col], 62)
        data[count] = [mul(v, inv) for v in data[count]]
        for i in range(len(data)):
            if i == count or data[i][col] == 0:
                continue
            u = data[i][col]
            data[i] = [v ^ mul(u, w) for v,w in zip(data[i],data[count])]
        count += 1
        if count == len(data):
            break
    return count


def read_lines():
    rows = []
    for raw in (Path(__file__).resolve().parent / 'lines.txt').read_text('utf-8').splitlines():
        words = raw.split()
        assert len(words) == 11 and words[0] == 'LINE', raw
        p, q, *vec = [int(w) for w in words[1:]]
        assert 0 <= p < q < 4 and len(vec) == 8
        A, B = vec[:4], vec[4:]
        assert all(0 <= x < FIELD_SIZE for x in vec)
        assert A[p] == 1 and B[q] == 1 and A[q] == B[p] == 0
        assert all(A[j] == 0 for j in range(p))
        assert all(B[j] == 0 for j in range(q))
        rows.append((p,q,tuple(A),tuple(B)))
    assert len(rows) == len(set(rows)) == 68
    return rows


def main():
    prove_irreducible()
    lines = read_lines()
    line_set = set(lines)
    tangents = Counter()
    chart = Counter()
    for p,q,A,B in lines:
        assert restriction(A,B) == [0,0,0,0,0]
        free = [(0,j) for j in range(p+1,4) if j != q]
        free += [(1,j) for j in range(q+1,4)]
        cols = []
        for row,j in free:
            da = [0]*4
            db = [0]*4
            (da if row == 0 else db)[j] = 1
            cols.append(tangent_column(A,B,da,db))
        tangent_dim = len(free) - rank(cols)
        assert tangent_dim == 0, (p,q,A,B,tangent_dim)
        tangents[tangent_dim] += 1
        chart[(p,q)] += 1
    def frobenius(L):
        p,q,A,B = L
        return (p,q,tuple(mul(x,x) for x in A),tuple(mul(x,x) for x in B))
    assert all(frobenius(L) in line_set for L in lines)
    seen = set()
    cycles = Counter()
    special = Counter()
    cuspidal = Counter()
    for L in lines:
        if L in seen:
            continue
        orb = []
        nxt = L
        while nxt not in orb:
            orb.append(nxt)
            nxt = frobenius(nxt)
        assert nxt == L
        assert all(M not in seen for M in orb)
        seen.update(orb)
        degree = len(orb)
        assert degree in (1,2,3,6)
        cycles[degree] += 1
        # Exactly four lines in the plane x0=0 are the cuspidal ones.
        family = cuspidal if all(A[0] == B[0] == 0 for _,_,A,B in orb) else special
        family[degree] += 1
    assert len(seen) == 68
    assert cycles == Counter({1:4,2:2,3:2,6:9})
    assert cuspidal == Counter({1:2,2:1})
    assert special == Counter({1:2,2:1,3:2,6:9})
    assert tangents == Counter({0:68})
    assert chart == Counter({(0,1):48,(0,2):16,(1,3):3,(2,3):1})
    print('GF64 irreducibility: PASS')
    print('contained distinct lines: 68')
    print('RREF charts:',dict(sorted(chart.items())))
    print('all line-scheme tangent dimensions: 0')
    print('Frobenius cycles:',dict(sorted(cycles.items())))
    print('cuspidal plane cycles:',dict(sorted(cuspidal.items())))
    print('other-line cycles:',dict(sorted(special.items())))
    for n in (1,2,3,4,5,6):
        count = sum(d*c for d,c in cycles.items() if n%d==0)
        print('F_2^%d count: %d'%(n,count))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
