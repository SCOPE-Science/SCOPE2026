#!/usr/bin/env python3
from itertools import product

def nonempty_subsets(n):
    out = []
    for mask in range(1, 1 << n):
        out.append(frozenset(i for i in range(n) if (mask >> i) & 1))
    return out

def nonempty_families(n):
    subs = nonempty_subsets(n)
    out = []
    for mask in range(1, 1 << len(subs)):
        out.append(frozenset(subs[i] for i in range(len(subs)) if (mask >> i) & 1))
    return out

def union_family(F):
    u = set()
    for s in F:
        u.update(s)
    return frozenset(u)

def independent(families):
    for chosen in product(*[tuple(F) for F in families]):
        inter = set(chosen[0])
        for s in chosen[1:]:
            inter.intersection_update(s)
        if not inter:
            return False
    return True

def build_and_check(families):
    O = sorted(union_family(families[0]))
    assert O
    assert all(union_family(F) == frozenset(O) for F in families)
    assert independent(families)

    idx = {x: i for i, x in enumerate(O)}
    r = len(O)

    actions = []
    for F in families:
        A = []
        for s in sorted(F, key=lambda x: (len(x), tuple(sorted(x)))):
            for v in O:
                A.append((s, v))
        actions.append(A)

    def gout(profile):
        chosen_sets = [a[0] for a in profile]
        I = set(chosen_sets[0])
        for s in chosen_sets[1:]:
            I.intersection_update(s)
        assert I

        residue = sum(idx[a[1]] for a in profile) % r
        candidate = O[residue]
        if candidate in I:
            return candidate
        return min(I)

    for ai, A in enumerate(actions):
        other_axes = [actions[j] for j in range(len(actions)) if j != ai]
        for action in A:
            got = set()
            for others in product(*other_axes):
                profile = []
                k = 0
                for j in range(len(actions)):
                    if j == ai:
                        profile.append(action)
                    else:
                        profile.append(others[k])
                        k += 1
                got.add(gout(tuple(profile)))
            assert got == set(action[0]), (families, ai, action, got)

    for ai, A in enumerate(actions):
        induced = {a[0] for a in A}
        assert induced == set(families[ai])

counts = {}
for n in range(1, 4):
    fams = nonempty_families(n)
    checked = 0
    for F, G in product(fams, repeat=2):
        if union_family(F) != union_family(G):
            continue
        if not independent((F, G)):
            continue
        build_and_check((F, G))
        checked += 1
    counts[("two", n)] = checked

for n in range(1, 3):
    fams = nonempty_families(n)
    checked = 0
    for Fs in product(fams, repeat=3):
        u = union_family(Fs[0])
        if not all(union_family(F) == u for F in Fs):
            continue
        if not independent(Fs):
            continue
        build_and_check(Fs)
        checked += 1
    counts[("three", n)] = checked

for r in range(1, 13):
    O = frozenset(range(r))
    F = frozenset([O])
    build_and_check((F, F))
    compressed_actions_each = len(F) * len(O)
    assert compressed_actions_each == r

    for m in range(r):
        assert m < r

print("CHECKED", counts)
print("VERIFY_OK")
