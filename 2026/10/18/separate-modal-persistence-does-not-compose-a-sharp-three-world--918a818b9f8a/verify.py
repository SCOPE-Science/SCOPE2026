#!/usr/bin/env python3
"""Finite semantic cross-checks of a three-point fusion-model counterexample.

The model-theoretic assertions for arbitrary formulas are proved by
closure arguments in RESULT.md; this executable independently verifies
those finite closure calculations and exhaustively checks tiny frames.
"""

from itertools import product


def bits(mask, n):
    return frozenset(i for i in range(n) if mask & (1 << i))


def preorders(n):
    mask = (1 << n) - 1
    for encoded in range(1 << (n * n)):
        order = tuple((encoded >> (i * n)) & mask for i in range(n))
        if not all((order[i] >> i) & 1 for i in range(n)):
            continue
        if any(order[j] & ~order[i]
               for i in range(n)
               for j in range(n)
               if order[i] & (1 << j)):
            continue
        yield order


def upsets(order):
    n = len(order)
    return frozenset(x for x in range(1 << n)
                     if all(not (x & (1 << i)) or (order[i] & ~x) == 0
                            for i in range(n)))


def imp(a, b, order):
    wrong = a & ~b
    return sum(1 << i for i, above in enumerate(order)
               if not (above & wrong))


def box(a, relation):
    return sum(1 << i for i, succ in enumerate(relation)
               if (succ & ~a) == 0)


def dia(a, relation):
    return sum(1 << i for i, succ in enumerate(relation)
               if succ & a)


def closure(atoms, order, relation, allow_box, allow_dia):
    """Complete subalgebra on the finite carrier; no formula-depth cutoff."""
    top = (1 << len(order)) - 1
    seen = {0, top, *atoms}
    while True:
        previous = len(seen)
        new = set(seen)
        for a in seen:
            if allow_box:
                new.add(box(a, relation))
            if allow_dia:
                new.add(dia(a, relation))
            for b in seen:
                new.update((a & b, a | b, imp(a, b, order)))
        seen = new
        if len(seen) == previous:
            return frozenset(seen)


def example():
    # 0=a, 1=b, 2=c; a<=b is the only nontrivial comparison.
    order = (0b011, 0b010, 0b100)
    relation = (0b001, 0b101, 0b001)
    p = 0b110
    ups = upsets(order)
    assert ups == frozenset({0, 0b010, 0b011, 0b100, 0b110, 0b111})
    only_box = closure([p], order, relation, True, False)
    only_dia = closure([p], order, relation, False, True)
    mixed = closure([p], order, relation, True, True)
    assert only_box == frozenset({0, p, 0b111}), only_box
    assert only_dia == ups, (only_dia, ups)
    assert all(dia(a, relation) in ups for a in ups)
    assert all(a in ups for a in only_box | only_dia)
    dp = dia(p, relation)
    conditional = imp(p, dp, order)
    failure = box(conditional, relation)
    assert dp == 0b010
    assert conditional == 0b011
    assert failure == 0b101
    assert failure in mixed and failure not in ups
    assert failure & 0b001 and not (failure & 0b010)
    print('WITNESS_OK: all-unimodal-truth-sets-upward; box(p->dia(p))={a,c}')
    return len(only_box), len(only_dia), len(mixed)


def exhaustive_two_point_check():
    total = 0
    qualifying = 0
    for n in (1, 2):
        top = (1 << n) - 1
        for order in preorders(n):
            ups = upsets(order)
            for encoded in range(1 << (n * n)):
                relation = tuple((encoded >> (i * n)) & top for i in range(n))
                # Two independent letters give an additional finite regression test;
                # the unrestricted-vocabulary lower bound is proved separately.
                for atoms in product(sorted(ups), repeat=2):
                    total += 1
                    b = closure(atoms, order, relation, True, False)
                    d = closure(atoms, order, relation, False, True)
                    if not b.issubset(ups) or not d.issubset(ups):
                        continue
                    qualifying += 1
                    both = closure(atoms, order, relation, True, True)
                    assert both.issubset(ups), (n, order, relation, atoms, both)
    print('TWO_POINT_EXHAUSTIVE_OK: configurations=', total,
          'unimodally_persistent=', qualifying)
    return total, qualifying


if __name__ == '__main__':
    print('FINITE_MODEL_VERIFY_START')
    sizes = example()
    print('UNIMODAL_CLOSURES:', sizes)
    exhaustive_two_point_check()
    print('LOCAL_PERSISTENCE_COUNTEREXAMPLE_VERIFY_OK')
