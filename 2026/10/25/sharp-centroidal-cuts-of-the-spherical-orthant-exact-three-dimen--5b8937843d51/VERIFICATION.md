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

From the package directory, run `python3 verify.py` with Python 3, NumPy, and SciPy. This checks the closed spherical-triangle formula against independently parameterized surface-area quadrature for seven parameter values (including both endpoints); evaluates the signed second derivative; and checks uniform orthant sampling with absolute Gaussian vectors. The deterministic seeded trials run at four angular values and at six dimensions (two, three, four, six, ten, thirty); the observed fractions agree with the analytic benchmarks within sampling error. All checks were actually executed successfully before packaging.

The analytic proof in `RESULT.md`, not simulation, establishes global optimality and the infinite-dimensional-index monotonicity assertion. In particular, the strict concavity identity for the full cut-normal parameter and the leave-one-out Jensen argument are the controlling certificates. The numerical program is not an exhaustive search or external audit.

The 2026 universal spherical Grünbaum bound is \(4/9\) in dimension three; the exact sharp octant minimum is approximately \(0.4645590544\). No higher-dimensional global minimum is asserted.
