import numpy as np


def phi(gamma, u):
    if abs(u) < 1e-14:
        return 1.0
    return -np.expm1(-gamma * u) / (gamma * u)


def stationary_covariance(h, gamma, alpha, kappa, delta, beta, nq=96):
    z, w = np.polynomial.legendre.leggauss(nq)
    taus = 0.5 * (z + 1.0)
    tw = 0.5 * w
    M = np.zeros((3, 3))
    qbar = np.zeros(3)

    for tau, wt in zip(taus, tw):
        s = (1.0 - tau) * h
        at = tau * h * phi(gamma, tau * h)
        pred_force = delta * alpha * kappa * tau * h * (1.0 - phi(gamma, tau * h)) / gamma
        cx = alpha * h * (1.0 - np.exp(-gamma * s)) / gamma
        ds = alpha * h * np.exp(-gamma * s)
        H = h * phi(gamma, h)
        E = np.exp(-gamma * h)

        A = np.array([
            [1.0 - kappa * cx * (1.0 - pred_force), H - kappa * cx * at],
            [-kappa * ds * (1.0 - pred_force), E - kappa * ds * at],
        ])
        aa, ab, ac, ad = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
        T = np.array([
            [aa * aa, 2.0 * aa * ab, ab * ab],
            [aa * ac, aa * ad + ab * ac, ab * ad],
            [ac * ac, 2.0 * ac * ad, ad * ad],
        ])
        M += wt * T

        zr, wr = np.polynomial.legendre.leggauss(nq)
        r = 0.5 * h * (zr + 1.0)
        rw = 0.5 * h * wr
        u = h - r
        kx = -np.expm1(-gamma * u) / gamma
        kv = np.exp(-gamma * u)
        mask = r <= tau * h
        up = tau * h - r[mask]
        kp = -np.expm1(-gamma * up) / gamma
        kx[mask] -= beta * kappa * cx * kp
        kv[mask] -= beta * kappa * ds * kp
        scale = 2.0 * gamma * alpha
        Qxx = scale * np.sum(rw * kx * kx)
        Qxv = scale * np.sum(rw * kx * kv)
        Qvv = scale * np.sum(rw * kv * kv)
        qbar += wt * np.array([Qxx, Qxv, Qvv])

    vec = np.linalg.solve(np.eye(3) - M, qbar)
    return np.array([[vec[0], vec[1]], [vec[1], vec[2]]])


def predicted_h2(alpha, kappa, delta, beta):
    return np.array([
        [alpha * (1.0 + delta - 2.0 * beta) / 6.0, 0.0],
        [0.0, alpha * alpha * kappa * (1.0 - beta) / 3.0],
    ])


def main():
    gamma, alpha, kappa = 3.0, 1.0, 1.0
    target = np.diag([1.0 / kappa, alpha])
    methods = {
        "LC-REI": (0.0, 0.0),
        "ALUM": (0.0, 1.0),
        "RMM": (1.0, 1.0),
        "half-noise one-gradient": (0.0, 0.5),
    }
    hs = [0.05, 0.025, 0.0125]
    print("numpy", np.__version__)
    print("gamma=3 alpha=1 kappa=1; entries are (Sigma_h-Sigma_*)/h^2")
    for name, (delta, beta) in methods.items():
        print("\n" + name, "predicted h^2 diag", np.diag(predicted_h2(alpha, kappa, delta, beta)))
        for h in hs:
            S = stationary_covariance(h, gamma, alpha, kappa, delta, beta)
            B = (S - target) / (h * h)
            print(f"h={h:.4f}  xx={B[0,0]: .9f}  xv={B[0,1]: .9f}  vv={B[1,1]: .9f}")

    h = 0.0125
    S = stationary_covariance(h, gamma, alpha, kappa, 0.0, 0.0)
    c3 = S[0, 1] / h**3
    print("\nLC-REI cross covariance / h^3 at h=0.0125:", f"{c3:.9f}", "predicted", f"{-1/12:.9f}")


if __name__ == "__main__":
    main()
