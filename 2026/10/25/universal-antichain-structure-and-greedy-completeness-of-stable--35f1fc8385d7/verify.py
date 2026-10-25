#!/usr/bin/env python3
"""Finite checks of antichain realization under substitutability and persistence.

The exhaustive cases below supplement, but do not replace, the arbitrary-size proof.
"""
from itertools import permutations


def subsets(n):
    return tuple(range(1 << n))


def inc(a, b):
    return (a & b) == a


def count_bits(x):
    return x.bit_count()


def maximal_feasible(faces):
    return {u for u in faces if not any(u != v and inc(u, v) for v in faces)}


def run():
    global c_sub, c_irp, c_block, c_order
    c_sub = c_irp = c_block = c_order = 0
    ncases = 0
    for n in range(5):
        allsets = subsets(n)
        # Enumerate each downward-closed set system exactly once via its facets.
        for flag in range(1, 1 << (1 << n)):
            family = {s for s in allsets if flag & (1 << s)}
            if any((t not in family) for s in family for t in allsets if inc(t, s)):
                continue
            faces = family
            facets = maximal_feasible(faces)
            # Central firm's choice: accept entire menu if feasible, else nothing.
            def choice(S):
                return S if S in faces else 0
            assert 0 in faces
            for A in allsets:
                for B in allsets:
                    if inc(A, B):
                        assert inc(choice(B) & A, choice(A))
                        c_sub += 1
                if choice(A) == A:
                    for k in range(n):
                        x = 1 << k
                        if A & x:
                            continue
                        B = A | x
                        if choice(B) & x:
                            assert (choice(B) & A) == A
                        c_irp += 1
            observed_stable = set()
            for M in allsets:
                if M not in faces:
                    continue
                blocked = False
                for Z in allsets:
                    if not Z or M & Z:
                        continue
                    # Workers have independent accept-all singleton choice, hence
                    # each proposed edge is acceptable to its worker.
                    if choice(M | Z) & Z == Z:
                        blocked = True
                        break
                if not blocked:
                    observed_stable.add(M)
                c_block += 1
            assert observed_stable == facets, (n, family, observed_stable, facets)
            possible = set()
            for order in permutations(range(n)):
                H = 0
                for k in order:
                    x = 1 << k
                    if choice(H | x) & x:
                        H = choice(H | x)
                    assert H in faces
                possible.add(H)
                c_order += 1
            assert possible == facets, (n, family, possible, facets)
            ncases += 1
        print(f"n={n}: validated every nonempty downward-closed family on {n} labels")
    print(f"PASS families={ncases} SUB comparisons={c_sub} IRP pairs={c_irp} CY checks={c_block} SMA orders={c_order}")
    assert ncases == 1 + 2 + 5 + 19 + 167
    # Illustrative nonuniform-cardinality stable family.
    faces = {0, 1, 2, 4, 6}
    assert maximal_feasible(faces) == {1, 6}
    print("Example facets: {x1} and {x2,x3}; both reachable by suitable arrival orders")


def check_all_three_contract_choice_functions():
    """Supplementary test of arbitrary SUB+IRP firm choices, not only constructed ones."""
    from itertools import product
    n = 3
    menus = tuple(range(1 << n))
    options = [tuple(s for s in menus if inc(s, m)) for m in menus]
    valid = 0
    for table in product(*options):
        def choice(m):
            return table[m]
        if any((choice(B) & A) & ~choice(A) for A in menus for B in menus if inc(A, B)):
            continue
        feasible = {m for m in menus if choice(m) == m}
        if any(((choice(S | (1 << k)) & (1 << k)) and
                (choice(S | (1 << k)) & S) != S)
               for S in feasible for k in range(n) if not S & (1 << k)):
            continue
        valid += 1
        stable = {M for M in feasible if not any(
            Z and not Z & M and choice(M | Z) & Z == Z
            for Z in menus)}
        assert stable == maximal_feasible(feasible)
        reached = set()
        for order in permutations(range(n)):
            h = 0
            for k in order:
                x = 1 << k
                if choice(h | x) & x:
                    h = choice(h | x)
                assert h in feasible
            reached.add(h)
        assert reached == stable
    print(f"PASS arbitrary 3-contract firm choices satisfying SUB+IRP: {valid} functions")


if __name__ == '__main__':
    run()
    check_all_three_contract_choice_functions()
