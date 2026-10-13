#!/usr/bin/env python3
"""Exact finite replay for order-refinement monotonicity of canonical inquisitive-algebra sizes."""
from itertools import combinations, product
from collections import Counter

checks = 0


def all_posets(n):
    pairs = list(combinations(range(n), 2))
    out = []
    for choices in product((0, 1, 2), repeat=len(pairs)):
        # rel[i] is the bitset of elements >= i; reflexivity is built in.
        rel = [1 << i for i in range(n)]
        for (i, j), c in zip(pairs, choices):
            if c == 1:
                rel[i] |= 1 << j
            elif c == 2:
                rel[j] |= 1 << i

        # The chosen orientation must already be transitive.
        closure = rel[:]
        changed = True
        while changed:
            changed = False
            for i in range(n):
                r = closure[i]
                nr = r
                for j in range(n):
                    if (r >> j) & 1:
                        nr |= closure[j]
                if nr != closure[i]:
                    closure[i] = nr
                    changed = True
        if closure != rel:
            continue

        # Antisymmetry.
        if any(((rel[i] >> j) & 1) and ((rel[j] >> i) & 1)
               for i in range(n) for j in range(i + 1, n)):
            continue
        out.append(tuple(rel))
    return out


def upsets(rel):
    n = len(rel)
    ans = []
    for s in range(1 << n):
        if all(not ((s >> i) & 1) or not (rel[i] & ~s) for i in range(n)):
            ans.append(s)
    return ans


def nonempty_downsets_of_upset_lattice(rel):
    U = upsets(rel)
    k = len(U)
    lower = []
    for a in U:
        mask = 0
        for j, b in enumerate(U):
            if (b & ~a) == 0:  # b subseteq a
                mask |= 1 << j
        lower.append(mask)

    ds = []
    for d in range(1, 1 << k):
        bits = d
        ok = True
        while bits:
            lsb = bits & -bits
            i = lsb.bit_length() - 1
            if lower[i] & ~d:
                ok = False
                break
            bits -= lsb
        if ok:
            ds.append(d)
    return U, ds


def rel_subset(p, q):
    return all((a & ~b) == 0 for a, b in zip(p, q))


def is_antichain(rel):
    return all(r == (1 << i) for i, r in enumerate(rel))


def is_chain(rel):
    n = len(rel)
    for i in range(n):
        for j in range(i + 1, n):
            if not (((rel[i] >> j) & 1) or ((rel[j] >> i) & 1)):
                return False
    return True


expected_posets = {1: 1, 2: 3, 3: 19, 4: 219}
expected_distributions = {
    1: {2: 1},
    2: {3: 2, 5: 1},
    3: {4: 6, 6: 6, 9: 6, 19: 1},
    4: {5: 24, 7: 36, 9: 6, 10: 48, 13: 24, 14: 24,
        19: 12, 20: 8, 26: 24, 49: 12, 167: 1},
}
# Dedekind M_n for n <= 4; the canonical antichain carrier has M_n - 1 elements.
dedekind = {1: 3, 2: 6, 3: 20, 4: 168}

refinement_pairs = 0
injection_images_checked = 0

for n in range(1, 5):
    ps = all_posets(n)
    assert len(ps) == expected_posets[n]
    checks += 1

    data = {}
    for p in ps:
        U, D = nonempty_downsets_of_upset_lattice(p)
        data[p] = (U, D)
        checks += 1

    dist = Counter(len(data[p][1]) for p in ps)
    assert dict(sorted(dist.items())) == expected_distributions[n]
    checks += 1

    # Sharp endpoint characterization.
    for p in ps:
        size = len(data[p][1])
        assert n + 1 <= size <= dedekind[n] - 1
        checks += 1
        assert (size == n + 1) == is_chain(p)
        checks += 1
        assert (size == dedekind[n] - 1) == is_antichain(p)
        checks += 1

    # Every strict order refinement strictly lowers the carrier size.
    # Also replay the proof injection D |-> down_{Up(P)} D and its recovery by intersection.
    for p in ps:
        Up, Dp = data[p]
        idxp = {s: i for i, s in enumerate(Up)}
        for q in ps:
            if p == q or not rel_subset(p, q):
                continue
            refinement_pairs += 1
            Uq, Dq = data[q]
            assert set(Uq) < set(Up)
            checks += 1
            assert len(Dq) < len(Dp)
            checks += 1

            # Map a downset of Up(Q) to its downward closure inside Up(P).
            images = set()
            Uq_index = {s: i for i, s in enumerate(Uq)}
            for d in Dq:
                chosen = [Uq[i] for i in range(len(Uq)) if (d >> i) & 1]
                image = 0
                for j, a in enumerate(Up):
                    if any((a & ~b) == 0 for b in chosen):
                        image |= 1 << j
                assert image in Dp
                checks += 1
                # Restricting back to Up(Q) recovers d exactly.
                recovered = 0
                for s, i_q in Uq_index.items():
                    if (image >> idxp[s]) & 1:
                        recovered |= 1 << i_q
                assert recovered == d
                checks += 1
                images.add(image)
                injection_images_checked += 1
            assert len(images) == len(Dq)
            checks += 1

print(
    f"VERIFY_OK {checks} exact assertions; "
    f"{sum(expected_posets.values())} labeled posets; "
    f"{refinement_pairs} strict refinements; "
    f"{injection_images_checked} injection images"
)
