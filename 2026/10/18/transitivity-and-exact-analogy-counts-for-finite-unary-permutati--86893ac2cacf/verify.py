"""Finite verification of the analogical-proportion theorem for unary permutations.

This program implements the directed maximization definition of Antić,
'Analogical proportions in monounary algebras' (2024), independently of
its asserted closed-form cycle criterion. In a finite permutation algebra
all unary terms are periodic; exponent pairs modulo the order of the
permutation suffice to represent their infinite justification sets.
"""
from itertools import product
from math import gcd, lcm


def check_cycle_partition(sizes):
    n = sum(sizes)
    cycle, offset = [], []
    for j, size in enumerate(sizes):
        for t in range(size):
            cycle.append(j)
            offset.append(t)
    period = lcm(*sizes)
    exponents = [(p, q) for p in range(period) for q in range(period)]

    # This is direct term evaluation: choose a witness point w, then
    # evaluate f^p(w)=a and f^q(w)=b for every exponent residue.
    successors = [[0] * n for _ in range(period)]
    for w in range(n):
        successors[0][w] = w
    for p in range(1, period):
        for w in range(n):
            j = cycle[w]
            base = sum(sizes[:j])
            successors[p][w] = base + (offset[w] + p) % sizes[j]
    justifications = {}
    for a, b in product(range(n), repeat=2):
        justifications[a, b] = frozenset(
            (p, q) for p, q in exponents
            if any(successors[p][w] == a and successors[q][w] == b
                   for w in range(n))
        )

    trivial = frozenset.intersection(*justifications.values())

    def arrow(a, b, c, d):
        ja, jc = justifications[a, b], justifications[c, d]
        if (ja | jc) <= trivial:
            return True
        overlap = (ja & jc) - trivial
        if not overlap:
            return False
        for replacement in range(n):
            alternative = (ja & justifications[c, replacement]) - trivial
            if overlap < alternative:
                return False
        return True

    def proportion(a, b, c, d):
        return (arrow(a, b, c, d) and arrow(b, a, d, c)
                and arrow(c, d, a, b) and arrow(d, c, b, a))

    arrows = list(product(range(n), repeat=2))
    relation = []
    actual_count = 0
    for a, b in arrows:
        row = []
        for c, d in arrows:
            expected = ((cycle[a] != cycle[b] and cycle[c] != cycle[d])
                        or (cycle[a] == cycle[b] and cycle[c] == cycle[d]
                            and (offset[b] - offset[a] - offset[d] + offset[c])
                            % gcd(sizes[cycle[a]], sizes[cycle[c]]) == 0))
            actual = proportion(a, b, c, d)
            assert actual == expected, (sizes, a, b, c, d, actual, expected)
            actual_count += actual
            row.append(actual)
        relation.append(row)

    total = n*n - sum(s*s for s in sizes)
    count_formula = total*total + sum(
        x*x*y*y//gcd(x, y) for x in sizes for y in sizes)
    assert actual_count == count_formula

    is_transitive = True
    for i in range(len(arrows)):
        for j in range(len(arrows)):
            if relation[i][j]:
                for k in range(len(arrows)):
                    if relation[j][k] and not relation[i][k]:
                        is_transitive = False
                        break
                if not is_transitive:
                    break
        if not is_transitive:
            break
    predicted_transitive = len(set(sizes)) == 1
    assert is_transitive == predicted_transitive, (sizes, is_transitive)
    if predicted_transitive:
        r, s = len(sizes), sizes[0]
        class_sizes = sorted([r*s]*s + ([r*(r-1)*s*s] if r > 1 else []))
        # More direct: distinct neighborhoods are the equivalence classes.
        distinct_classes = sorted(set(tuple(row) for row in relation))
        actual_sizes = sorted(sum(row) for row in distinct_classes)
        assert actual_sizes == class_sizes, (sizes, actual_sizes, class_sizes)
    return n**4


def run():
    families, quadruples = 0, 0
    for n in range(1, 8):
        for mask in range(1 << (n-1)):
            sizes = []
            width = 1
            for k in range(n-1):
                if (mask >> k) & 1:
                    sizes.append(width)
                    width = 1
                else:
                    width += 1
            sizes.append(width)
            quadruples += check_cycle_partition(sizes)
            families += 1
    print(f'VERIFY_OK compositions={families} tested_quadruples={quadruples} '
          f'direct_justifications=YES exact_counts=YES transitivity=YES')


if __name__ == '__main__':
    run()
