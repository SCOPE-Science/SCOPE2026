#!/usr/bin/env python3
"""Exact finite-field enumeration for Paley four-extension at the first order.

Use `python3 verify_paley89.py` (Python 3.9+, standard library only).
Field elements are base-p coefficient vectors, not integers modulo p**k.
"""
import itertools
import json
from math import isqrt

# Irreducible monic polynomials, lowest-degree coefficient first.
MODULUS = {
    (3, 2): (1, 0, 1),       # x^2+1
    (5, 2): (1, 1, 1),       # x^2+x+1
    (7, 2): (1, 0, 1),       # x^2+1
    (3, 4): (2, 1, 0, 0, 1),# x^4+x+2
}


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def prime_powers(up_to):
    ans = {}
    for p in range(2, up_to + 1):
        if not prime(p):
            continue
        k, q = 1, p
        while q <= up_to:
            if q % 4 == 1 and q >= 5:
                ans[q] = (p, k)
            k, q = k + 1, q * p
    return sorted((q, p, k) for q, (p, k) in ans.items())


def remainder(poly, divisor, p):
    a = [v % p for v in poly]
    deg = len(divisor) - 1
    while len(a) > deg:
        lead = a[-1]
        if lead:
            for j in range(deg):
                a[len(a)-deg-1+j] = (a[len(a)-deg-1+j] - lead * divisor[j]) % p
        a.pop()
    return a


def validate_modulus(p, k):
    if k == 1:
        return
    f = MODULUS[p, k]
    assert f[-1] == 1 and len(f) == k + 1
    # A reducible quartic has a factor of degree at most two.
    for degree in range(1, k // 2 + 1):
        for coeffs in itertools.product(range(p), repeat=degree):
            g = tuple(coeffs) + (1,)
            assert any(remainder(f, g, p)), (p, k, g)


def make_field_graph(p, k):
    validate_modulus(p, k)
    q = p ** k
    if k == 1:
        add = lambda a, b: (a+b) % p
        mult = lambda a, b: (a*b) % p
    else:
        f = MODULUS[p, k]
        digits = [tuple((a // p**j) % p for j in range(k)) for a in range(q)]
        lookup = {a: j for j, a in enumerate(digits)}

        def add(a, b):
            return lookup[tuple((x+y) % p for x, y in zip(digits[a], digits[b]))]

        def mult(a, b):
            aa, bb = digits[a], digits[b]
            product = [0] * (2*k-1)
            for i in range(k):
                for j in range(k):
                    product[i+j] = (product[i+j] + aa[i]*bb[j]) % p
            for t in range(2*k-2, k-1, -1):
                v = product[t]
                for j in range(k):
                    product[t-k+j] = (product[t-k+j] - v*f[j]) % p
            return lookup[tuple(product[:k])]

    residues = {mult(v, v) for v in range(1, q)}
    assert len(residues) == (q-1)//2 and 0 not in residues
    assert all(add(v, r) < q for v in range(q) for r in residues)
    nonresidue = next(v for v in range(1, q) if v not in residues)
    adj = [sum(1 << add(a, v) for v in residues) for a in range(q)]
    assert all(((adj[a] >> b) & 1) == ((adj[b] >> a) & 1)
               for a in range(q) for b in range(q))
    assert all((adj[a] >> a) & 1 == 0 for a in range(q))
    return nonresidue, adj


def check_four_extension(q, nu, adj):
    """Use only translation and square-multiplication automorphisms.

    Every ordered distinct initial pair is carried to (0,1) or (0,nu).
    For each pair, exhaust unordered choices x<y of remaining points,
    and all 16 desired adjacency patterns to (0,d,x,y).
    """
    full = (1 << q) - 1
    visited = 0
    for d in (1, nu):
        for x in range(1, q):
            if x == d:
                continue
            for y in range(x+1, q):
                if y == d:
                    continue
                visited += 1
                vertices = (0, d, x, y)
                free = full ^ sum(1 << v for v in vertices)
                extensions = [free]
                for vertex in vertices:
                    N = adj[vertex]
                    extensions = [mask & (full ^ N) for mask in extensions] + [mask & N for mask in extensions]
                for pattern, candidates in enumerate(extensions):
                    if not candidates:
                        return {"four_ec": False, "bad_set": list(vertices),
                                "missing_adjacency_pattern": pattern, "checked_orbits": visited}
    assert visited == (q-2)*(q-3)
    return {"four_ec": True, "bad_set": None,
            "missing_adjacency_pattern": None, "checked_orbits": visited}


def main():
    data = []
    for q, p, k in prime_powers(89):
        nu, adj = make_field_graph(p, k)
        result = check_four_extension(q, nu, adj)
        result.update({"q": q, "characteristic": p, "extension_degree": k,
                       "normalized_nonsquare": nu})
        data.append(result)
        print("q=%d p=%d degree=%d four_ec=%s pair_orbits=%d witness=%s pattern=%s" % (
            q, p, k, result['four_ec'], result['checked_orbits'],
            result['bad_set'], result['missing_adjacency_pattern']))
    assert [v['q'] for v in data if v['four_ec']] == [89]
    print("VERIFIED: 89 is the least Paley graph order with the 4-e.c. property.")
    return data


if __name__ == '__main__':
    main()
