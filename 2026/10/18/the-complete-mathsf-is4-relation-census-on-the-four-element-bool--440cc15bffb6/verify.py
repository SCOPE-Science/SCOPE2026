"""Exhaustive certificate for admissible modal preorders over the Boolean square.
Run with: python3 diamond_verify.py. Standard Python only.
"""
from collections import Counter

N = 4
# Bit i in LE[x] means x <= i, with diamond bottom 0, middle 1,2, top 3.
LE = (15, 10, 12, 8)
SWAP = (0, 2, 1, 3)


def checks(rows):
    if any(not (rows[i] & (1 << i)) for i in range(N)):
        return False
    # Reflexivity and transitivity of modal accessibility.
    if any((rows[y] & ~rows[x]) != 0 for x in range(N)
           for y in range(N) if rows[x] & (1 << y)):
        return False
    # Source-defined Fischer--Servi interactions F1 and F2, no shortcuts.
    for x in range(N):
        for y in range(N):
            if not (rows[x] & (1 << y)):
                continue
            for z in range(N):
                if LE[y] & (1 << z):
                    if not any((LE[x] & (1 << u)) and (rows[u] & (1 << z))
                               for u in range(N)):
                        return False
                if LE[x] & (1 << z):
                    if not any((rows[z] & (1 << u)) and (LE[y] & (1 << u))
                               for u in range(N)):
                        return False
    return True


def raw_relations():
    off = [(i, j) for i in range(N) for j in range(N) if i != j]
    assert len(off) == 12
    for bits in range(1 << len(off)):
        r = [1 << i for i in range(N)]
        for bit, (i, j) in enumerate(off):
            if bits & (1 << bit): r[i] |= 1 << j
        yield tuple(r)


def partitions(n):
    # Distinct set partitions, via restricted-growth strings.
    def rec(code, m):
        if len(code) == n:
            yield tuple(code)
        else:
            for j in range(m + 2):
                yield from rec(code + [j], max(m, j))
    yield from rec([0], 0)


def block_posets(t):
    off = [(i,j) for i in range(t) for j in range(t) if i != j]
    for bits in range(1 << len(off)):
        r = [1 << i for i in range(t)]
        for bit,(i,j) in enumerate(off):
            if bits & (1 << bit):r[i] |= 1 << j
        # Antisymmetry and transitivity.
        if any((r[i] & (1 << j)) and (r[j] & (1 << i)) for i in range(t) for j in range(i+1,t)):
            continue
        if any(r[j] & ~r[i] for i in range(t) for j in range(t) if r[i] & (1 << j)):
            continue
        yield tuple(r)


def independent_preorders():
    for p in partitions(N):
        t = 1 + max(p)
        for block_relation in block_posets(t):
            yield tuple(sum((1 << j) for j in range(N)
                            if block_relation[p[i]] & (1 << p[j])) for i in range(N))


def conjugate(rows):
    return tuple(sum(((rows[SWAP[i]] >> SWAP[j]) & 1) << j for j in range(N)) for i in range(N))


def verify():
    a = {r for r in raw_relations() if checks(r)}
    assert len(a) == 135
    b_all = list(independent_preorders())
    assert len(b_all) == 355 and len(set(b_all)) == 355
    b = {r for r in b_all if checks(r)}
    assert a == b  # independent generation paths, exact complete sets
    profile = Counter((bool(r[0] & 8), bool(r[3] & 1)) for r in a)
    assert profile == {(False,False):76, (True,False):29,
                       (False,True):29, (True,True):1}, profile
    assert all(r == (15,15,15,15) for r in a if r[0]&8 and r[3]&1)
    assert all(conjugate(r) in a for r in a)
    fixed = sum(conjugate(r) == r for r in a)
    assert fixed == 27
    orbits = {min(r,conjugate(r)) for r in a}
    assert len(orbits) == 81 and (len(a) + fixed)//2 == 81
    print('REFLEXIVE_RELATIONS_ENUMERATED=4096')
    print('INDEPENDENT_PREORDERS_ENUMERATED=355')
    print('ADMISSIBLE_RELATIONS=135')
    print('ROOT_TOP_EDGE_PROFILE=76,29,29,1')
    print('SIDE_SWAP_FIXED=27')
    print('SIDE_SWAP_ORBITS=81')
    print('DIAMOND_IS4_CENSUS_VERIFY_OK')


if __name__ == '__main__':
    verify()
