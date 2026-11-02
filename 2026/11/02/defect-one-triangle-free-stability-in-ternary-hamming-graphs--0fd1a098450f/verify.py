"""Standalone small-order checks for ternary coordinate-line near-extremizers."""
from itertools import combinations, permutations, product
from math import comb


def words(n):
    return list(product(range(3), repeat=n))


def lines(n):
    w = words(n)
    idx = {x: i for i, x in enumerate(w)}
    out = []
    for d in range(n):
        for fixed in product(range(3), repeat=n-1):
            row = []
            for t in range(3):
                x = list(fixed)
                x.insert(d, t)
                row.append(idx[tuple(x)])
            out.append(tuple(row))
    return out


def line_cover(A, ln):
    return all(any(v in A for v in line) for line in ln)


def max_complements(n):
    w = words(n)
    out = set()
    for coeff in product((1, 2), repeat=n - 1):
        coeff = (1,) + coeff
        for c in range(3):
            out.add(frozenset(i for i, x in enumerate(w)
                              if sum(a * b for a, b in zip(coeff, x)) % 3 == c))
    assert len(out) == 3 * 2 ** (n-1)
    return out


def test(n):
    w = words(n)
    ln = lines(n)
    k = 3 ** (n - 1) + 1
    if n == 2:
        allsets = (frozenset(c) for c in combinations(range(9), 4))
    elif n == 3:
        # Partition into three z-layers, with point indices 0..26 ordered xyz.
        patterns = {s: [] for s in (3,4)}
        local_lines = lines(2)
        for s in (3,4):
            patterns[s] = [tuple(c) for c in combinations(range(9), s)
                           if line_cover(set(c), local_lines)]
        assert len(patterns[3]) == 6
        def generate():
            for heavy in range(3):
                opts = [patterns[4] if z == heavy else patterns[3]
                        for z in range(3)]
                for p0, p1, p2 in product(*opts):
                    yield frozenset(3 * x + z for z, pattern in enumerate((p0,p1,p2))
                                    for x in pattern)
        allsets = generate()
    else:
        raise ValueError(n)
    maxc = max_complements(n)
    valid = set()
    for A in allsets:
        if len(A) == k and line_cover(A, ln):
            valid.add(A)
    complete = {A for A in valid if any(M.issubset(A) for M in maxc)}
    holes = valid - complete
    assert len(complete) == 6 ** n
    assert len(holes) == {2:9,3:54}[n]
    for A in complete:
        assert sum(M.issubset(A) for M in maxc) == 1
    for A in valid:
        assert sorted(sum(v in A for v in line) for line in ln).count(2) == n
    print(f'DIMENSION_{n}_OK total={len(valid)} repairable={len(complete)} unrepairable={len(holes)}')


def check_maximal_transversals():
    # At dimension three each z-layer is a permutation matrix. Their
    # 6^3 combinations are filtered by the vertical-line condition.
    p2 = [tuple(c) for c in combinations(range(9), 3)
          if line_cover(set(c), lines(2))]
    assert len(p2) == 6
    found3 = set()
    for layers in product(p2, repeat=3):
        A = frozenset(3 * x + z for z, pattern in enumerate(layers)
                      for x in pattern)
        if line_cover(A, lines(3)):
            found3.add(A)
    assert found3 == max_complements(3)
    # The fourth dimension is obtained from three ternary three-cube
    # layers. All 12^3 candidates are checked without the affine formula.
    found4 = set()
    for layers in product(tuple(found3), repeat=3):
        A = frozenset(3 * x + z for z, pattern in enumerate(layers)
                      for x in pattern)
        if line_cover(A, lines(4)):
            found4.add(A)
    assert found4 == max_complements(4)
    print(f'MAXIMAL_TRANSVERSALS_OK 3:{len(found3)} 4:{len(found4)}')


def local_four_dimensional_obstruction():
    # If the duplicated coordinate lines pass through an absent origin,
    # each 3-coordinate section contains one parity class on its eight
    # all-nonzero corners. There are 16 possible parity-sign choices.
    for signs in product((-1, 1), repeat=4):
        viable = []
        for corner in product((-1, 1), repeat=4):
            if all(corner[0] * corner[1] * corner[2] * corner[3] // corner[j] == -signs[j]
                   for j in range(4)):
                viable.append(corner)
        assert len(viable) == 1
    print('FOUR_DIMENSIONAL_HOLE_OBSTRUCTION_OK 16')


if __name__ == '__main__':
    test(2)
    test(3)
    check_maximal_transversals()
    local_four_dimensional_obstruction()
    print('VERIFY_OK')
