from itertools import product

def add(a, b, mods):
    return tuple((x + y) % m for x, y, m in zip(a, b, mods))

def neg(a, mods):
    return tuple((-x) % m for x, m in zip(a, mods))

def zero(mods):
    return tuple(0 for _ in mods)

def elements_A(mods):
    return [tuple(v) for v in product(*[range(m) for m in mods])]

def mul(g, h, mods, y):
    a, e = g
    b, f = h
    term = b if e == 0 else neg(b, mods)
    c = add(a, term, mods)
    if e and f:
        c = add(c, y, mods)
    return (c, e ^ f)

def verify_case(mods, y):
    A = elements_A(mods)
    z = zero(mods)
    G = [(a, e) for a in A for e in (0, 1)]
    T = [a for a in A if add(a, a, mods) == z]
    Tset = set(T)
    m = len(A)
    t = len(T)

    assert add(y, y, mods) == z and y != z
    assert t < m  # nonabelian scope

    def commute(g, h):
        return mul(g, h, mods, y) == mul(h, g, mods, y)

    center = {g for g in G if all(commute(g, h) for h in G)}
    assert center == {(a, 0) for a in T}

    for a in A:
        g = (a, 0)
        C = {h for h in G if commute(g, h)}
        if a not in Tset:
            assert C == {(b, 0) for b in A}

    for a in A:
        g = (a, 1)
        C = {h for h in G if commute(g, h)}
        expected = {(u, 0) for u in T}
        expected |= {(add(a, u, mods), 1) for u in T}
        assert C == expected
        assert all(commute(u, v) for u in C for v in C)

    # Edge-for-edge comparison with K_t join (K_{m-t} disjoint-union (m/t) K_t).
    def model_commute(g, h):
        if g == h:
            return False
        a, e = g
        b, f = h
        if e == 0 and a in Tset:
            return True
        if f == 0 and b in Tset:
            return True
        if e == 0 and f == 0:
            return a not in Tset and b not in Tset
        if e != f:
            return False
        # both outside A
        return add(a, neg(b, mods), mods) in Tset

    for i, g in enumerate(G):
        for h in G[i + 1:]:
            assert commute(g, h) == model_commute(g, h), (mods, y, g, h)

    # Degree profile forced by the claimed decomposition.
    degrees = sorted(sum(commute(g, h) for h in G if h != g) for g in G)
    expected_degrees = sorted(
        [2 * m - 1] * t
        + [m - 1] * (m - t)
        + [2 * t - 1] * m
    )
    assert degrees == expected_degrees

tests = [
    ((4,), (2,)),
    ((6,), (3,)),
    ((8,), (4,)),
    ((3, 4), (0, 2)),
    ((4, 2), (2, 0)),
    ((4, 2), (0, 1)),
    ((4, 4), (2, 0)),
    ((4, 4), (2, 2)),
    ((8, 2), (4, 0)),
    ((4, 2, 2), (2, 0, 0)),
]

for mods, y in tests:
    verify_case(mods, y)

print("VERIFY_OK")
