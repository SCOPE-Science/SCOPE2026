from itertools import product
from collections import deque

def add_A(x, y, mods):
    return tuple((a + b) % m for a, b, m in zip(x, y, mods))

def neg_A(x, mods):
    return tuple((-a) % m for a, m in zip(x, mods))

def elements_A(mods):
    return [tuple(v) for v in product(*[range(m) for m in mods])]

def zero_A(mods):
    return tuple(0 for _ in mods)

def mul_dih(x, y, mods):
    a, e = x
    b, f = y
    if e:
        b = neg_A(b, mods)
    return (add_A(a, b, mods), (e + f) & 1)

def cyclic_subgroup(g, identity, mul):
    H = {identity}
    x = identity
    while True:
        x = mul(x, g)
        if x in H:
            break
        H.add(x)
    return frozenset(H)

def enhanced_power_graph(mods):
    A = elements_A(mods)
    elements = [(a, e) for a in A for e in (0, 1)]
    identity = (zero_A(mods), 0)
    cyclic = {
        cyclic_subgroup(g, identity, lambda x, y: mul_dih(x, y, mods))
        for g in elements
    }
    adj = {g: set() for g in elements}
    for H in cyclic:
        H = list(H)
        for i, u in enumerate(H):
            for v in H[i + 1:]:
                adj[u].add(v)
                adj[v].add(u)
    return A, elements, identity, adj

def isolated_kernel_involutions(mods):
    A = elements_A(mods)
    z = zero_A(mods)
    cyclic = {
        cyclic_subgroup(a, z, lambda x, y: add_A(x, y, mods))
        for a in A
    }
    T = set()
    for u in A:
        if u == z or add_A(u, u, mods) != z:
            continue
        if not any(u in H and len(H) > 2 for H in cyclic):
            T.add(u)
    return T

def closed_T_count(mods):
    def is_power_two(n):
        return n >= 2 and (n & (n - 1)) == 0
    if not all(is_power_two(n) for n in mods):
        return 0
    r = len(mods)
    s = sum(n >= 4 for n in mods)
    return 2 ** r - 2 ** s

def verify_kernel(mods):
    A, elements, identity, adj = enhanced_power_graph(mods)
    z = zero_A(mods)
    T = isolated_kernel_involutions(mods)
    assert len(T) == closed_T_count(mods), (mods, T)

    # Graph-theoretic leaf characterization.
    for a in A:
        if a == z:
            continue
        is_leaf = adj[(a, 0)] == {identity}
        assert is_leaf == (a in T), (mods, a, adj[(a, 0)], T)

    F = [(a, 1) for a in A] + [(a, 0) for a in sorted(T)]
    for f in F:
        assert adj[f] == {identity}, (mods, f, adj[f])

    m = len(A)
    R = [(a, 0) for a in A if a != z and a not in T]
    assert len(R) <= len(F)

    # Coloring from the proof.
    color = {}
    for i, f in enumerate(F):
        color[f] = i
    color[identity] = len(F)
    for r, f in zip(R, F):
        color[r] = color[f]

    k = max(color.values()) + 1
    assert k == m + len(T) + 1

    # Properness.
    for u in elements:
        for v in adj[u]:
            assert color[u] != color[v], (mods, u, v, color[u])

    # All-pairs distances and locating color codes.
    dist = {}
    for source in elements:
        d = {source: 0}
        q = deque([source])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    q.append(v)
        assert len(d) == len(elements)
        dist[source] = d

    classes = [[v for v in elements if color[v] == c] for c in range(k)]
    seen = {}
    for u in elements:
        code = tuple(min(dist[u][v] for v in C) for C in classes)
        assert code not in seen, (mods, u, seen.get(code), code)
        seen[code] = u

    return m, len(T), k

tests = [
    (2,), (3,), (4,), (5,), (6,), (8,),
    (2, 2), (2, 4), (4, 4), (2, 6), (3, 3), (2, 2, 2)
]

observed = {mods: verify_kernel(mods) for mods in tests}
assert observed[(2,)] == (2, 1, 4)
assert observed[(3,)] == (3, 0, 4)
assert observed[(4,)] == (4, 0, 5)
assert observed[(2, 2)] == (4, 3, 8)
assert observed[(2, 4)] == (8, 2, 11)
assert observed[(2, 2, 2)] == (8, 7, 16)

print('VERIFY_OK')
