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

# Verification summary

The exact identity for the finite-size quadratic projection error is established by stationary generator calculations for the two backward reset ages, followed by the fourth moments of a centered Gaussian. The limiting random measure is obtained from finite-label inclusion convergence and geometric truncation. The infinite-product, cumulant, and exponential-tail statements follow from independent exponential gaps and a higher exponential moment of the remaining sum.

Run `python3 verify_energy.py` with the Python standard library. Its output is `PASS: 10664 bounded arithmetic checks`; the code independently enumerates selected reset subsets for small particle numbers, compares rational finite-population second moments and their bound, and checks finite discounted-exponential products and hypoexponential tails. The simulation-free bounded computations do not establish asymptotic or infinite-volume results, which require the proof in `RESULT.md`.

Scope limitations: all stationary claims require positive parameters and batch fractions tending to a strictly positive limit. The quoted right-tail constant is for the infinite-population energy law and is not uniform in finite population size. No independent audit or validation is represented by these diagnostics.
