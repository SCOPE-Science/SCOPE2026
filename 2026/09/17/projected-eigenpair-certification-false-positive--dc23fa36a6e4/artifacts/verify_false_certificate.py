import numpy as np


def check(M=7.0, rho=0.3, delta=1e-8):
    H = np.diag([0.0, 0.0, M])
    A = np.array([[1.0, 0.0, 0.0]])
    ATA = A.T @ A
    Mrho = H - rho * ATA

    # Bounds used in the PSM scaling: lower_lambda_H=0, upper_lambda_H=M,
    # upper_nu_A=1, with s=0.
    eta = rho
    sigma = max(1.0, M + rho)
    K = (Mrho + eta * np.eye(3)) / sigma

    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    P = np.eye(3) - A.T @ np.linalg.solve(A @ A.T, A)

    # Exact false positive.
    target = M
    theta_pen = float(e2 @ Mrho @ e2)
    rM = np.linalg.norm(Mrho @ e2 - theta_pen * e2) / max(1.0, abs(theta_pen))
    uhat = P @ e2 / np.linalg.norm(P @ e2)
    theta_hat = float(uhat @ H @ uhat)
    rfeas = np.sqrt(np.linalg.norm(A @ uhat) ** 2)
    rKKT = np.linalg.norm(P @ (H @ uhat - theta_hat * uhat)) / max(
        1.0, np.linalg.norm(H @ uhat) + abs(theta_hat)
    )

    assert np.allclose(K @ e2, (rho / (M + rho)) * e2)
    assert rM == 0.0 and rfeas == 0.0 and rKKT == 0.0
    assert theta_hat == 0.0 and target - theta_hat == M

    # Robust residual family inside the feasible plane.
    u = np.sqrt(1.0 - delta**2) * e2 + delta * e3
    theta = float(u @ H @ u)
    raw_res = np.linalg.norm(H @ u - theta * u)
    formula = M * delta * np.sqrt(1.0 - delta**2)
    assert np.isclose(raw_res, formula, rtol=1e-10, atol=1e-15)
    assert np.isclose(target - theta, M * (1.0 - delta**2))

    return {
        "M": M,
        "rho": rho,
        "K_eigs": np.linalg.eigvalsh(K).tolist(),
        "target": target,
        "false_value": theta_hat,
        "rM": rM,
        "rfeas": rfeas,
        "rKKT": rKKT,
        "robust_delta": delta,
        "robust_raw_residual": raw_res,
        "robust_value_error": target - theta,
    }


if __name__ == "__main__":
    out = check()
    for key, value in out.items():
        print(f"{key}={value}")
