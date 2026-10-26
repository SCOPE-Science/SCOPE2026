"""Finite stress tests for prime color-symmetry group-complexity gap.
Uses Python standard library only. The mathematical proof is in RESULT.md.
"""
from itertools import product, permutations


def shift_word(w, p, step=1):
    return tuple((x + step) % p for x in w)


def permute_word(w, perm):
    return tuple(w[perm[i]] for i in range(len(w)))


def groups(n):
    allp = list(permutations(range(n)))
    e = tuple(range(n))
    out = set()
    for mask in range(1 << len(allp)):
        chosen = {allp[i] for i in range(len(allp)) if mask & (1 << i)} | {e}
        changed = True
        while changed:
            original = len(chosen)
            chosen |= {tuple(a[b[i]] for i in range(n)) for a in chosen for b in chosen}
            changed = len(chosen) > original
        out.add(frozenset(chosen))
    return [tuple(sorted(h)) for h in sorted(out, key=lambda x: (len(x), sorted(x)))]


def classes(F, H):
    buckets = {}
    for w in F:
        key = min(permute_word(w, h) for h in H)
        buckets.setdefault(key, set()).add(w)
    return list(buckets.values())


def color_orbits(p, n):
    U = set(product(range(p), repeat=n))
    ans = []
    while U:
        w = min(U)
        o = frozenset(shift_word(w, p, j) for j in range(p))
        assert len(o) == p
        U.difference_update(o)
        ans.append(o)
    return ans


def audit(F, p, n, H):
    B = classes(F, H)
    D = len(F) - len(B)
    assert D == 0 or D >= p-1, (p, n, H, D)
    if n % p:
        assert D % p == 0, (p, n, H, D)
        assert len(B) % p == 0
    if D == p - 1:
        nontrivial = [C for C in B if len(C) > 1]
        assert len(nontrivial) == 1 and len(nontrivial[0]) == p
        C = nontrivial[0]
        assert C == {shift_word(next(iter(C)), p, j) for j in range(p)}
    return D


def periodic_factors(period, n):
    return {tuple((period * (n // len(period) + 2))[i:i+n]) for i in range(len(period))}


def check_all(p, n):
    os = color_orbits(p, n)
    hs = groups(n)
    tests = 0
    possible_D = set()
    for mask in range(1 << len(os)):
        F = set().union(*(os[i] for i in range(len(os)) if mask & (1 << i)))
        for h in hs:
            possible_D.add(audit(F, p, n, h))
            tests += 1
    print(f'EXHAUSTIVE p={p} n={n}: {len(os)} color-orbits, {1<<len(os)} invariant factor sets, {len(hs)} position groups, {tests} cases; deficits={sorted(possible_D)}')


def check_examples(p):
    W = tuple(range(p))
    F = periodic_factors(W, p)
    cyclic_positions = tuple(tuple((i + j) % p for i in range(p)) for j in range(p))
    D = audit(F, p, p, cyclic_positions)
    assert len(F) == p and D == p - 1
    assert {shift_word(w, p) for w in F} == F
    V = tuple(x for j in range(p) for x in (j, (j + 1) % p, (j + 2) % p))
    E = periodic_factors(V, 2)
    H2 = groups(2)[-1]
    D2 = audit(E, p, 2, H2)
    assert len(E) == 2*p and D2 == p
    # Alphabet shift corresponds to three-position cyclic rotation of V.
    assert tuple((x+1) % p for x in V) == V[3:] + V[:3]
    assert {shift_word(w, p) for w in E} == E
    print(f'SHARP p={p}: length {p}: ({len(F)} factors, deficit {D}); length 2: ({len(E)} factors, deficit {D2})')


if __name__ == '__main__':
    check_all(3, 2)
    check_all(3, 3)
    check_all(5, 2)
    check_all(7, 2)
    for p in (3, 5, 7):
        check_examples(p)
    print('FINITE_STRESS_TESTS_OK')
