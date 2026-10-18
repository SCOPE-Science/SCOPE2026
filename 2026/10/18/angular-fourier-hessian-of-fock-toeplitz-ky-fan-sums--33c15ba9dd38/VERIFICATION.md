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

# Reproducibility and limits

The analytical proof in RESULT.md uses a positive spectral gap, a trace-norm differentiable coherent-state integral, and the second-order isolated-spectral-block formula. No finite enumeration is used as a proof of the infinite-dimensional result. The spectral gaps are \(\lambda_j(s)-\lambda_{j+m}(s)=\sum_{r=j+1}^{j+m}b_r(s)>0\) for positive \(s\).

Run `python3 verify.py` to check the exact rational identities on 75 rank–area combinations. The expected terminal line is `FOCK_KYFAN_ANGULAR_HESSIAN_EXACT_IDENTITIES_OK parameter_sets=75`.

Optionally install NumPy and SciPy and run `python3 check_numeric.py`. It computes 22-by-22 Toeplitz compressions by periodic angular quadrature and special-function radial integrals, tests four rank–area combinations at three perturbation scales, and prints `FOCK_KYFAN_QUADRUPOLE_FINITE_MATRIX_CHECKS_OK cases=12` on success. These computations are finite-section consistency checks, not certificates for the tail spectrum or shape differentiability. The proof does not depend on SciPy or NumPy.

Mathematical limits: fixed finite rank, fixed positive area, sufficiently small real perturbations, and smooth real mean-zero angular data. Independent audit has not been performed.
