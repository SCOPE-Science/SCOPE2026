"""Exact finite checks for a permutation-incidence closure theorem.

Objects are fixed-point-free permutations, attributes are allowed board cells.
All computations are integers and use only the Python standard library.
"""
from itertools import permutations
from math import comb, factorial


def rook_number(n, k):
    return sum((-1)**j * comb(n, j) * comb(n-j, k-j)**2 * factorial(k-j)
               for j in range(k+1))


def derangements(n):
    return sum((-1)**j * comb(n, j) * factorial(n-j) for j in range(n+1))


def two_hole_count(n):
    return (comb(n, 2) * comb(n-2, 2) *
            sum((-1)**j * comb(n-4, j) * factorial(n-2-j)
                for j in range(n-3)))


def context(n):
    cells = [(i, j) for i in range(n) for j in range(n) if i != j]
    index = {e: z for z, e in enumerate(cells)}
    objects = [sum(1 << index[i, p[i]] for i in range(n))
               for p in permutations(range(n)) if all(p[i] != i for i in range(n))]
    top = (1 << len(cells)) - 1

    def close(mask):
        present = [p for p in objects if p & mask == mask]
        if not present:
            return top
        common = present[0]
        for p in present[1:]:
            common &= p
        return common

    masks = []

    def walk(i, mask, used):
        if i == n:
            masks.append(mask)
            return
        walk(i+1, mask, used)
        for j in range(n):
            if i != j and not (used & (1 << j)):
                walk(i+1, mask | (1 << index[i, j]), used | (1 << j))

    walk(0, 0, 0)
    return cells, index, objects, top, close, masks


def check(n):
    cells, idx, objects, top, close, masks = context(n)
    closed = {top}
    actual_rook = [0] * (n+1)
    actual_good = 0
    for mask in masks:
        k = mask.bit_count()
        actual_rook[k] += 1
        c = close(mask)
        closed.add(c)
        if n >= 4:
            used_rows = {cells[i][0] for i in range(len(cells)) if mask & (1 << i)}
            used_cols = {cells[i][1] for i in range(len(cells)) if mask & (1 << i)}
            remaining_rows = set(range(n)) - used_rows
            remaining_cols = set(range(n)) - used_cols
            good = (k <= n-3 or
                    (k == n-2 and remaining_rows.isdisjoint(remaining_cols)) or
                    (k == n and mask in objects))
            if k == n-2 and remaining_rows.isdisjoint(remaining_cols):
                actual_good += 1
            if good:
                assert c == mask, (n, 'expected-closed', k, mask, c)
            else:
                assert c in objects or c == top, (n, 'expected-top-or-object', k, mask, c)
    if n >= 4:
        expected = 1 + sum(rook_number(n, k) for k in range(n-2)) + two_hole_count(n) + derangements(n)
        assert actual_good == two_hole_count(n)
        assert len(closed) == expected
    else:
        expected = len(closed)
        assert n == 3 and expected == 4
    assert len(objects) == derangements(n)
    assert actual_rook == [rook_number(n, k) for k in range(n+1)]
    if n == 4:
        assert len({close(mask) for mask in range(1 << len(cells))}) == len(closed)
    if 4 <= n <= 6:
        # Build explicit finite Horn rules, independently replay forward
        # chaining and compare with the Galois double derivation.
        exceptional = []
        for premise in masks:
            if premise.bit_count() != n-2:
                continue
            rows = {cells[t][0] for t in range(len(cells)) if premise & (1 << t)}
            cols = {cells[t][1] for t in range(len(cells)) if premise & (1 << t)}
            if (set(range(n))-rows) & (set(range(n))-cols):
                exceptional.append((premise, close(premise)))

        def forward(b):
            while True:
                chosen = [cells[z] for z in range(len(cells)) if b & (1 << z)]
                if (len({e[0] for e in chosen}) != len(chosen) or
                    len({e[1] for e in chosen}) != len(chosen)):
                    return top  # a conflict-pair Horn rule
                nxt = b
                for antecedent, consequent in exceptional:
                    if (b & antecedent) == antecedent:
                        nxt |= consequent
                if nxt == b:
                    return b
                b = nxt

        for premise in masks:
            assert forward(premise) == close(premise), ('Horn replay mismatch', n, premise)
        for i, e in enumerate(cells):
            for j in range(i):
                mask = (1 << i) | (1 << j)
                assert forward(mask) == close(mask)

    if n in (4, 5):
        # Every simultaneous row/column permutation and transposition is a
        # closure-preserving automorphism, and these maps are all distinct.
        atom_actions = set()
        for sigma in permutations(range(n)):
            for swap in (0, 1):
                image = tuple(idx[(sigma[j], sigma[i]) if swap else (sigma[i], sigma[j])]
                              for i, j in cells)
                atom_actions.add(image)
                for mask in closed:
                    transported = sum(1 << image[z] for z in range(len(cells)) if mask & (1 << z))
                    assert transported in closed
        assert len(atom_actions) == 2 * factorial(n)
    print(f'CASE n={n} derangements={len(objects)} partial_matchings={len(masks)}'
          f' two_hole={actual_good} concepts={len(closed)} PASS')


if __name__ == '__main__':
    for size in range(3, 8):
        check(size)
    print('VERIFY_OK exact_closures=PASS inclusion_exclusion=PASS two_hole_boundary=PASS'
          ' automorphism_generators=PASS horn_forward_chaining=PASS n=3..7')
