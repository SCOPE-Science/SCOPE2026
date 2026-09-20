import numpy as np


def normalized_objects(C):
    n = C.shape[0]
    I = np.eye(n)
    X = np.linalg.inv(I + C)
    H = I + C + C.T
    B = X + X.T - I
    SGS = X.T @ X
    return I, X, H, B, SGS


def random_check(seed=20260920, n=7, delta=0.4):
    rng = np.random.default_rng(seed)
    C = np.tril(rng.standard_normal((n, n)), -1)
    C *= delta / np.linalg.norm(C, 2)
    I, X, H, B, SGS = normalized_objects(C)

    factor_rhs = X.T @ (I - C.T @ C) @ X
    error_rhs = -X @ C @ C.T - X.T @ C.T @ C
    q = 2 * delta**2 / (1 - delta)

    factor_residual = np.linalg.norm(B - factor_rhs, 2)
    error_residual = np.linalg.norm((B @ H - I) - error_rhs, 2)
    inv_dom_min = np.linalg.eigvalsh(np.linalg.inv(B) - H).min()
    eig_BH = np.linalg.eigvals(B @ H).real
    error_norm = np.linalg.norm(I - B @ H, 2)

    assert factor_residual < 1e-12
    assert error_residual < 1e-12
    assert np.linalg.eigvalsh(B).min() > 0
    assert np.linalg.eigvalsh(H).min() > 0
    assert inv_dom_min > -1e-12
    assert eig_BH.min() > 0
    assert eig_BH.max() <= 1 + 1e-12
    assert error_norm <= q + 1e-12

    return {
        "delta": delta,
        "factor_residual": factor_residual,
        "error_identity_residual": error_residual,
        "min_eig_B": np.linalg.eigvalsh(B).min(),
        "min_eig_H": np.linalg.eigvalsh(H).min(),
        "min_eig_Binv_minus_H": inv_dom_min,
        "min_eig_BH": eig_BH.min(),
        "max_eig_BH": eig_BH.max(),
        "error_norm": error_norm,
        "theorem_bound": q,
        "sgs_minus_B_min_eig": np.linalg.eigvalsh(SGS - B).min(),
    }


def counterexample_check():
    C = np.array([
        [0.0, 0.0, 0.0],
        [4.0 / 5.0, 0.0, 0.0],
        [-3.0 / 5.0, -3.0 / 5.0, 0.0],
    ])
    _, _, H, B, _ = normalized_objects(C)
    delta = np.linalg.norm(C, 2)
    eig_H = np.linalg.eigvalsh(H)
    eig_B = np.linalg.eigvalsh(B)
    assert eig_H.min() > 0
    assert delta > 1
    assert eig_B.min() < 0
    return {
        "delta": delta,
        "eig_H": eig_H,
        "eig_B": eig_B,
    }


def two_block_check(seed=314159, m=4, n=3, target_norm=0.7):
    rng = np.random.default_rng(seed)
    K = rng.standard_normal((n, m))
    K *= target_norm / np.linalg.norm(K, 2)
    Zmm = np.zeros((m, m))
    Znn = np.zeros((n, n))
    C = np.block([[Zmm, np.zeros((m, n))], [K, Znn]])
    I, X, H, B, _ = normalized_objects(C)
    expected = np.block([
        [np.eye(m) - K.T @ K, np.zeros((m, n))],
        [np.zeros((n, m)), np.eye(n) - K @ K.T],
    ])
    residual = np.linalg.norm(B @ H - expected, 2)
    assert residual < 1e-12
    return {
        "norm_K": np.linalg.norm(K, 2),
        "product_identity_residual": residual,
        "min_eig_BH": np.linalg.eigvals(B @ H).real.min(),
        "max_eig_BH": np.linalg.eigvals(B @ H).real.max(),
    }


if __name__ == "__main__":
    rc = random_check()
    ce = counterexample_check()
    tb = two_block_check()

    print("random weak-coupling check")
    for k, v in rc.items():
        print(f"{k}: {v}")
    print("\nexact-structure counterexample (floating evaluation)")
    print(f"delta: {ce['delta']}")
    print(f"eig_H: {ce['eig_H']}")
    print(f"eig_B: {ce['eig_B']}")
    print("\ntwo-block identity check")
    for k, v in tb.items():
        print(f"{k}: {v}")
