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

# Reproducibility checks

The companion `verify.py` computes the mean exit expectation by two independently parameterized radial quadratures and compares them, evaluates the one-dimensional Dawson kernel and its root condition, checks the exact planar exponential-integral identity, samples monotonicity for dimensions \(d=2,\ldots,8\), and verifies the backward-generator equation numerically at interior radii. A successful run prints the total deterministic assertion count and the reference optimum.

Run `python3 verify.py` with NumPy and SciPy installed. The program makes no external requests and uses no stochastic simulations. Its checks validate normalization and numerical consistency for finite parameter selections; the infinite-range existence, strict monotonicity, unique optimizer and planar asymptotic are proved in `RESULT.md`, not inferred from the computations.

The mathematical sources supply the established first-order stochastic-inertia sign and exact OU exit integral. The all-noise comparison theorem and optimizer are supported by the explicit kernel argument in the accompanying proof. Independent audit status: not performed.
