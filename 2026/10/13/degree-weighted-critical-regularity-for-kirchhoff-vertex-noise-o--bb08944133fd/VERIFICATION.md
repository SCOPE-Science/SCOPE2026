---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python3 verify.py` in the same directory. The script requires only the Python 3 standard library. It verifies positive definiteness of the correlated example covariance, exact parity-dependent endpoint eigenfunction weights, the scaling of symmetric central-vertex modes in equal-arm star graphs, and the ultraviolet cutoff slope. The latter is a finite numerical consistency check, **not** an infinite regularity proof.

The unrestricted conclusion rests on the established positive-length walk expansion of the Kirchhoff heat kernel, the explicit zero-length weight \(2/\deg(v)\), the positivity of the spectral covariance coefficients, Karamata's theorem, spectral Itô isometry, Abel summation, and Gaussian linear-subspace zero-one and Fernique theorems. The source heat kernel and sharpness of its coefficient are independently readable in the cited primary full text. No external validation, independent audit, or external certification is claimed.

The critical formula is specific to the graph and stochastic normalization explicitly defined in `RESULT.md`, with covariance \(\mathbb E[dW_v dW_w]=Q_{vw}\,dt\), semigroup \(e^{-t(I-\Delta)}\), and eigenvalue cutoff of \(I-\Delta\). For an interval of length \(\pi\), \(Q=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\), the exact coefficient is \(5/(2\pi)\). Correlated off-diagonal contributions oscillate by eigenfunction parity and do not contribute to the leading logarithm. The method does not establish uniform estimates under graph degenerations where the minimum edge length tends to zero.
