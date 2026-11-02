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

# Verification

The complete analytic proof and quantifiers appear in `RESULT.md`; this file records reproducibility, not independent validation. The standalone `VERIFY.py` requires Python 3.10+ and no third-party packages. In a directory containing both documents, run `python3 VERIFY.py`. In the saved research package this command completed with `PASS: 52 exact rational assertions and asymptotic convergence checks`.

Checks use `fractions.Fraction` and exact Gaussian elimination to reconstruct the stationary mean and covariance generator, seven positive resetting rates for a three-node star, both signs of leaf frequencies in the leading Gramian, and three clock partitions of a five-node graph. The finite large-rate checks show decreasing exact rational discrepancies, but do not certify an infinite asymptotic; the latter follows from the invertible triangular block system in the proof.

No package dependency beyond the Python standard library is needed. The public model is an exact linear phase-deviation model, not a numerical certificate for nonlinear Kuramoto dynamics. Independent audit has not been performed.
