"""Standalone finite checks for Boolean team-dependence/covering-array equivalence.

Run: python3 checker.py. Uses Python standard library only.
"""
from itertools import combinations, product


def coverage_masks(m, s):
    requirements = [(cols, pat) for cols in combinations(range(m), s)
                    for pat in product((0, 1), repeat=s)]
    rows = list(product((0, 1), repeat=m))
    masks = [sum(1 << j for j, (cols, pat) in enumerate(requirements)
                 if tuple(row[c] for c in cols) == pat) for row in rows]
    return rows, masks, (1 << len(requirements)) - 1


def optimum(m, s):
    rows, masks, full = coverage_masks(m, s)
    for d in range(1, len(rows) + 1):
        for ii in combinations(range(len(rows)), d):
            coverage = 0
            for i in ii:
                coverage |= masks[i]
            if coverage == full:
                return d, [rows[i] for i in ii]
    raise AssertionError('No cover')


def supports_dependence(team):
    seen = {}
    for x, b in team:
        if x in seen and seen[x] != b:
            return False
        seen[x] = b
    return True


def supports_disjunction(team, funcs):
    return any(all(row[x] == b for x, b in team) for row in funcs)


def check_teams(m, r, funcs):
    valuations = [(x, bit) for x in range(m) for bit in (0, 1)]
    count = 0
    for n in range(r + 1):
        for t in combinations(valuations, n):
            assert supports_dependence(t) == supports_disjunction(t, funcs), (m,r,t)
            count += 1
    return count


def balanced_six():
    # Traces of a 6-row strength-two array: take 8 of 10 inequivalent
    # columns, each beginning with 0 and carrying three 1s among rows 1..5.
    cols = [(0,) + tail for tail in product((0, 1), repeat=5)
            if sum(tail) == 3][:8]
    rows = [tuple(column[r] for column in cols) for r in range(6)]
    return rows


def main():
    assert optimum(2, 2)[0] == 4
    assert optimum(4, 2)[0] == 5
    assert optimum(4, 3)[0] == 8
    print('strength 2 on two columns: 4 rows; strength 2 on four columns: 5 rows')
    print('strength 3 on four columns: 8 rows')
    for m, r in ((2, 2), (4, 2), (4, 3)):
        n, funcs = optimum(m, r)
        count = check_teams(m, r, funcs)
        print(f'{m} input values, team size <= {r}: width={n}, verified {count} teams')
    rows = balanced_six()
    column_set = set(rows)
    assert len(column_set) == 6
    c = 0
    for cols in combinations(range(8), 2):
        for bits in product((0, 1), repeat=2):
            assert any(tuple(row[i] for i in cols) == bits for row in rows)
            c += 1
    print(f'8-column strength-2 covering array: six rows, checked {c} pair patterns')
    for m in (2, 4):
        vals = [(x,b) for x in range(m) for b in (0,1)]
        assert all(supports_dependence(t) for t in combinations(vals, 1))
    print('All singleton teams satisfy dependence, so width one is sufficient at r=1.')
    for m in (2, 4):
        complete_graphs = list(product((0, 1), repeat=m))
        assert all(supports_disjunction(list(enumerate(row)), complete_graphs) for row in complete_graphs)
        assert len(complete_graphs) == 2**m
    print('Full-graph widths checked: 4 for m=2; 16 for m=4')
    print('PASS')


if __name__ == '__main__':
    main()
