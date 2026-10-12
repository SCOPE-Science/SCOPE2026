#!/usr/bin/env python3
"""Reproduce the minimal common-carrier separation of four intuitionistic modalities.

Python >=3.8, standard library only. Indices 0,1,2 denote the three-element
intuitionistic chain. Relation masks use bit (3*i+j) for the arrow i -> j.
"""
from itertools import product

OPERATORS = ("P", "B", "W", "N")
# P: Přenosil possibility, B: its box dual;
# W: Wijesekera possibility, N: its box dual.
WITNESSES = {
    "P": (35, 39),
    "B": (280, 408),
    "W": (279, 311),
    "N": (419, 435),
}


def relation(n, mask):
    return {(i, j) for i in range(n) for j in range(n)
            if (mask >> (n * i + j)) & 1}


def compose(a, b):
    return {(x, z) for x, y in a for v, z in b if y == v}


def transpose(a):
    return {(b, a) for a, b in a}


def is_preorder(n, le):
    return all((i, i) in le for i in range(n)) and compose(le, le) <= le


def upsets(n, le):
    return [frozenset(i for i in range(n) if mask >> i & 1)
            for mask in range(1 << n)
            if all(not (mask >> x & 1) or (mask >> y & 1)
                   for x, y in le)]


def confluences(le, r):
    ge = transpose(le)
    return {
        "f": compose(ge, r) <= compose(r, ge),
        "b": compose(r, le) <= compose(le, r),
        "d": compose(le, r) <= compose(r, le),
        "u": compose(r, ge) <= compose(ge, r),
    }


def evaluate_modalities(n, le, r, truth):
    out = []
    for op in OPERATORS:
        result = set()
        for s in range(n):
            predecessors = [t for t in range(n) if (t, s) in le]
            successors = [t for t in range(n) if (s, t) in le]
            if op == "P":
                holds = any((t, v) in r and v in truth
                            for t in predecessors for v in range(n))
            elif op == "B":
                holds = all(not ((t, v) in r) or v in truth
                            for t in successors for v in range(n))
            elif op == "W":
                holds = all(any((t, v) in r and v in truth
                                for v in range(n)) for t in successors)
            else:
                holds = any(all(not ((t, v) in r) or v in truth
                                for v in range(n)) for t in predecessors)
            if holds:
                result.add(s)
        out.append(frozenset(result))
    return tuple(out)


def signature(n, le, r):
    return tuple(tuple(evaluate_modalities(n, le, r, u)[k]
                       for u in upsets(n, le)) for k in range(4))


def admissible(which, conf):
    if which in ("P", "W"):
        return conf["b"] and conf["d"] and conf["u"]
    return conf["f"] and conf["b"] and conf["u"]


def check_two_point_lower_bound():
    statistics = []
    for n in (1, 2):
        orders = [relation(n, t) for t in range(1 << (n * n))
                  if is_preorder(n, relation(n, t))]
        assert len(orders) == (1 if n == 1 else 4)
        for op in OPERATORS:
            k = OPERATORS.index(op)
            frame_count = 0
            for le in orders:
                fingerprints = {}
                for rm in range(1 << (n * n)):
                    r = relation(n, rm)
                    if not admissible(op, confluences(le, r)):
                        continue
                    frame_count += 1
                    full = signature(n, le, r)
                    reduced = tuple(full[i] for i in range(4) if i != k)
                    if reduced in fingerprints:
                        assert fingerprints[reduced] == full[k], (n, op, le, rm)
                    fingerprints[reduced] = full[k]
            statistics.append((n, op, frame_count))
    return statistics


def check_three_point_witnesses():
    n = 3
    le = {(i, j) for i in range(n) for j in range(n) if i <= j}
    assert is_preorder(n, le)
    universe = upsets(n, le)
    assert universe == [frozenset(), frozenset({2}),
                        frozenset({1, 2}), frozenset({0, 1, 2})]
    discrepancies = []
    for op, (ra, rb) in WITNESSES.items():
        r, s = relation(n, ra), relation(n, rb)
        assert r <= s and len(s - r) == 1, (op, ra, rb)
        assert admissible(op, confluences(le, r))
        assert admissible(op, confluences(le, s))
        t, v = signature(n, le, r), signature(n, le, s)
        k = OPERATORS.index(op)
        assert all(t[j] == v[j] for j in range(4) if j != k)
        assert t[k] != v[k]
        u = frozenset({2})
        a, b = evaluate_modalities(n, le, r, u), evaluate_modalities(n, le, s, u)
        assert a[k] != b[k]
        assert all(a[j] == b[j] for j in range(4) if j != k)
        discrepancies.append((op, ra, rb, sorted(a[k]), sorted(b[k])))
    return discrepancies


if __name__ == "__main__":
    print("SMALL", check_two_point_lower_bound())
    print("WITNESSES", check_three_point_witnesses())
    print("VERIFY_OK")
