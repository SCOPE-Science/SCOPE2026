#!/usr/bin/env python3
from itertools import product


def subsets(n):
    return [frozenset(i for i in range(n) if (m >> i) & 1) for m in range(1 << n)]


def contract_row(S, P, W):
    return S | (W - P) if S <= P else S


# Exhaustive set theorem through six worlds.
for n in range(1, 7):
    W = frozenset(range(n))
    ss = subsets(n)

    for P in ss:
        for S in ss:
            once = contract_row(S, P, W)
            twice = contract_row(once, P, W)
            assert twice == once

    for P in ss:
        for Q in ss:
            universal_commutation = True
            for S in ss:
                pq = contract_row(contract_row(S, P, W), Q, W)
                qp = contract_row(contract_row(S, Q, W), P, W)
                if pq != qp:
                    universal_commutation = False
                    break

            criterion = (P == Q) or (P | Q == W)
            assert universal_commutation == criterion, (n, P, Q)

            if not criterion:
                empty = frozenset()
                pq = contract_row(contract_row(empty, P, W), Q, W)
                qp = contract_row(contract_row(empty, Q, W), P, W)
                assert pq == W - P
                assert qp == W - Q
                assert pq != qp

                # A fresh propositional marker can distinguish the two rows.
                diff = pq ^ qp
                z = next(iter(diff))
                marker_true = W - {z}
                believes_pq = pq <= marker_true
                believes_qp = qp <= marker_true
                assert believes_pq != believes_qp


# Truth-function level check for one and two propositional atoms.
# A "model" needs only a set of propositional valuation types for the
# universal commutation condition, because relations are then arbitrary.
for atoms in range(1, 3):
    num_types = 1 << atoms
    all_types = range(num_types)
    functions = range(1 << num_types)

    def value(fun, t):
        return bool((fun >> t) & 1)

    for f in functions:
        for g in functions:
            equiv_taut = all(value(f, t) == value(g, t) for t in all_types)
            disj_taut = all(value(f, t) or value(g, t) for t in all_types)
            logical_criterion = equiv_taut or disj_taut

            universal = True
            # It suffices to inspect all nonempty sets of valuation types.
            for mask in range(1, 1 << num_types):
                types = [t for t in all_types if (mask >> t) & 1]
                P = {t for t in types if value(f, t)}
                Q = {t for t in types if value(g, t)}
                W = set(types)
                if not (P == Q or P | Q == W):
                    universal = False
                    break
            assert universal == logical_criterion, (atoms, f, g)

print('VERIFY_OK')
