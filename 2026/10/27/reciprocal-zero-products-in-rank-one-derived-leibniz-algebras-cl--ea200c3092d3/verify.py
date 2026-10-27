#!/usr/bin/env python3
"""Finite-field tests for the one-dimensional-derived Leibniz reciprocity classification.

Run with: python3 verify.py
Uses only the Python 3 standard library.
"""
from itertools import product


def span_rank(vectors, q):
    if not vectors:
        return 0
    a = [[x % q for x in row] for row in vectors]
    rows, cols = len(a), len(a[0])
    rank = 0
    for c in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][c], -1, q)
        a[rank] = [(t * inv) % q for t in a[rank]]
        for i in range(rows):
            if i != rank and a[i][c]:
                t = a[i][c]
                a[i] = [(a[i][k] - t * a[rank][k]) % q for k in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def zero_vector(n):
    return (0,) * n


def bracket(tensor, x, y, q):
    n = len(x)
    v = [0] * n
    for i in range(n):
        for j in range(n):
            c = (x[i] * y[j]) % q
            if c:
                for k in range(n):
                    v[k] = (v[k] + c * tensor[i][j][k]) % q
    return tuple(v)


def is_right_leibniz(tensor, q):
    n = len(tensor)
    base = [tuple(int(i == j) for i in range(n)) for j in range(n)]
    for x, y, z in product(base, repeat=3):
        left = bracket(tensor, bracket(tensor, x, y, q), z, q)
        right1 = bracket(tensor, bracket(tensor, x, z, q), y, q)
        right2 = bracket(tensor, x, bracket(tensor, y, z, q), q)
        if left != tuple((a + b) % q for a, b in zip(right1, right2)):
            return False
    return True


def reciprocal(tensor, q):
    n = len(tensor)
    vectors = list(product(range(q), repeat=n))
    zero = zero_vector(n)
    for x in vectors:
        for y in vectors:
            if (bracket(tensor, x, y, q) == zero) != (bracket(tensor, y, x, q) == zero):
                return False
    return True


def is_lie(tensor, q):
    n = len(tensor)
    for i in range(n):
        if tensor[i][i] != zero_vector(n):
            return False
        for j in range(n):
            if any((tensor[i][j][k] + tensor[j][i][k]) % q for k in range(n)):
                return False
    return True


def is_symmetric(tensor, q):
    n = len(tensor)
    return all(tensor[i][j] == tensor[j][i] for i in range(n) for j in range(n))


def encode_tensor(t):
    return tuple(v for row in t for v0 in row for v in v0)


def tensor_from_flat(flat, n):
    p = iter(flat)
    return tuple(tuple(tuple(next(p) for k in range(n)) for j in range(n)) for i in range(n))


def n2_exhaustive(q):
    n = 2
    counts = {'symmetric': 0, 'lie': 0}
    for flat in product(range(q), repeat=n**3):
        t = tensor_from_flat(flat, n)
        if span_rank([t[i][j] for i in range(n) for j in range(n)], q) != 1:
            continue
        if not is_right_leibniz(t, q):
            continue
        if not reciprocal(t, q):
            continue
        if is_lie(t, q):
            counts['lie'] += 1
        elif is_symmetric(t, q):
            counts['symmetric'] += 1
        else:
            raise AssertionError('Missing classification type')
    assert counts == {'symmetric': q*q-1, 'lie': q*q-1}, (q,counts)
    return counts


def tuple_add(a, b, q):
    return tuple((x + y) % q for x,y in zip(a,b))


def normalized_lines(n, q):
    lines = set()
    for x in product(range(q), repeat=n):
        if all(v == 0 for v in x):
            continue
        first = next(v for v in x if v)
        lines.add(tuple(v * pow(first,-1,q) % q for v in x))
    return sorted(lines)


def n3_constructive(q=3):
    n, m = 3, 2
    std = [tuple(int(i==j) for i in range(n)) for j in range(n)]
    forms = []
    for a,b,c in product(range(q), repeat=3):
        if (a,b,c) != (0,0,0):
            forms.append(((a,b),(b,c)))
    for v in range(1,q):
        forms.append(((0,v),(-v%q,0)))
    central, affine = set(), set()
    for z in normalized_lines(n,q):
        basis = [z]
        for e in std:
            if span_rank(basis+[e],q)>len(basis):
                basis.append(e)
        assert len(basis)==n
        # Coordinates in the ordered basis (z, basis[1], basis[2]); generate lookup for vectors.
        lookup = {}
        for t in product(range(q), repeat=n):
            x=tuple(sum(t[h]*basis[h][k] for h in range(n))%q for k in range(n))
            lookup[x]=t
        for matrix in forms:
            tensor=[]
            for e in std:
                row=[]
                for f in std:
                    x,y=lookup[e][1:],lookup[f][1:]
                    scalar=sum(x[i]*matrix[i][j]*y[j] for i in range(m) for j in range(m)) % q
                    row.append(tuple(scalar*zk%q for zk in z))
                tensor.append(tuple(row))
            central.add(encode_tensor(tuple(tensor)))
        # For fixed z, enumerate all nonzero phi with phi(z)=0, alpha with alpha(z)=1.
        for phi in product(range(q), repeat=n):
            if not any(phi) or sum(phi[i]*z[i] for i in range(n))%q:
                continue
            for alpha in product(range(q), repeat=n):
                if sum(alpha[i]*z[i] for i in range(n))%q != 1:
                    continue
                t=[]
                for e in std:
                    row=[]
                    for f in std:
                        # sign normalized so [x,z] = phi(x) z
                        s = (sum(e[i]*phi[i] for i in range(n))*sum(f[i]*alpha[i] for i in range(n)) -
                             sum(e[i]*alpha[i] for i in range(n))*sum(f[i]*phi[i] for i in range(n)))%q
                        row.append(tuple(s*zk%q for zk in z))
                    t.append(tuple(row))
                affine.add(encode_tensor(tuple(t)))
    assert central.isdisjoint(affine)
    assert len(central) == (q*q+q+1)*(q**3+q-2), len(central)
    assert len(affine) == (q*q+q+1)*q*(q*q-1), len(affine)
    for flat in central|affine:
        t=tensor_from_flat(flat,n)
        assert is_right_leibniz(t,q)
        assert reciprocal(t,q)
        assert is_symmetric(t,q) or is_lie(t,q)
    return len(central), len(affine)


def mixed_example(q):
    n=4
    t=[[[0]*n for _ in range(n)] for _ in range(n)]
    t[0][0][2]=1
    t[0][1][3]=1
    t[1][0][3]=q-1
    t=tuple(tuple(tuple(v) for v in row) for row in t)
    assert span_rank([t[i][j] for i in range(n) for j in range(n)],q)==2
    assert is_right_leibniz(t,q)
    for x in product(range(q),repeat=2):
        for y in product(range(q),repeat=2):
            s = (x[0]*y[0], x[0]*y[1]-x[1]*y[0])
            rev = (s[0], -s[1])
            assert (all(v%q==0 for v in s)) == (all(v%q==0 for v in rev))
    assert not is_symmetric(t,q) and not is_lie(t,q)


def main():
    for q in (3,):
        print('n=2',q,n2_exhaustive(q))
    print('n=3,q=3 central/affine', n3_constructive(3))
    for q in (3,5,7):
        mixed_example(q)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
