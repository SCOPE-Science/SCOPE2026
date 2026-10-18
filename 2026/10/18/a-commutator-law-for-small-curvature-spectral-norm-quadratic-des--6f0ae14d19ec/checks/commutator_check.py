"""Numerical cross-checks for the Kronecker-curvature commutator law.

Requirements: Python 3, NumPy, SciPy. This checks finite instances;
all-dimensional conclusions are established separately by proof.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize


def check(singular_values, m, nmat, radius, epsilon):
    dimension = len(singular_values)
    pairs = [(i, j) for i in range(dimension)
             for j in range(i + 1, dimension)]
    sigma = np.diag(singular_values)
    commutator = m @ nmat - nmat @ m
    derivative = np.array([
        -radius * commutator[i, j] / (singular_values[i] + singular_values[j])
        for i, j in pairs
    ])

    def rotation(parameters):
        k = np.zeros((dimension, dimension))
        for (i, j), value in zip(pairs, parameters):
            k[i, j], k[j, i] = value, -value
        return expm(k)

    def objective(parameters):
        r = rotation(parameters)
        return (-radius * np.trace(sigma @ r)
                + epsilon * radius**2 / 2 * np.trace(r.T @ m @ r @ nmat))

    fit = minimize(objective, epsilon * derivative, method='BFGS',
                   options={'gtol': 1e-12, 'maxiter': 200})
    r = rotation(fit.x)
    normal_certificate = r.T @ (sigma - epsilon * radius * m @ r @ nmat)
    skew_error = np.linalg.norm(normal_certificate - normal_certificate.T)
    smallest_normal_eigenvalue = np.linalg.eigvalsh(
        (normal_certificate + normal_certificate.T) / 2)[0]
    gap = objective(np.zeros(len(pairs))) - objective(fit.x)
    leading = (radius**3 / 2 * sum(
        commutator[i, j]**2 / (singular_values[i] + singular_values[j])
        for i, j in pairs))
    assert smallest_normal_eigenvalue > 0
    assert skew_error < 3e-6
    assert np.max(np.abs(fit.x / epsilon - derivative)) < 0.01
    assert abs(gap / epsilon**2 - leading) < 0.002
    print('dimension', dimension, 'epsilon', epsilon,
          'generator_slope', fit.x / epsilon, 'predicted', derivative,
          'gap_per_epsilon_squared', float(gap / epsilon**2),
          'predicted_coefficient', float(leading),
          'normal_skew_residual', float(skew_error),
          'smallest_normal_eigenvalue', float(smallest_normal_eigenvalue))


def main():
    m2 = np.diag([2.0, 1.0])
    n2 = np.array([[2.0, 0.5], [0.5, 3.0]])
    for epsilon in (0.1, 0.03, 0.01, 0.003):
        check([3.0, 1.0], m2, n2, 1.0, epsilon)

    m3 = np.array([[1.8, 0.3, 0.1], [0.3, 1.5, 0.2], [0.1, 0.2, 1.9]])
    n3 = np.array([[2.3, -0.25, 0.1], [-0.25, 1.2, 0.3], [0.1, 0.3, 1.5]])
    for epsilon in (0.01, 0.003):
        check([4.0, 2.0, 1.0], m3, n3, 0.7, epsilon)

    # When both curvature factors are diagonal, the exact baseline
    # optimality threshold is (radius * max_i(m_i*n_i/sigma_i))**(-1).
    sigma = np.diag([3.0, 1.0])
    m = np.diag([2.0, 1.0])
    nmat = np.diag([2.0, 3.0])
    critical = 1.0 / max((2.0 * 2.0 / 3.0), (1.0 * 3.0 / 1.0))
    assert abs(critical - 1.0 / 3.0) < 1e-14
    assert np.min(np.linalg.eigvalsh(sigma - 0.3 * m @ nmat)) >= 0
    assert np.min(np.linalg.eigvalsh(sigma - 0.4 * m @ nmat)) < 0
    print('commuting_threshold', critical, 'certificate_test', 'PASS')


if __name__ == '__main__':
    main()
