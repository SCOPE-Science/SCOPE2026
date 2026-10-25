"""Independent finite checks for two-colour strong-majority hypercube edge colourings."""
from itertools import product


def edges_of_cube(d):
    return [(v, v ^ (1 << i), i) for v in range(1 << d)
            for i in range(d) if not (v & (1 << i))]


def prescribed(d, eps):
    edges = edges_of_cube(d)
    return tuple(1 if eps[i] * (-1 if ((v & ~ (1 << i)).bit_count() % 2) else 1) > 0 else 0
                 for v, _, i in edges)


def valid(d, col, edges=None):
    edges = edges if edges is not None else edges_of_cube(d)
    for j, (u, v, _) in enumerate(edges):
        neighbours = [col[k] for k, (a, b, _) in enumerate(edges)
                      if k != j and (u == a or u == b or v == a or v == b)]
        if neighbours.count(1) != d - 1:
            return False
    return True


def main():
    checks = []
    for d in (2, 3):
        ed = edges_of_cube(d)
        predicted = {prescribed(d, eps) for eps in product((-1, 1), repeat=d)}
        found = {col for col in product((0, 1), repeat=len(ed)) if valid(d, col, ed)}
        assert found == predicted and len(found) == (1 << d)
        checks.append((d, len(ed), len(found), 'exhaustive'))
    for d in (4, 5, 6, 7):
        ed = edges_of_cube(d)
        predicted = {prescribed(d, eps) for eps in product((-1, 1), repeat=d)}
        assert len(predicted) == (1 << d)
        assert all(valid(d, coloring, ed) for coloring in predicted)
        checks.append((d, len(ed), len(predicted), 'constructed'))
    print('VERIFY_OK hypercube_d_edgecount_colorings_mode=' + repr(checks))


if __name__ == '__main__':
    main()
