import numpy as np


def verify(eps):
    # Coordinates are taken in an energy-orthonormal pair (phi_1, phi_2).
    z1 = np.array([0.0, 1.0])
    z2 = np.array([eps, 1.0]) / np.sqrt(1.0 + eps**2)
    Z = np.column_stack([z1, z2])
    G = Z.T @ Z

    # Current error is phi_2; the one-dimensional tangent correction is xi*phi_1.
    e = np.array([0.0, 1.0])
    tangent = np.array([1.0, 0.0])
    b = Z.T @ e
    J = Z.T @ tangent

    xi = float((J @ b) / (J @ J))
    residual0 = b
    residual1 = b - J * xi
    loss0 = float(residual0 @ residual0)
    loss1 = float(residual1 @ residual1)
    energy0 = float(np.linalg.norm(e))
    energy1 = float(np.linalg.norm(e - xi * tangent))

    xi_gram = float((J @ np.linalg.solve(G, b)) / (J @ np.linalg.solve(G, J)))
    eig = np.linalg.eigvalsh(G)
    kappa = float(eig[-1] / eig[0])
    xi_from_kappa = 0.5 * (np.sqrt(kappa) - 1.0 / np.sqrt(kappa))
    amp_from_kappa = 0.5 * (np.sqrt(kappa) + 1.0 / np.sqrt(kappa))

    return {
        "eps": eps,
        "unit_norm_error": max(abs(np.linalg.norm(z1) - 1), abs(np.linalg.norm(z2) - 1)),
        "xi": xi,
        "xi_exact": 1.0 / eps,
        "loss0": loss0,
        "loss1": loss1,
        "energy_amp": energy1 / energy0,
        "gram_xi": xi_gram,
        "kappa": kappa,
        "xi_from_kappa": xi_from_kappa,
        "amp_from_kappa": amp_from_kappa,
    }


print("Unit-normalized weak Gauss-Newton frame obstruction")
print("Columns z1,z2 are expressed in an energy-orthonormal basis.")
for eps in [0.5, 0.2, 0.1, 0.05, 0.02]:
    r = verify(eps)
    print(
        f"eps={r['eps']:.5f}  "
        f"unit_norm_err={r['unit_norm_error']:.3e}  "
        f"xi={r['xi']:.12f}  "
        f"1/eps={r['xi_exact']:.12f}  "
        f"loss_sq:{r['loss0']:.12f}->{r['loss1']:.12f}  "
        f"energy_amp={r['energy_amp']:.12f}  "
        f"gram_xi={r['gram_xi']:.3e}  "
        f"kappa={r['kappa']:.12f}  "
        f"xi(kappa)={r['xi_from_kappa']:.12f}  "
        f"amp(kappa)={r['amp_from_kappa']:.12f}"
    )
