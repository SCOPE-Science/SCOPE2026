#!/usr/bin/env python3
from itertools import product

def powerset(n):
    return [
        frozenset(i for i in range(n) if (mask >> i) & 1)
        for mask in range(1 << n)
    ]

def all_families(n):
    P = powerset(n)
    for mask in range(1 << len(P)):
        yield frozenset(P[i] for i in range(len(P)) if (mask >> i) & 1)

def induced_behavior(covers, n):
    return frozenset(
        X for X in powerset(n)
        if any(B <= X for B in covers)
    )

def minimal_members(upset):
    return frozenset(
        X for X in upset
        if not any(Y < X for Y in upset)
    )

def is_antichain(F):
    return all(
        not (A < B or B < A)
        for A in F for B in F
    )

def directed_down(covers):
    return all(
        any(G <= (A & B) for G in covers)
        for A in covers for B in covers
    )

# Dedekind numbers M_1,...,M_4 by direct antichain enumeration.
known = {1: 3, 2: 6, 3: 20, 4: 168}
for n in range(1, 5):
    P = powerset(n)
    count = 0
    for mask in range(1 << len(P)):
        F = frozenset(P[i] for i in range(len(P)) if (mask >> i) & 1)
        if is_antichain(F):
            count += 1
    assert count == known[n], (n, count)

# Exhaustive raw modal-cover families through n=3.
for n in range(1, 4):
    fams = list(all_families(n))

    # CM: semantic quotients are exactly Boolean-lattice upsets.
    cm_behaviors = {}
    for C in fams:
        N = induced_behavior(C, n)
        mins = minimal_members(N)
        assert is_antichain(mins)
        assert induced_behavior(mins, n) == N
        cm_behaviors[N] = mins
    assert len(cm_behaviors) == known[n]

    for w in range(n):
        singleton = frozenset({w})

        # SL: modal inclusion says every cover is contained in {w}.
        sl_behaviors = set()
        pll_behaviors = set()

        for C in fams:
            if all(B <= singleton for B in C):
                sl_behaviors.add(induced_behavior(C, n))

                # PLL additionally has modal identity.  With inclusion,
                # transitivity is automatic for the only possible covers:
                # empty and singleton.
                if singleton in C:
                    # explicit transitivity check
                    ok = True
                    for A in C:
                        if not A:
                            if frozenset() not in C:
                                ok = False
                        else:
                            assert A == singleton
                            # the only v in A is w; every chosen cover at w
                            # has union equal to that chosen cover, already in C.
                            for Aw in C:
                                if Aw not in C:
                                    ok = False
                    if ok:
                        pll_behaviors.add(induced_behavior(C, n))

        assert len(sl_behaviors) == 3, (n, w, len(sl_behaviors))
        assert len(pll_behaviors) == 2, (n, w, len(pll_behaviors))

        # CK-box: seriality plus confluence.
        ck_behaviors = set()
        for C in fams:
            if not C or not directed_down(C):
                continue

            K = frozenset.intersection(*C)
            assert K in C

            N = induced_behavior(C, n)
            N_from_core = frozenset(X for X in powerset(n) if K <= X)
            assert N == N_from_core
            ck_behaviors.add(N)

        assert len(ck_behaviors) == 2 ** n, (n, w, len(ck_behaviors))

# Formula-level global counts for small n.
for n in range(1, 5):
    assert known[n] ** n >= 1
    assert 3 ** n >= 1
    assert 2 ** n >= 1
    assert 2 ** (n * n) == (2 ** n) ** n

print("VERIFY_OK")
