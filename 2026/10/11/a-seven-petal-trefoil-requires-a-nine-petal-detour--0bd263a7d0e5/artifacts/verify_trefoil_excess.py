#!/usr/bin/env python3
from itertools import permutations


def canon(p):
    p = tuple(p)
    return min(p[i:] + p[:i] for i in range(len(p)))


def r_move(p):
    n = len(p)
    return canon(tuple((x + 1) % n for x in p))


def s_move(p):
    n = len(p)
    return canon(tuple(n - 1 - x for x in reversed(p)))


def pair_partition(n, b):
    return [((b + 1 + 2*k) % n, (b + 2 + 2*k) % n)
            for k in range((n - 1)//2)]


def legal_x(p, b, m, w):
    n = len(p)
    pairs = pair_partition(n, b)
    values = [{p[i], p[j]} for i, j in pairs]
    target_a = {m, w + 1}
    target_b = {m + 1, w}
    ia = [k for k, e in enumerate(values) if e == target_a]
    ib = [k for k, e in enumerate(values) if e == target_b]
    interval = set(range(m + 2, w))
    for a in ia:
        for bidx in ib:
            if a == bidx:
                continue
            if all(e.issubset(interval) or e.isdisjoint(interval)
                   for k, e in enumerate(values) if k not in (a, bidx)):
                return True
    return False


def apply_x(p, m, w):
    trans = {m: m + 1, m + 1: m, w: w + 1, w + 1: w}
    return canon(tuple(trans.get(x, x) for x in p))


def all_x(p):
    n = len(p)
    tested = 0
    out = []
    for b in range(n):
        for m in range(n):
            for w in range(m + 2, n - 1):
                tested += 1
                if legal_x(p, b, m, w):
                    out.append((b, m, w, apply_x(p, m, w)))
    return tested, out


def deletions(p):
    p = tuple(p)
    n = len(p)
    out = []
    for i in range(n):
        j = (i + 1) % n
        a, b = p[i], p[j]
        if abs(a - b) != 1:
            continue
        m = min(a, b)
        keep = [p[k] for k in range(n) if k not in (i, j)]
        keep = [x - 2 if x > m + 1 else x for x in keep]
        out.append(canon(tuple(keep)))
    return sorted(set(out))


p7 = (0, 2, 4, 6, 1, 3, 5)
q1 = (0, 7, 6, 2, 4, 8, 1, 3, 5)
q2 = (0, 7, 5, 3, 4, 8, 1, 2, 6)
q3 = (0, 5, 3, 1, 2, 6, 4)
q4 = (0, 3, 1, 4, 2)
source_trefoil = (3, 1, 4, 2, 0)

assert canon(p7) == p7
assert r_move(p7) == p7
assert s_move(p7) == p7
assert deletions(p7) == []
tested, moves = all_x(p7)
assert tested == 70
assert moves == []

# The displayed detour is checked in the reducing direction.
assert p7 in deletions(q1)
assert legal_x(q1, 4, 2, 5)
assert apply_x(q1, 2, 5) == q2
assert q3 in deletions(q2)
assert q4 in deletions(q3)
assert canon(source_trefoil) == q4

# Both cyclic classes of three-letter petal words delete to the one-petal word.
three = sorted({canon(p) for p in permutations(range(3))})
assert len(three) == 2
assert all((0,) in deletions(p) for p in three)

# Regression of the published crossing-exchange example.
example = (4, 2, 0, 6, 5, 1, 3)
assert legal_x(example, 6, 1, 4)
assert apply_x(example, 1, 4) == canon((5, 1, 0, 6, 4, 2, 3))

print('VERIFY_OK candidate_x_triples=70 candidate_R=fixed candidate_S=fixed '
      'candidate_Tminus=none detour_max_petals=9 trefoil_petals=5 source_X_example=PASS')
