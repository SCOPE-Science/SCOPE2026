from math import gcd


def phi(n):
    x, ans, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            ans -= ans // p
        p += 1
    if x > 1:
        ans -= ans // x
    return ans


def ell(q, j):
    return (q**j - 1) // (q - 1)


def verify(q, e):
    L = ell(q, e)
    N = q**e - 1
    hs = [h for h in range(1, e) if gcd(h, e) == 1]
    units_d = [d for d in range(1, L) if gcd(d, L) == 1]
    triples = []
    for d in units_d:
        for r in range(1, N):
            if gcd(r, q - 1) != 1:
                continue
            matches = [h for h in hs if (r * ell(q, h) - d) % L == 0]
            if matches:
                assert len(matches) == 1
                triples.append((d, r, matches[0]))
    assert len(triples) == phi(e) * phi(N)

    support_map = {}
    for d, r, h in triples:
        u = r % N
        v = (r + d * (q - 1)) % N
        assert u and v and u != v
        support_map.setdefault(tuple(sorted((u, v))), []).append((d, r, h))

    for vals in support_map.values():
        assert len(vals) == 2
        (d, r, h), (d2, r2, h2) = vals
        assert (d2 + d) % L == 0
        assert ((r2 - r - d * (q - 1)) % N == 0 or
                (r - r2 - d2 * (q - 1)) % N == 0)
        assert {h, h2} == {h, e - h}

    E = phi(e) * phi(N) // phi(L)
    A = (q - 2) * L
    special = q % 2 == 1 and e % 2 == 1
    if special:
        distinct = phi(e) * phi(N) * (2 * A - 1) // 2
    else:
        distinct = phi(e) * phi(N) * A
    naive = len(units_d) * A * E
    correction = (len(units_d) // 2) * E if special else 0
    assert distinct == naive - correction
    return L, N, len(triples), len(support_map), E, A, special, distinct


for q, e in [(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4),(7,3)]:
    L, N, pairs, supports, E, A, special, distinct = verify(q, e)
    print(f"q={q} e={e} L={L} N={N} admissible_exponent_index_pairs={pairs} "
          f"support_pairs={supports} E={E} A={A} exceptional={special} distinct={distinct}")
