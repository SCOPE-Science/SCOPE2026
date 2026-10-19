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
# Reproducibility

The standalone `verify.py` checks the derivative factorization with SymPy, the right-Gaussian angular identity by deterministic quadrature, the strict location of the ridge optimum against several positive alternatives for multiple sketch sizes and diagonal condition ratios, samplewise agreement between the original matrix formula and the orthogonal error formula over seeded independent Gaussian draws, the zero-ridge second-moment identity for three or more rows, and the Student–beta tail identity in the isotropic case. Running `python verify.py` with NumPy, SciPy and SymPy yielded **6,049 checks passed**.

The infinite-parameter claims require the analytic proof in `RESULT.md`; tests do not certify unbounded dimensions, all real parameters, or the mathematical novelty of the result. A complete independent audit has not been performed. No stochastic time-integration trajectory or floating-point robustness bound has been validated.
