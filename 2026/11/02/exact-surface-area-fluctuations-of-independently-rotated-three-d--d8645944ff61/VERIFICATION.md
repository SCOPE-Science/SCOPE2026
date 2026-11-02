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

# Reproducibility and verification

Install Python 3, NumPy, and SciPy, then run `python verify.py` from the directory containing the included script. The script is deterministic, using random seed `202610311`. Its final successful marker is `ALL_3D_ROTATED_MINKOWSKI_SURFACE_CHECKS_PASSED`.

The critical independent geometric check integrates the determinant of the support Gauss-map Jacobian \(\det(hI+\nabla^2h)\) using Gauss–Legendre and periodic quadrature, separately from the exact spherical-harmonic area expression. It compares three-dimensional Minkowski sums with one degree-two support mode and with an independent degree-two/degree-four mixture. Exact one-mode deficit values in this checker are \(\delta_2=8\pi\varepsilon^2/5\), and for the added degree-four mode \(\delta_4=4\pi\eta^2\).

Monte Carlo independently checks finite-sample expectation and variance in the degree-two family at \(n=2,5,20\). With \(n=260\) it compares the centered area law to the specific predicted \(\delta_2(1-\chi_5^2/5)\) limit using the empirical Kolmogorov distance of independent samples.

The analytical proof, not the finite checker, establishes the all-body support identity, matrix-coefficient orthogonality, full variance sum, weak convergence, the infinite tail bound, and the sharp equality classification. Numerical sampling cannot certify infinite identities, general nonsmooth convex bodies, or historical originality. Independent audit is not performed.
