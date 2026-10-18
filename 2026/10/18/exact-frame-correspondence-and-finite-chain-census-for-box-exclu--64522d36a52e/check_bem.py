#!/usr/bin/env python3
"""Finite reproducibility checks for box excluded middle on birelational frames.

A finite intuitionistic valuation is an upward-closed subset of the carrier.
The mathematical correspondence is proved separately, for all cardinalities.
"""


def posets(n):
    for code in range(1 << (n * (n - 1))):
        rows = [1 << i for i in range(n)]
        bit = 0
        for x in range(n):
            for y in range(n):
                if x != y:
                    rows[x] |= ((code >> bit) & 1) << y
                    bit += 1
        if any(x != y and (rows[x] >> y & 1) and (rows[y] >> x & 1)
               for x in range(n) for y in range(n)):
            continue
        if any((rows[x] >> y & 1) and (rows[y] & ~rows[x])
               for x in range(n) for y in range(n)):
            continue
        yield tuple(rows)


def rows_of_relation(n, code):
    mask = (1 << n) - 1
    return tuple((code >> (x * n)) & mask for x in range(n))


def is_base_frame(order, R, n):
    return all(not (order[x] >> y & 1) or not (R[y] & ~R[x])
               for x in range(n) for y in range(n))


def exact_correspondent(order, R, n):
    return all(not (order[x] >> y & 1)
               or all(any((R[y] >> t & 1) and (order[t] >> z & 1)
                          for t in range(n))
                      for z in range(n) if R[x] >> z & 1)
               for x in range(n) for y in range(n))


def all_atomic_instances(order, R, n):
    # Directly interpret Box p and intuitionistic negation over all upsets.
    for U in range(1 << n):
        if any((U >> x & 1) and (order[x] & ~U) for x in range(n)):
            continue
        box = [not (R[x] & ~U) for x in range(n)]
        for x in range(n):
            not_box = all(not box[y] for y in range(n)
                          if order[x] >> y & 1)
            if not (box[x] or not_box):
                return False
    return True


def check_all_posets():
    expected_base = {1: 2, 2: 34, 3: 2942}
    expected_valid = {1: 2, 2: 26, 3: 1262}
    for n in (1, 2, 3):
        base = valid = 0
        for order in posets(n):
            for code in range(1 << (n * n)):
                R = rows_of_relation(n, code)
                if not is_base_frame(order, R, n):
                    continue
                base += 1
                predicted = exact_correspondent(order, R, n)
                observed = all_atomic_instances(order, R, n)
                assert predicted == observed, (n, order, R, predicted, observed)
                valid += observed
        assert (base, valid) == (expected_base[n], expected_valid[n])
        print('posets n=%d: %d basic frames, %d validating frames' % (n, base, valid))


def check_chains():
    for n in (1, 2, 3, 4):
        order = tuple(((1 << n) - 1) & ~((1 << i) - 1)
                      for i in range(n))
        count = strong = 0
        for code in range(1 << (n * n)):
            R = rows_of_relation(n, code)
            if not is_base_frame(order, R, n):
                continue
            count += exact_correspondent(order, R, n)
            strong += all(R[x] == R[y] for x in range(n) for y in range(n))
        formula = 1 + ((n + 1) ** n - 1) // n
        assert count == formula and strong == 2 ** n
        print('chain n=%d: valid=%d, strong=%d' % (n, count, strong))
    # The two-world smallest counterexample.
    order, R = (0b11, 0b10), (0b11, 0b01)
    assert is_base_frame(order, R, 2)
    assert exact_correspondent(order, R, 2)
    assert all_atomic_instances(order, R, 2)
    assert R[0] != R[1]
    print('two-world strict witness: verified')


if __name__ == '__main__':
    check_all_posets()
    check_chains()
    print('All checks passed')
