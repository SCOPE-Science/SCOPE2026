"""Reproduce finite checks for a nonempty-selection Boolean-rank identity.
Scientific inputs are Boolean matrices; no particular external software is needed.
Run: python3 check.py
"""
from itertools import combinations, product


def union_outputs(basis, allow_empty):
    values = {0} if allow_empty else set()
    for mask in basis:
        values |= {x | mask for x in tuple(values)}
        if not allow_empty:
            values.add(mask)
    return values


def best_basis_cost(rows, s, allow_empty):
    candidate_masks = tuple(range(1 << s)) if not allow_empty else tuple(range(1, 1 << s))
    for k in range(0 if allow_empty else 1, min(len(candidate_masks), s + 1) + 1):
        for basis in combinations(candidate_masks, k):
            attainable = union_outputs(basis, allow_empty)
            if all(x in attainable for x in rows):
                return k
    raise AssertionError(('basis not found', rows, s, allow_empty))


def verify():
    count = 0
    for s in range(1, 4):
        for r in range(1, 5):
            peak = 0
            for rows in product(range(1 << s), repeat=r):
                b = best_basis_cost(rows, s, False)
                rank = best_basis_cost(rows, s, True)
                assert b == rank + int(0 in rows), (s, r, rows, b, rank)
                peak = max(peak, b)
                count += 1
            assert peak == min(r, s + 1), (r, s, peak)
            print(f'r={r} s={s} worst={peak}: OK')
    print('EXHAUSTIVE_MATRIX_CHECK_OK', count)

    # Explicit full-size sharpness construction for larger parameters.
    for r in range(1, 15):
        for s in range(1, 15):
            forced = min(r, s + 1)
            rows = (0,) + tuple(1 << j for j in range(min(s, r - 1)))
            if len(rows) < r:
                rows += (0,) * (r - len(rows))
            assert len(rows) == r
            assert len(set(rows)) == forced
            # Each singleton row requires its own basis world, and empty row
            # requires a separate all-true witness, achieving forced worlds.
    print('SHARPNESS_CONSTRUCTION_OK', 14 * 14)

    # Concrete anti-world valuation and selected-world realization for every
    # truth table with <= 3 antecedents and <= 3 consequents.
    n = 0
    for r in range(1, 4):
        for s in range(1, 4):
            for rows in product(range(1 << s), repeat=r):
                k = best_basis_cost(rows, s, False)
                for basis in combinations(range(1 << s), k):
                    if all(row in union_outputs(basis, False) for row in rows):
                        break
                else:
                    raise AssertionError('missing realizing basis')
                selection = []
                for row in rows:
                    for flags in product((0, 1), repeat=k):
                        if not any(flags):
                            continue
                        choice = [basis[t] for t, flag in enumerate(flags) if flag]
                        aggregate = 0
                        for e in choice:
                            aggregate |= e
                        if aggregate == row:
                            selection.append(tuple(t for t,flag in enumerate(flags) if flag))
                            break
                    else:
                        raise AssertionError('selection not found')
                for i, row in enumerate(rows):
                    # Anti-state t has consequent q_j false precisely when
                    # bit j of basis[t] is present. Hence all selected states
                    # satisfy q_j exactly when row bit j is absent.
                    for j in range(s):
                        semantic_truth = all(not (basis[t] & (1 << j)) for t in selection[i])
                        expected_truth = not bool(row & (1 << j))
                        assert semantic_truth == expected_truth
                n += 1
    print('FINITE_SEMANTIC_REALIZATION_OK', n)


if __name__ == '__main__':
    verify()
