from itertools import permutations
from math import factorial

def rank_matrix(w):
    n = len(w)
    return [[sum(1 for k in range(j+1) if w[k] <= i+1) for j in range(n)] for i in range(n)]

def coordinate_survives_direct(r, row, col):
    n = len(r)
    for p in range(n):
        for q in range(n):
            actual = 1 if p >= row and q >= col else 0
            if actual > r[p][q]:
                return False
    return True

def formula(w):
    n = len(w)
    m = n + 1
    total = 0
    for x in w:
        m = min(m, x)
        total += n - m + 1
    return total

permutation_checks = coordinate_checks = condition_checks = 0

for n in range(1, 8):
    min_count = 10**9
    max_count = -1
    min_perms = []
    max_perms = []

    for w in permutations(range(1, n+1)):
        r = rank_matrix(w)
        direct = 0
        for i in range(n):
            for j in range(n):
                ok = coordinate_survives_direct(r, i, j)
                direct += int(ok)
                coordinate_checks += 1
                condition_checks += n*n
                assert ok == (r[i][j] > 0)

        f = formula(w)
        assert direct == f
        permutation_checks += 1

        if f < min_count:
            min_count, min_perms = f, [w]
        elif f == min_count:
            min_perms.append(w)
        if f > max_count:
            max_count, max_perms = f, [w]
        elif f == max_count:
            max_perms.append(w)

    assert min_count == n*(n+1)//2
    assert min_perms == [tuple(range(n,0,-1))]
    assert max_count == n*n
    assert all(w[0] == 1 for w in max_perms)
    assert len(max_perms) == factorial(n-1)

assert formula((1,3,2)) == 9
assert formula((3,2,1)) == 6
assert formula((2,1,3)) == 8

print("VERIFY_OK", permutation_checks, coordinate_checks, condition_checks)
