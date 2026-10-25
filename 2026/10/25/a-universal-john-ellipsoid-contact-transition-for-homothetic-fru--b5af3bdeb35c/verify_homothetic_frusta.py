"""Reproduce the analytic John-contact identities for homothetic convex frusta.

Only numpy is needed. This verifies finite sample cases, not the universal theorem.
"""
import math
import numpy as np


def contact_design(m, family):
    """Unit contact normals and positive base John weights in R^m."""
    if family == "box":
        U = np.concatenate([np.eye(m), -np.eye(m)], axis=0)
        weights = np.full(2 * m, 0.5)
    elif family == "simplex":
        # Orthogonal coordinates for the zero-sum subspace of R^(m+1).
        Z = np.eye(m + 1) - np.ones((m + 1, m + 1)) / (m + 1)
        Q, _ = np.linalg.qr(Z[:, :m])
        U = (Z @ Q) * math.sqrt((m + 1) / m)
        weights = np.full(m + 1, m / (m + 1))
    else:
        raise ValueError(family)
    assert np.linalg.norm(weights @ U) < 1e-12
    assert np.linalg.norm(U.T @ (weights[:, None] * U) - np.eye(m)) < 1e-12
    assert np.max(np.abs(np.linalg.norm(U, axis=1) - 1)) < 1e-12
    return U, weights


def verify(d, q, family):
    m = d - 1
    k = 1 - q
    b = min(0.5, 1 / ((d + 1) * k)) if k else 0.5
    a = math.sqrt(1 - 2 * k * b)
    t = k * b / (1 - k * b)
    s = math.sqrt(1 - t * t)
    U, weights = contact_design(m, family)
    lateral = np.column_stack([s * U, np.full(len(U), t)])
    lateral_weights = weights / (s * s)
    lower = np.r_[np.zeros(m), -1.]
    upper = np.r_[np.zeros(m), 1.]
    lower_weight = (1 + m * t / (1 + t)) / 2
    upper_weight = (1 - m * t / (1 - t)) / 2
    assert lower_weight >= -1e-12
    assert upper_weight >= -1e-12
    assert abs(2 * b - 1) < 1e-12 or upper_weight < 1e-12
    pts = np.vstack([lateral, lower, upper])
    lam = np.r_[lateral_weights, lower_weight, max(0, upper_weight)]
    assert np.linalg.norm(lam @ pts) < 3e-12
    assert np.linalg.norm(pts.T @ (lam[:, None] * pts) - np.eye(d)) < 3e-12
    assert abs(sum(lam) - d) < 2e-11
    # Check all active contact hyperplanes in physical (y,z) coordinates.
    for u, p in zip(U, lateral):
        y = a * p[:m]
        z = b * (1 + p[m])
        assert abs(np.dot(u, y) + k * z - 1) < 2e-12
    # Deterministic orientations test support inequality for all normal directions.
    rng = np.random.default_rng(20261019 + d * 13 + round(q * 1000))
    B = rng.normal(size=(6000, d))
    B /= np.linalg.norm(B, axis=1)[:, None]
    y = a * B[:, :m]
    z = b * (1 + B[:, m])
    assert z.min() >= -1e-12 and z.max() <= 1 + 1e-12
    assert np.max(np.linalg.norm(y, axis=1) + k * z - 1) < 1e-11
    # Independently test the scalar volume objective against feasible b values.
    vol = b * a**m
    bs = np.linspace(0.000001, 0.5, 2001)
    vols = bs * np.maximum(0, 1 - 2 * k * bs)**(m / 2)
    assert vol >= max(vols) - 1e-12
    return b, a, lower_weight, upper_weight


if __name__ == "__main__":
    n = 0
    for d in range(2, 9):
        threshold = (d - 1) / (d + 1)
        for q in sorted(set([0., threshold / 2, threshold, (1 + threshold) / 2, 1.])):
            for family in ("simplex", "box"):
                b, a, lo, up = verify(d, q, family)
                print(f"CONTACT_AND_VOLUME_OK dimension={d} q={q:.9f} base={family} axial_center={b:.9f} radial={a:.9f} top_weight={up:.9f}")
                n += 1
    print("ALL_FRUSTUM_JOHN_CONTACT_AND_OPTIMALITY_DIAGNOSTICS_OK", n)
