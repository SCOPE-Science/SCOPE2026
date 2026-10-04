from itertools import product, combinations
from collections import Counter, deque
from math import gcd


def add(x, y, mods):
    return tuple((a + b) % m for a, b, m in zip(x, y, mods))


def neg(x, mods):
    return tuple((-a) % m for a, m in zip(x, mods))


def sub(x, y, mods):
    return add(x, neg(y, mods), mods)


def additive_subgroup(gens, mods):
    zero = tuple(0 for _ in mods)
    steps = list(gens) + [neg(g, mods) for g in gens]
    seen = {zero}
    q = deque([zero])
    while q:
        x = q.popleft()
        for g in steps:
            z = add(x, g, mods)
            if z not in seen:
                seen.add(z)
                q.append(z)
    return seen


def element_order(a, mods):
    if all(x == 0 for x in a):
        return 1
    ans = 1
    for x, m in zip(a, mods):
        if x:
            o = m // gcd(m, x)
            ans = ans * o // gcd(ans, o)
    return ans


def prime_factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def rank_mod_p(vectors, p):
    if not vectors:
        return 0
    M = [[x % p for x in v] for v in vectors]
    rows = len(M)
    cols = len(M[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(z * inv) % p for z in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c] % p
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def sylow_coordinates(a, mods, p):
    # For the examples, each cyclic factor has prime-power order or is coprime to p.
    return tuple((x % p) for x, m in zip(a, mods) if m % p == 0)


def predicted_adj(x, y, mods):
    # The examples all have d(A)=2.
    primes = sorted(set(q for m in mods for q in prime_factors(m)))
    ranks = {p: sum(1 for m in mods if m % p == 0) for p in primes}
    d = max(ranks.values())
    assert d == 2
    P = {p for p, r in ranks.items() if r == d}
    Q = {p for p, r in ranks.items() if r == d - 1}

    def active(a):
        return all(any(z % p for z in sylow_coordinates(a, mods, p)) for p in P)

    ax, ex = x
    ay, ey = y
    if ex == 0 and ey == 1:
        return active(ax)
    if ex == 1 and ey == 0:
        return active(ay)
    if ex == 1 and ey == 1:
        return active(sub(ay, ax, mods))
    for p in P:
        u = sylow_coordinates(ax, mods, p)
        v = sylow_coordinates(ay, mods, p)
        if rank_mod_p([u, v], p) != 2:
            return False
    for p in Q:
        u = sylow_coordinates(ax, mods, p)
        v = sylow_coordinates(ay, mods, p)
        if not any(u) and not any(v):
            return False
    return True


def triple_generates(triple, mods, A_size):
    reflections = [x for x in triple if x[1] == 1]
    if not reflections:
        return False
    base = reflections[0][0]
    rotations = []
    used_base = False
    for a, e in triple:
        if e == 0:
            rotations.append(a)
        else:
            if not used_base and a == base:
                used_base = True
            else:
                rotations.append(sub(a, base, mods))
    return len(additive_subgroup(rotations, mods)) == A_size


def run_case(mods, expected_triples, expected_degrees):
    A = list(product(*[range(m) for m in mods]))
    elems = [(a, e) for a in A for e in (0, 1)]
    A_size = len(A)
    edges = set()
    generating = 0
    for idxs in combinations(range(len(elems)), 3):
        tri = [elems[i] for i in idxs]
        if triple_generates(tri, mods, A_size):
            generating += 1
            for i, j in combinations(idxs, 2):
                edges.add((i, j))
    assert generating == expected_triples
    deg = [0] * len(elems)
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    assert Counter(deg) == Counter(expected_degrees)

    # Compare every pair with the theorem's direct rank criterion.
    for i, j in combinations(range(len(elems)), 2):
        assert ((i, j) in edges) == predicted_adj(elems[i], elems[j], mods)

    # Check order divides degree for every vertex.
    for (a, e), dgr in zip(elems, deg):
        order = 2 if e else element_order(a, mods)
        assert dgr % order == 0
    return generating, Counter(deg)


r1 = run_case((9, 3), 13608, {0: 3, 45: 24, 48: 27})
r2 = run_case((3, 3, 5), 60480, {0: 5, 69: 8, 75: 32, 80: 45})
print('VERIFY_OK')
print(r1)
print(r2)
