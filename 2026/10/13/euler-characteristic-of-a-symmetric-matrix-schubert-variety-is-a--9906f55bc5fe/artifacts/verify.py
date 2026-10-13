from itertools import permutations
from math import factorial

def rank_matrix(w):
    n = len(w)
    return [[sum(1 for k in range(i+1) if w[k] <= n-j) for j in range(n)] for i in range(n)]

def direct_survives(r, a, b):
    # a,b are zero-indexed, a <= b.
    n = len(r)
    for p in range(n):
        for q in range(n):
            first = p >= a and q <= b
            if a == b:
                actual = 1 if first else 0
            else:
                second = p >= b and q <= a
                actual = int(first) + int(second)
            if actual > r[p][q]:
                return False
    return True

def rank_criterion(r, a, b):
    if a == b:
        return r[a][a] >= 1
    return r[a][b] >= 1 and r[b][a] >= 2

def order_stat_criterion(w, a, b):
    n = len(w)
    if a == b:
        return True
    minimum = min(w[:a+1])
    second = sorted(w[:b+1])[1]
    return minimum <= n-b and second <= n-a

permutation_checks = coordinate_checks = condition_checks = 0

for n in range(1, 8):
    min_value = 10**9
    max_value = -1
    min_perms = []
    max_perms = []

    for w in permutations(range(1, n+1)):
        r = rank_matrix(w)
        value = 0
        for a in range(n):
            for b in range(a, n):
                direct = direct_survives(r, a, b)
                by_rank = rank_criterion(r, a, b)
                by_order = order_stat_criterion(w, a, b)
                assert direct == by_rank == by_order
                value += int(direct)
                coordinate_checks += 1
                condition_checks += n*n

        permutation_checks += 1
        if value < min_value:
            min_value, min_perms = value, [w]
        elif value == min_value:
            min_perms.append(w)
        if value > max_value:
            max_value, max_perms = value, [w]
        elif value == max_value:
            max_perms.append(w)

    assert min_value == n
    assert min_perms == [tuple(range(n, 0, -1))]
    assert max_value == n*(n+1)//2
    assert all(w[0] == 1 for w in max_perms)
    assert len(max_perms) == factorial(n-1)

print("VERIFY_OK", permutation_checks, coordinate_checks, condition_checks)
