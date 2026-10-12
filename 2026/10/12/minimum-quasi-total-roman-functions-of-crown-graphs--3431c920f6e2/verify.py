from itertools import product
from collections import Counter

def is_qtrd(n, vals):
    A = vals[:n]
    B = vals[n:]
    A2 = [i for i,x in enumerate(A) if x == 2]
    B2 = [i for i,x in enumerate(B) if x == 2]
    Ap = [i for i,x in enumerate(A) if x > 0]
    Bp = [i for i,x in enumerate(B) if x > 0]

    for i,x in enumerate(A):
        if x == 0 and not any(j != i for j in B2):
            return False
        if x == 2 and not any(j != i for j in Bp):
            return False
    for i,x in enumerate(B):
        if x == 0 and not any(j != i for j in A2):
            return False
        if x == 2 and not any(j != i for j in Ap):
            return False
    return True

def predicted_minimum_n_ge_4(n, vals):
    if sum(vals) != 6:
        return False
    A = vals[:n]
    B = vals[n:]
    if A.count(2) != 1 or A.count(1) != 1:
        return False
    if B.count(2) != 1 or B.count(1) != 1:
        return False
    i = A.index(2)
    j = A.index(1)
    k = B.index(2)
    ell = B.index(1)
    # Family I: the 2-labels are matched; the 1-labels can be chosen
    # independently away from that matched pair.
    if k == i:
        return j != i and ell != i
    # Family II: the 2-labels are crossed and the 1-labels occupy the
    # opposite matched positions.
    return k == j and ell == i

total_assignments = 0
for n in range(3, 8):
    by_weight = Counter()
    min_vals = []
    for vals in product(range(3), repeat=2*n):
        total_assignments += 1
        if is_qtrd(n, vals):
            w = sum(vals)
            by_weight[w] += 1
            if w <= 6:
                min_vals.append(vals)

    minimum = min(by_weight)
    if n == 3:
        assert minimum == 6
        assert by_weight[6] == 37
        print(f"n=3: gamma_qtR=6, minimum_functions={by_weight[6]}")
    else:
        assert minimum == 6
        expected = n*n*(n-1)
        assert by_weight[6] == expected
        actual_min = [v for v in min_vals if sum(v) == 6 and is_qtrd(n, v)]
        assert len(actual_min) == expected
        assert all(predicted_minimum_n_ge_4(n, v) for v in actual_min)
        predicted_count = 0
        for vals in product(range(3), repeat=2*n):
            if predicted_minimum_n_ge_4(n, vals):
                predicted_count += 1
                assert is_qtrd(n, vals)
        assert predicted_count == expected
        print(f"n={n}: gamma_qtR=6, minimum_functions={expected}")

print("VERIFY_OK")
print("n_range = 3..7")
print("ternary_labelings_checked =", total_assignments)
print("Cr_3 minimum-function count = 37")
print("for n=4..7 every minimum function matched exactly one of the two structural families")
print("minimum-function formula for n>=4 = n^2(n-1)")
