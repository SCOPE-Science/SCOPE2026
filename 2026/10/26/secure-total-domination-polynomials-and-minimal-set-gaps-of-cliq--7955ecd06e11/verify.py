"""Independent finite checks of secure total domination on clique bouquets.

Run with Python 3.10 or later. The graph and the original exchange
condition are constructed directly; the formula is checked separately.
"""

from collections import Counter
from itertools import product
from math import comb, prod


def build_graph(block_sizes):
    """Vertex 0 is the common center; other vertices follow block order."""
    n = 1 + sum(block_sizes)
    adjacency = [set() for _ in range(n)]
    position = 1
    for size in block_sizes:
        vertices = range(position, position + size)
        for v in vertices:
            adjacency[0].add(v)
            adjacency[v].add(0)
            for w in vertices:
                if v != w:
                    adjacency[v].add(w)
        position += size
    return adjacency


def total_dominating(adjacency, selected):
    """Original definition: every vertex has a selected open neighbor."""
    return all(bool(neighbors & selected) for neighbors in adjacency)


def secure_total_dominating(adjacency, selected):
    """Original definition, checking every nonselected vertex and defender."""
    if not total_dominating(adjacency, selected):
        return False
    for attacked in range(len(adjacency)):
        if attacked in selected:
            continue
        defended = False
        for defender in adjacency[attacked] & selected:
            moved = (selected - {defender}) | {attacked}
            if total_dominating(adjacency, moved):
                defended = True
                break
        if not defended:
            return False
    return True


def predicted_structure(block_sizes, selected):
    counts = []
    index = 1
    for size in block_sizes:
        counts.append(sum(v in selected for v in range(index, index + size)))
        index += size
    if 0 in selected:
        return all(count >= 1 for count in counts)
    return all(count >= 2 for count in counts)


def product_polynomial(a, b):
    out = Counter()
    for degree_a, count_a in a.items():
        for degree_b, count_b in b.items():
            out[degree_a + degree_b] += count_a * count_b
    return out


def polynomial_formula(block_sizes):
    with_center = Counter({1: 1})
    without_center = Counter({0: 1})
    for size in block_sizes:
        with_center = product_polynomial(
            with_center, Counter({j: comb(size, j) for j in range(1, size + 1)})
        )
        without_center = product_polynomial(
            without_center, Counter({j: comb(size, j) for j in range(2, size + 1)})
        )
    return with_center + without_center


def minimal_polynomial_formula(block_sizes):
    count_blocks = len(block_sizes)
    return Counter({count_blocks + 1: prod(block_sizes)}) + Counter(
        {2 * count_blocks: prod(comb(s, 2) for s in block_sizes)}
    )


def check_one(block_sizes):
    adjacency = build_graph(block_sizes)
    sets = []
    polynomial = Counter()
    n = len(adjacency)
    for mask in range(1 << n):
        selected = frozenset(v for v in range(n) if (mask >> v) & 1)
        truth = secure_total_dominating(adjacency, selected)
        expected = predicted_structure(block_sizes, selected)
        if truth != expected:
            raise AssertionError((block_sizes, selected, truth, expected))
        if truth:
            sets.append(selected)
            polynomial[len(selected)] += 1
    expected_polynomial = polynomial_formula(block_sizes)
    if polynomial != expected_polynomial:
        raise AssertionError((block_sizes, polynomial, expected_polynomial))

    # Inclusion minimality checked against all actual secure sets.
    minimal = Counter()
    for selected in sets:
        if not any(other < selected for other in sets):
            minimal[len(selected)] += 1
    expected_minimal = minimal_polynomial_formula(block_sizes)
    if minimal != expected_minimal:
        raise AssertionError((block_sizes, minimal, expected_minimal))
    return 1 << n


def main():
    graph_count = 0
    subset_count = 0
    for t in (2, 3, 4):
        for sizes in product((2, 3, 4), repeat=t):
            if sum(sizes) > 11:
                continue
            subset_count += check_one(sizes)
            graph_count += 1
    assert graph_count == 66
    assert subset_count == 127904
    # A small illustrative graph with three triangular blocks.
    assert polynomial_formula((2, 2, 2)) == Counter({4: 8, 5: 12, 6: 7, 7: 1})
    assert minimal_polynomial_formula((2, 2, 2)) == Counter({4: 8, 6: 1})
    print(f"PASS: {graph_count} ordered clique-bouquet parameter vectors")
    print(f"PASS: {subset_count} exhaustively examined vertex subsets")
    print("PASS: original exchange condition matches the two-family structural characterization")
    print("PASS: complete secure-total-domination coefficient polynomials")
    print("PASS: inclusion-minimal secure-total-domination coefficients")
    print("Example (2,2,2): total {4: 8, 5: 12, 6: 7, 7: 1}; minimal {4: 8, 6: 1}")


if __name__ == "__main__":
    main()
