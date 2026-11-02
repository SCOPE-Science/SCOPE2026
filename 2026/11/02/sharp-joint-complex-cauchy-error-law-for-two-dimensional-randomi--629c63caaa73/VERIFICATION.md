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

# Reproduction

Run `python VERIFY.py` with Python 3, NumPy, and SciPy. This script uses a recorded deterministic random seed, checks the exact example's compressed Hermitian matrix at several trial angles, compares numerical generalized eigenpairs with their analytically derived first-order limits, repeats that comparison for randomly rotated four-dimensional Hermitian examples with nonzero *complex* coupling, and verifies empirical Cauchy marginal and joint-tail frequencies. The analytic proof in `RESULT.md`, not finite random sampling, establishes the probability law in all permitted dimensions.

# Mathematical limits of these checks

The number of tested matrices and random probes is finite. Sampling cannot certify an exact continuous distribution or an almost-sure statement. Those conclusions rest on an analytic simple-root argument, the complex-Gaussian Jacobian, and exact polar integrations. Near-singular compressed matrices cause large coefficients and are accounted for in the law rather than discarded theoretically. The program treats random numerical near-singular cases with relative error tolerances appropriate to finite precision.

No independent audit has been performed.
