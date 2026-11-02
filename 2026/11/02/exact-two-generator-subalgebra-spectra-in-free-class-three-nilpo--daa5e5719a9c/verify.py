#!/usr/bin/env python3
"""Independent associative-word model for two-generator Lie subalgebras.

The verification embeds the truncated free Lie algebra into the free
associative word algebra and computes actual brackets and linear spans.
No external libraries are needed. Exhaustive testing is used where stated.
"""
from collections import Counter
from itertools import combinations, product
import random


def linear_rank(rows, p):
    pivots = {}
    for row in rows:
        a = [v % p for v in row]
        for j in sorted(pivots):
            if a[j]:
                f = a[j]
                v = pivots[j]
                a = [(x - f * y) % p for x, y in zip(a, v)]
        t = next((i for i, x in enumerate(a) if x), None)
        if t is not None:
            b = pow(a[t], -1, p)
            pivots[t] = [(x * b) % p for x in a]
    return len(pivots)


def canonical_row_space(rows, p):
    """Unique reduced echelon encoding of a linear subspace."""
    pivots = {}
    for row in rows:
        a = [v % p for v in row]
        for j in sorted(pivots):
            if a[j]:
                b = pivots[j]
                a = [(x - a[j] * y) % p for x, y in zip(a, b)]
        pivot = next((i for i, v in enumerate(a) if v), None)
        if pivot is None:
            continue
        inv = pow(a[pivot], -1, p)
        a = [(v * inv) % p for v in a]
        for j, old in list(pivots.items()):
            if old[pivot]:
                f = old[pivot]
                pivots[j] = [(x - f * y) % p for x, y in zip(old, a)]
        pivots[pivot] = a
    return tuple(tuple(pivots[j]) for j in sorted(pivots))


def bracket(a, b, p):
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            if len(wa) + len(wb) <= 3:
                x, y = wa + wb, wb + wa
                out[x] = (out.get(x, 0) + ca * cb) % p
                out[y] = (out.get(y, 0) - ca * cb) % p
    return {w: x for w, x in out.items() if x}


def as_row(a, words):
    return tuple(a.get(w, 0) for w in words)


def lie_basis(n, p):
    gens = [{(i,): 1} for i in range(n)]
    degree2 = [bracket(gens[i], gens[j], p) for i, j in combinations(range(n), 2)]
    third = []
    words3 = list(product(range(n), repeat=3))
    for b in degree2:
        for g in gens:
            c = bracket(b, g, p)
            if linear_rank([as_row(x, words3) for x in third + [c]], p) > len(third):
                third.append(c)
    m, w = n * (n - 1) // 2, (n ** 3 - n) // 3
    assert len(degree2) == m and len(third) == w, (n, p, len(third), w)
    return gens + degree2 + third


def combine(basis, coeff, p):
    ans = {}
    for a, c in zip(basis, coeff):
        if c:
            for word, val in a.items():
                ans[word] = (ans.get(word, 0) + c * val) % p
    return {w: x for w, x in ans.items() if x}


def generated_rows(x, y, p, words):
    z = bracket(x, y, p)
    xz = bracket(x, z, p)
    yz = bracket(y, z, p)
    return [as_row(t, words) for t in (x, y, z, xz, yz)]


def generated_dimension(x, y, p, words):
    return linear_rank(generated_rows(x,y,p,words),p)


def formula(n, q):
    m = n * (n - 1) // 2
    w = (n ** 3 - n) // 3
    A, B, C = q ** n, q ** m, q ** w
    N = A * B * C
    c5 = (A-1)*(A-q)*B*B*C*C
    c3 = (A-1)*(q+1)*B*(B-1)*C*C
    commuting = B*C*C*(B+(A-1)*(q+1))
    c0 = 1
    c1 = (q+1)*(N-1)
    c2 = commuting-c0-c1
    assert sum((c0,c1,c2,c3,c5)) == N*N
    assert min(c0,c1,c2,c3,c5) >= 0
    return {0:c0,1:c1,2:c2,3:c3,5:c5}


def subalgebra_formula(n,q):
    m = n*(n-1)//2
    w = (n**3-n)//3
    total_dim = n+m+w
    pair = formula(n,q)
    gl2 = (q*q-1)*(q*q-q)
    return {0:1, 1:(q**total_dim-1)//(q-1),
            2:pair[2]//gl2,
            3:((q**n-1)//(q-1))*((q**m-1)//(q-1))*q**(m+2*w-3),
            5:((q**n-1)*(q**n-q)//gl2)*q**(2*(m+w-3))}


def exhaustive(n, q):
    basis = lie_basis(n, q)
    words = [w for r in range(1,4) for w in product(range(n), repeat=r)]
    elems = [combine(basis, c, q) for c in product(range(q), repeat=len(basis))]
    census = Counter()
    distinct = {}
    for x in elems:
        for y in elems:
            rows = generated_rows(x,y,q,words)
            dim = linear_rank(rows,q)
            census[dim] += 1
            distinct[canonical_row_space(rows,q)] = dim
    expected = formula(n, q)
    assert dict(census) == expected, (n,q,census,expected)
    subcounts = Counter(distinct.values())
    assert dict(subcounts) == subalgebra_formula(n,q), (n,q,subcounts,subalgebra_formula(n,q))
    return {"n":n,"q":q,"elements":len(elems),"pairs":len(elems)**2,
            "pair_counts":dict(sorted(census.items())), "distinct_subalgebras":dict(sorted(subcounts.items()))}


def sample(n, q, tests=5000):
    basis = lie_basis(n,q)
    words = [w for r in range(1,4) for w in product(range(n), repeat=r)]
    rnd = random.Random(241075)
    found = Counter()
    for _ in range(tests):
        cx = [rnd.randrange(q) for _ in basis]
        cy = [rnd.randrange(q) for _ in basis]
        x,y = combine(basis,cx,q), combine(basis,cy,q)
        d = generated_dimension(x,y,q,words)
        nx,ny = cx[:n],cy[:n]
        r = linear_rank((nx,ny),q)
        predicted = 5 if r == 2 else (3 if bracket(x,y,q) else linear_rank((cx,cy),q))
        assert d == predicted, (n,q,cx,cy,d,predicted)
        found[d] += 1
    return {"n":n,"q":q,"sample_pairs":tests,"observed_dimensions":dict(sorted(found.items()))}


def main():
    for n,q in ((2,2),(2,3)):
        print('EXHAUSTIVE',exhaustive(n,q))
    for n,q in ((3,2),(3,3),(4,2)):
        print('SAMPLED',sample(n,q,1500))
    print('FREE_CLASS3_TWO_GENERATOR_CENSUS_OK')

if __name__ == '__main__':
    main()
