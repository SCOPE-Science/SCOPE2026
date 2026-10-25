"""Finite exact-arithmetic diagnostics for rank-two spectral detectors.
Requires Python 3 and SymPy. Not a proof of the all-dimensional statement.
"""
import itertools
import random
import sympy as sp

RNG = random.Random(20261018)
COUNT = 0
CASES = 0

def randomized_basis(n):
    return sp.Matrix([[RNG.randrange(-3, 4) for _ in range(2)] for _ in range(n)])

def make_detector(A, B):
    n = A.rows
    for _ in range(150):
        U = randomized_basis(n)
        Y = A * U
        if Y.rank() < 2:
            continue
        i, j = next((i, j) for i in range(n) for j in range(i + 1, n)
                    if Y.extract([i, j], [0, 1]).det() != 0)
        select = sp.zeros(2, n)
        select[0, i] = 1
        select[1, j] = 1
        L = Y.extract([i, j], [0, 1]).inv() * select
        for _ in range(25):
            W = sp.Matrix([[RNG.randrange(-2, 3) for _ in range(n)] for _ in range(2)])
            V = L + W * (sp.eye(n) - Y * L)
            M = V * B * U
            if M != sp.eye(2) * M[0, 0]:
                if M[0, 0] != M[1, 1]:
                    H = sp.diag(1, -1)
                elif M[0, 1] != 0:
                    H = sp.Matrix([[1, 0], [1, -1]])
                else:
                    H = sp.Matrix([[1, 1], [0, -1]])
                return U, V, H, M
    raise ValueError('unable to locate a nonscalar two-dimensional compression')

def trial(A, B):
    global COUNT, CASES
    U, V, H, M = make_detector(A, B)
    T = U * H * V
    checks = [
        V * A * U == sp.eye(2),
        H * H == sp.eye(2),
        H.trace() == 0,
        (M * H).trace() != 0,
        T.rank() == 2,
        (A * T).trace() == 0,
        ((A * T) ** 2).trace() == 2,
        (B * T).trace() != 0,
    ]
    for lam, mu in itertools.product(range(-2, 3), repeat=2):
        if not (lam or mu):
            continue
        C = lam * A + mu * B
        assert C != sp.zeros(A.rows)
        checks.append((C * T).trace() != 0 or ((C * T) ** 2).trace() != 0)
    if not all(checks):
        raise AssertionError((A, B, checks))
    COUNT += len(checks)
    CASES += 1

# Complete integer pencil sample in dimension two, excluding dependent pairs.
A = sp.Matrix([[1, 0], [0, 1]])
for vals in itertools.product([-1, 0, 1], repeat=4):
    B = sp.Matrix(2, 2, vals)
    if B != sp.zeros(2) and B != B[0, 0] * A:
        trial(A, B)

for n in (2, 3, 4):
    k = 0
    while k < 75:
        A = sp.Matrix([[RNG.randrange(-2, 3) for _ in range(n)] for _ in range(n)])
        B = sp.Matrix([[RNG.randrange(-2, 3) for _ in range(n)] for _ in range(n)])
        if A.rank() < 2 or (A.row_join(B)).rank() == 0:
            continue
        # Operator-linear independence: B is not a scalar multiple of A.
        v = [a for a in A]
        w = [b for b in B]
        if sp.Matrix.hstack(sp.Matrix(v), sp.Matrix(w)).rank() < 2:
            continue
        trial(A, B)
        k += 1

# Degenerate pencils stress the kernel/range separation in the proof.
A = sp.diag(1, 1, 0, 0)
for B in (
    sp.eye(4).extract([0, 1, 2, 3], [0, 1, 2, 3]) - sp.diag(0, 0, 1, 1),
    sp.eye(4) - A,
    sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
    sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]),
    sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]),
    sp.diag(1, 1, 0, 1),
    sp.diag(sp.I, sp.I, 0, 0) + sp.Matrix([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
):
    if sp.Matrix.hstack(sp.Matrix(list(A)), sp.Matrix(list(B))).rank() == 2:
        trial(A, B)
print('exact_cases=', CASES, 'assertions=', COUNT, 'status=PASS')
