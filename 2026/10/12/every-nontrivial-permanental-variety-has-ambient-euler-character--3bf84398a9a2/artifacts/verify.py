from itertools import combinations, permutations

formats = 0
coordinate_tests = 0
permanent_term_evaluations = 0
weight_term_checks = 0

for m in range(2, 6):
    for n in range(m, 7):
        row_weights = [1 << i for i in range(m)]
        col_weights = [1 << (m + j) for j in range(n)]
        coordinate_weights = [
            row_weights[i] + col_weights[j]
            for i in range(m)
            for j in range(n)
        ]
        assert len(coordinate_weights) == len(set(coordinate_weights))

        for r in range(2, m + 1):
            formats += 1
            rowsets = list(combinations(range(m), r))
            colsets = list(combinations(range(n), r))

            for i0 in range(m):
                for j0 in range(n):
                    coordinate_tests += 1
                    for I in rowsets:
                        for J in colsets:
                            value = 0
                            common_weight = None
                            for sigma in permutations(range(r)):
                                term = 1
                                term_weight = 0
                                for q in range(r):
                                    i = I[q]
                                    j = J[sigma[q]]
                                    term *= int(i == i0 and j == j0)
                                    term_weight += row_weights[i] + col_weights[j]
                                value += term
                                permanent_term_evaluations += 1
                                if common_weight is None:
                                    common_weight = term_weight
                                else:
                                    assert term_weight == common_weight
                                weight_term_checks += 1
                            assert value == 0

assert formats == 30
assert coordinate_tests == 548
assert permanent_term_evaluations == 202968
assert weight_term_checks == 202968
print("VERIFY_OK", formats, coordinate_tests, permanent_term_evaluations, weight_term_checks)
