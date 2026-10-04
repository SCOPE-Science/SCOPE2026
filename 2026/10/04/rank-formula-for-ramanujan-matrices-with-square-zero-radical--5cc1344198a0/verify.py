#!/usr/bin/env python3
from fractions import Fraction


def rank_q(A):
    A = [[Fraction(x) for x in row] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [A[i][j] - z * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def local_square_zero_matrix(q, d):
    h = q ** d
    P = (h - 1) // (q - 1)
    rows = [[0] + [-h] * P + [h * (q - 1)]]
    mid = [-1] + [q - 1] * P + [q - 1]
    rows.extend(mid[:] for _ in range(P))
    rows.append([1] + [1] * P + [1])
    return rows


def field_matrix(q):
    return [[-1, q - 1], [1, 1]]


def kron(A, B):
    out = []
    for ar in A:
        for br in B:
            row = []
            for a in ar:
                row.extend(a * b for b in br)
            out.append(row)
    return out


def check_local(q, d):
    A = local_square_zero_matrix(q, d)
    P = (q ** d - 1) // (q - 1)
    assert len(A) == P + 2
    assert rank_q(A) == 3
    # Every projective-direction column is identical.
    for j in range(2, P + 1):
        for row in A:
            assert row[1] == row[j]
    # Unit, one projective-direction, and zero columns are independent.
    cols = [[row[j] for row in A] for j in (0, 1, P + 1)]
    B = [[cols[j][i] for j in range(3)] for i in range(len(A))]
    assert rank_q(B) == 3
    return len(A), P


cases = []
for q in [2, 3, 4, 5, 7]:
    assert rank_q(field_matrix(q)) == 2
    for d in range(1, 4):
        n, P = check_local(q, d)
        cases.append((q, d, n, P))

# Small exact tensor-product checks of the global multiplicative formula.
A = local_square_zero_matrix(2, 2)   # rank 3, size 5
B = local_square_zero_matrix(3, 2)   # rank 3, size 6
F2 = field_matrix(2)                  # rank 2
F3 = field_matrix(3)                  # rank 2
assert rank_q(kron(F2, A)) == 6
assert rank_q(kron(A, B)) == 9
assert rank_q(kron(F2, F3)) == 4
assert rank_q(kron(kron(F2, A), F3)) == 12

print('VERIFY_OK local_cases=%d q_values=%s d=1..3 max_local_matrix=%d tensor_checks=4' %
      (len(cases), [2, 3, 4, 5, 7], max(n for _, _, n, _ in cases)))
for q, d, n, P in cases[:8]:
    print('q=%d d=%d tau=%d projective_classes=%d rank=3 nullity=%d' %
          (q, d, n, P, n - 3))
