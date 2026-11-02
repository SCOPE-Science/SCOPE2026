#!/usr/bin/env python3
"""Independent finite-field checks for fixed-point-free automorphisms
of the free class-two Lie algebra on three generators.

No external dependencies; run: python3 verify_fpf_free_two_step_rank3.py
"""
from itertools import product


def field_tables(q):
    if q == 4:
        # F_2[t]/(t^2+t+1), a+bt encoded as a+2*b.
        plus = [[a ^ b for b in range(q)] for a in range(q)]
        mul = [[0] * q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                a0, a1 = a & 1, a >> 1
                b0, b1 = b & 1, b >> 1
                c0 = (a0*b0) ^ (a1*b1)
                c1 = (a0*b1) ^ (a1*b0) ^ (a1*b1)
                mul[a][b] = c0 | (c1 << 1)
        minus = list(range(q))
    else:
        assert q in (2, 3, 5)
        plus = [[(a + b) % q for b in range(q)] for a in range(q)]
        mul = [[a * b % q for b in range(q)] for a in range(q)]
        minus = [(-a) % q for a in range(q)]
    return plus, mul, minus


def det3(a, add, mul, neg):
    a0,a1,a2,a3,a4,a5,a6,a7,a8 = a
    p = add[mul[a0][mul[a4][a8]]][mul[a1][mul[a5][a6]]]
    p = add[p][mul[a2][mul[a3][a7]]]
    z = add[mul[a2][mul[a4][a6]]][mul[a1][mul[a3][a8]]]
    z = add[z][mul[a0][mul[a5][a7]]]
    return add[p][neg[z]]


def theorem_gl_count(q):
    # This closed form follows from irreducible cubic, quadratic+linear,
    # and split rational-canonical-type counts.
    return q**3 * (q**6 - 3*q**5 + q**4 + 4*q**3 + q**2 - 3*q - 8 - (q % 2))


def rank6(matrix, add, mul, neg):
    a = [list(row) for row in matrix]
    inv = {x: next(y for y in range(len(mul)) if mul[x][y] == 1)
           for x in range(1, len(mul))}
    pivot_row = 0
    for j in range(6):
        p = next((i for i in range(pivot_row, 6) if a[i][j] != 0), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        a[pivot_row] = [mul[x][inv[a[pivot_row][j]]] for x in a[pivot_row]]
        for i in range(6):
            if i != pivot_row and a[i][j]:
                factor = a[i][j]
                a[i] = [add[a[i][c]][neg[mul[factor][a[pivot_row][c]]]]
                        for c in range(6)]
        pivot_row += 1
    return pivot_row


def verify_induced_lie_automorphism(a, q, add, mul, neg, qualifies):
    # Explicitly construct the induced action on V + exterior^2(V), with
    # independent arbitrary central shears and the original Lie brackets.
    ij = [(0,1),(0,2),(1,2)]
    wedge = [[0]*3 for _ in range(3)]
    for k,(i,j) in enumerate(ij):
        for l,(u,v) in enumerate(ij):
            wedge[k][l] = add[mul[a[3*i+u]][a[3*j+v]]][
                neg[mul[a[3*i+v]][a[3*j+u]]]]
    for trial in (0,1,2):
        b = [[0 if trial == 0 else (1 if trial == 1 else
             (i+j+sum(a))%q) for j in range(3)] for i in range(3)]
        mat = [[0]*6 for _ in range(6)]
        for i in range(3):
            for j in range(3):
                mat[i][j] = a[3*i+j]
                mat[3+i][j] = b[i][j]
                mat[3+i][3+j] = wedge[i][j]
        # Preservation of each basis bracket is represented by the minors.
        for k,(u,v) in enumerate(ij):
            assert [mat[3+i][3+k] for i in range(3)] == [wedge[i][k] for i in range(3)]
        for i in range(6):
            mat[i][i] = add[mat[i][i]][neg[1]]
        assert (rank6(mat, add, mul, neg) == 6) == qualifies


def check(q):
    add, mul, neg = field_tables(q)
    gl, eligible, direct_checks = 0, 0, 0
    for a in product(range(q), repeat=9):
        delta = det3(a, add, mul, neg)
        if delta == 0:
            continue
        gl += 1
        b = list(a)
        for i in (0,4,8):
            b[i] = add[b[i]][neg[1]]
        first_ok = det3(b, add, mul, neg) != 0
        b = [neg[x] for x in a]
        for i in (0,4,8):
            b[i] = add[b[i]][delta]
        qualifies = first_ok and det3(b, add, mul, neg) != 0
        if qualifies:
            eligible += 1
        if direct_checks < (500 if q == 2 else 150):
            verify_induced_lie_automorphism(a, q, add, mul, neg, qualifies)
            direct_checks += 1
    expected_gl = (q**3 - 1)*(q**3 - q)*(q**3 - q*q)
    expected = theorem_gl_count(q)
    assert gl == expected_gl, (q, gl, expected_gl)
    assert eligible == expected, (q, eligible, expected)
    # Each eligible quotient action has precisely q^9 central shears.
    print('q=%d GL3=%d admissible=%d fixed_point_free_automorphisms=%d direct_block_checks=%d OK'
          % (q, gl, eligible, eligible*q**9, direct_checks*3), flush=True)

if __name__ == '__main__':
    for q in (2,3,4,5):
        check(q)
    print('FREE_TWO_STEP_RANK3_FIXED_POINT_FREE_OK 4_EXHAUSTIVE_FIELDS')
