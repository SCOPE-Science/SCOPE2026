"""Direct finite-dimensional checks of an exact two-qubit stationary concurrence theorem.

Requires NumPy. The mathematical proof is analytic; finite tests do not establish
claims for all parameters.
"""
import math
import numpy as np


def direct_stationary(J, detuning, kappa, p1, p2):
    local_id = np.eye(2, dtype=complex)
    identity = np.eye(4, dtype=complex)
    lowering = np.array([[0, 1], [0, 0]], dtype=complex)
    lower = [np.kron(lowering, local_id), np.kron(local_id, lowering)]
    raise_ops = [a.conj().T for a in lower]
    number = [raise_ops[i] @ lower[i] for i in range(2)]
    hamiltonian = (detuning / 2) * (number[0] - number[1])
    hamiltonian += J * (raise_ops[0] @ lower[1] + lower[0] @ raise_ops[1])

    def dissipator(op):
        norm = op.conj().T @ op
        return np.kron(op.conj(), op) - 0.5 * (
            np.kron(identity, norm) + np.kron(norm.T, identity)
        )

    superop = -1j * (
        np.kron(identity, hamiltonian) - np.kron(hamiltonian.T, identity)
    )
    for excitation, down, up in zip((p1, p2), lower, raise_ops):
        superop += kappa * (
            excitation * dissipator(up) + (1 - excitation) * dissipator(down)
        )
    matrix = superop.copy()
    right_side = np.zeros(16, complex)
    matrix[-1, :] = np.eye(4).reshape(16, order="F")
    right_side[-1] = 1
    rho = np.linalg.solve(matrix, right_side).reshape((4, 4), order="F")
    residual = np.max(np.abs(superop @ rho.reshape(16, order="F")))
    assert residual < 1e-10
    return rho


def reconstructed_stationary(J, detuning, kappa, p1, p2):
    q = (p1 + p2) / 2
    d = (p1 - p2) / 2
    t = 2 * abs(J) / math.hypot(kappa, detuning)
    z = 1 / (1 + t * t)
    u1, u2 = q + d * z, q - d * z
    p11 = q * q - d * d * z
    p00 = (1 - q) ** 2 - d * d * z
    coherence = 2j * J * d * z / (kappa + 1j * detuning)
    return np.array([
        [p00, 0, 0, 0],
        [0, u2 - p11, np.conj(coherence), 0],
        [0, coherence, u1 - p11, 0],
        [0, 0, 0, p11],
    ], dtype=complex)


def concurrence(rho):
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    y2 = np.kron(pauli_y, pauli_y)
    roots = np.sqrt(np.clip(np.linalg.eigvals(rho @ y2 @ rho.conj() @ y2).real, 0, None))
    roots = np.sort(roots)[::-1]
    return max(0.0, float(roots[0] - sum(roots[1:])))


def entanglement_interval(p1, p2):
    q = (p1 + p2) / 2
    d = (p1 - p2) / 2
    h = q * (1 - q)
    if d * d <= h * h / (1 - 2 * h):
        return None
    gap = math.sqrt(1 - 2 * h - h * h / (d * d))
    zp = (1 - h + gap) / (1 + d * d)
    zm = (1 - h - gap) / (1 + d * d)
    return math.sqrt((1 - zp) / zp), math.sqrt((1 - zm) / zm)


def check():
    rng = np.random.default_rng(20231002)
    checked, classified = 0, 0
    for _ in range(350):
        p1, p2 = rng.uniform(0.015, 0.985, 2)
        kappa = float(rng.uniform(0.25, 2.3))
        detuning = float(rng.uniform(-3, 3))
        t = float(rng.uniform(0.03, 5.0))
        exchange = t * math.hypot(kappa, detuning) / 2
        actual = direct_stationary(exchange, detuning, kappa, p1, p2)
        closed = reconstructed_stationary(exchange, detuning, kappa, p1, p2)
        assert np.max(np.abs(actual - closed)) < 2e-11
        checked += 1
        window = entanglement_interval(p1, p2)
        expected = window is not None and window[0] < t < window[1]
        value = concurrence(actual)
        if expected:
            assert value > 1e-10
        elif window is None or min(abs(t - window[0]), abs(t - window[1])) > 1e-5:
            assert value < 1e-8
        classified += 1

    for m in (0.72, 0.8, 0.9, 0.98):
        p1, p2 = (1 + m) / 2, (1 - m) / 2
        lower, upper = entanglement_interval(p1, p2)
        target_lower = m - math.sqrt(2 * m * m - 1)
        target_upper = m + math.sqrt(2 * m * m - 1)
        assert abs(lower - target_lower) < 2e-12
        assert abs(upper - target_upper) < 2e-12

    # At the sharp feasibility threshold there is no positive concurrence.
    mcritical = 1 / math.sqrt(2)
    assert entanglement_interval((1 + mcritical) / 2, (1 - mcritical) / 2) is None
    print("PASS: %d direct Liouvillian stationary-state checks" % checked)
    print("PASS: %d independent Wootters concurrence window tests" % classified)
    print("PASS: 4 exact complementary-bath interval checks and boundary")


if __name__ == "__main__":
    check()
