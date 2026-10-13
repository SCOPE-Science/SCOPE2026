#!/usr/bin/env python3
"""Exact arithmetic checks for the two-missing-corners Segre toric charts.
Run with Python 3 and SymPy; no data files required.
"""
from sympy import Matrix


def charts(a, b, ref):
    i, j = ref
    rows = [p for p in range(a) if p != i]
    cols = [q for q in range(b) if q != j]
    labels = [('R', p) for p in rows] + [('C', q) for q in cols]
    index = {label: n for n, label in enumerate(labels)}
    d = a + b - 2

    def unit(key):
        w = [0] * d
        w[index[key]] = 1
        return w

    def add(*terms):
        return [sum(t[z] for t in terms) for z in range(d)]

    vectors = []
    for p in range(a):
        for q in range(b):
            if (p, q) in ((0, 0), (1, 1), ref):
                continue
            summands = []
            if p != i:
                summands.append(unit(('R', p)))
            if q != j:
                summands.append(unit(('C', q)))
            vectors.append(((p, q), add(*summands)))

    normals = [unit(key) for key in labels]
    if i >= 2 and j >= 2:
        kind = 'ordinary-ordinary'
    elif i < 2 and j >= 2:
        kind = 'special-row'
        missing_col = unit(('C', i))
        normal = [sum(unit(('R', p))[k] for p in rows) - missing_col[k]
                  for k in range(d)]
        normals.append(normal)
    elif i >= 2 and j < 2:
        kind = 'special-column'
        missing_row = unit(('R', j))
        normal = [sum(unit(('C', q))[k] for q in cols) - missing_row[k]
                  for k in range(d)]
        normals.append(normal)
    else:
        assert i != j, 'both missing diagonal coordinates are excluded'
        kind = 'cross'
        x = unit(('R', j))
        y = unit(('C', i))
        other_c = [unit(('C', q)) for q in range(2, b)]
        other_r = [unit(('R', p)) for p in range(2, a)]
        n1 = [-x[k] + y[k] + sum(u[k] for u in other_c) for k in range(d)]
        n2 = [x[k] - y[k] + sum(u[k] for u in other_r) for k in range(d)]
        normals.extend((n1, n2))
    return kind, labels, vectors, normals


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def main():
    count = 0
    for a in range(3, 7):
        for b in range(3, 7):
            predicted_smooth = (a - 2) * (b - 2)
            predicted_side = 2 * ((a - 2) + (b - 2))
            predicted_cross = 2
            obs_smooth = obs_side = obs_cross = 0
            for i in range(a):
                for j in range(b):
                    if (i, j) in ((0, 0), (1, 1)):
                        continue
                    kind, labels, vectors, normals = charts(a, b, (i, j))
                    d = a + b - 2
                    assert Matrix([v for _, v in vectors]).rank() == d
                    assert len(set(map(tuple, normals))) == len(normals)
                    assert all(dot(n, v) >= 0 for n in normals for _, v in vectors)
                    # Every proposed supporting hyperplane has dimension d-1.
                    for normal in normals:
                        on_face = [v for _, v in vectors if dot(normal, v) == 0]
                        assert Matrix(on_face).rank() == d - 1, (a, b, i, j, normal)
                    # The coordinate normals occur as a saturated lattice basis.
                    assert normals[:d] == [[int(k == h) for k in range(d)] for h in range(d)]
                    rank = len(normals) - d
                    expected_rank = 0 if kind == 'ordinary-ordinary' else 2 if kind == 'cross' else 1
                    assert rank == expected_rank
                    # Since the coordinate facet normals fix m=(1,...,1), Q-Gorenstein
                    # is equivalent to testing that integer vector on extra facets.
                    q_gorenstein = all(dot(n, [1] * d) == 1 for n in normals)
                    expected_q_gorenstein = (
                        True if kind == 'ordinary-ordinary' else
                        a == 3 if kind == 'special-row' else
                        b == 3 if kind == 'special-column' else
                        a == b == 3)
                    assert q_gorenstein == expected_q_gorenstein
                    obs_smooth += kind == 'ordinary-ordinary'
                    obs_side += kind in ('special-row', 'special-column')
                    obs_cross += kind == 'cross'
                    count += 1
            assert (obs_smooth, obs_side, obs_cross) == (predicted_smooth, predicted_side, predicted_cross)
            print(f'({a},{b}): smooth={obs_smooth}; class-Z={obs_side}; class-Z2={obs_cross}; Q-Gorenstein={a==b==3}')
    print(f'PASS: {count} exact chart verifications and all facet-rank and lattice-basis checks')


if __name__ == '__main__':
    main()
