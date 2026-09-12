"""Exhaustive classification of anti-Pasch cyclic STS(19) difference families."""
import sys
from itertools import combinations
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1132/output/artifacts')
from ball import gen

V = 19
UNITS = [u for u in range(1, V) if u % 19 != 0]


def diffs_of(tri):
    a, b, c = tri
    s = set()
    for x, y in ((a, b), (a, c), (b, c)):
        s.add((y - x) % V); s.add((x - y) % V)
    return s


def search():
    triples = [(0, i, j) for i in range(1, V) for j in range(i + 1, V)]
    dmap = {t: diffs_of(t) for t in triples}
    fams = []
    # fix first triple with middle=1 to break translation+negation symmetry partially;
    # then complete the difference partition. Collect ALL then quotient later.
    # Simpler: full backtrack over partition of Z19\{0}.
    def bt(chosen, covered):
        if len(chosen) == 3:
            if len(covered) == 18:
                fams.append(tuple(chosen))
            return
        if len(covered) >= 18:
            return
        # smallest uncovered difference must be covered next
        d = min(set(range(1, V)) - covered)
        for t in triples:
            if d in dmap[t] and not (dmap[t] & covered):
                bt(chosen + [t], covered | dmap[t])
    bt([], set())
    return fams


def pasch_count(B):
    bl = list(B)
    n = 0
    for six in combinations(range(V), 6):
        s = set(six)
        if sum(1 for b in bl if s.issuperset(b)) == 4:
            from collections import Counter
            deg = Counter()
            for b in bl:
                if s.issuperset(b):
                    for x in b:
                        deg[x] += 1
            if all(deg[x] == 2 for x in six):
                n += 1
    return n


def canon_mult(B):
    # canonical multiplier-quotient signature: sorted tuple of sorted mapped fams
    best = None
    for u in UNITS:
        img = set()
        for b in B:
            img.add(tuple(sorted([(u * x) % V for x in b])))
        # translate-normalize: shift so that ... use sorted tuple
        key = tuple(sorted(img))
        if best is None or key < best:
            best = key
    return best


if __name__ == '__main__':
    fams = search()
    print('raw difference families:', len(fams))
    anti = []
    for f in fams:
        B = gen(list(f))
        assert len(B) == 57
        if pasch_count(B) == 0:
            anti.append(f)
    print('anti-Pasch raw fams:', len(anti))
    for f in anti:
        print(f)
    # quotient by multiplier equivalence
    types = {}
    for f in anti:
        B = gen(list(f))
        k = canon_mult(B)
        types.setdefault(k, []).append(f)
    print('multiplier types:', len(types))
    for k, v in types.items():
        print('type size', len(v), 'eg', v[0])
