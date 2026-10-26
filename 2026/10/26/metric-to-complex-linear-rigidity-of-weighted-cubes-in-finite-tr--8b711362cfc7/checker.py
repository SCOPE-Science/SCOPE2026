"""Deterministic finite tests for weighted Boolean-cube trace-norm constructions.

Run: python checker.py  (requires numpy).  These tests are diagnostic only;
nonexistence in smaller matrix sizes and rigidity follow from the proof.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261019)
assertions = 0


def check(condition, explanation):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(explanation)


def trace_norm(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def isometry_columns(rows, rank):
    matrix = rng.normal(size=(rows, rank)) + 1j * rng.normal(size=(rows, rank))
    return np.linalg.qr(matrix, mode='reduced')[0][:, :rank]


def test_cube(n, p, q, weights, rank_blocks=None):
    if rank_blocks is None:
        rank_blocks = [1] * n
    r = sum(rank_blocks)
    check(r <= min(p, q), 'rank exceeds matrix dimensions')
    left = isometry_columns(p, r)
    right = isometry_columns(q, r)
    polar = left @ right.conj().T
    check(np.allclose(polar.conj().T @ polar, right @ right.conj().T, atol=1e-10), 'polar initial projection')
    positives = []
    offset = 0
    for wi, ri in zip(weights, rank_blocks):
        basis = right[:, offset:offset + ri]
        z = rng.normal(size=(ri, ri)) + 1j * rng.normal(size=(ri, ri))
        local = z @ z.conj().T
        local *= wi / np.trace(local).real
        h = basis @ local @ basis.conj().T
        positives.append(h)
        offset += ri
        check(abs(np.trace(h).real - wi) < 1e-9, 'block trace')
        check(float(np.linalg.eigvalsh(h).min()) > -1e-9, 'block positivity')
    for i in range(n):
        for j in range(i + 1, n):
            check(np.linalg.norm(positives[i] @ positives[j], 'fro') < 1e-9, 'block orthogonality')
    translation = rng.normal(size=(p, q)) + 1j * rng.normal(size=(p, q))
    cube = list(itertools.product((0, 1), repeat=n))
    outputs = []
    for vertex in cube:
        h = np.zeros((q, q), dtype=np.complex128)
        for i, active in enumerate(vertex):
            if active:
                h += positives[i]
        outputs.append(translation + polar @ h)
    for k, x in enumerate(cube):
        for l, y in enumerate(cube):
            expected = sum(weights[i] for i in range(n) if x[i] != y[i])
            actual = trace_norm(outputs[k] - outputs[l])
            check(abs(actual - expected) < 2e-8 * max(1, expected), f'trace distance n={n}, k={k}, l={l}')
    return len(cube)


for n in (3, 4, 5, 6):
    for trial in range(3):
        weights = rng.uniform(0.5, 3.0, n).tolist()
        test_cube(n, n + 1, n + 2, weights)
# Multirank blocks and genuinely rectangular operators.
test_cube(3, 8, 7, [1.0, 2.5, 0.75], [2, 1, 2])
test_cube(4, 9, 10, [0.9, 1.3, 2.1, 1.7], [2, 1, 1, 2])

# Exact integer computation in canonical diagonal representatives.
for n in range(3, 9):
    weights = list(range(1, n + 1))
    for x in itertools.product((0, 1), repeat=n):
        for y in itertools.product((0, 1), repeat=n):
            diagonal_difference = [weights[i] * (x[i] - y[i]) for i in range(n)]
            direct_trace_norm = sum(abs(value) for value in diagonal_difference)
            hamming_distance = sum(weights[i] for i in range(n) if x[i] != y[i])
            check(direct_trace_norm == hamming_distance, 'exact diagonal witness')

print('PASS:', assertions, 'finite diagnostics (floating complex matrices and exact integer witnesses)')
