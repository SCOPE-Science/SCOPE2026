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
The metric formula is proved by feasible planar unfoldings and a globally 1-Lipschitz glued function, with no appeal to a finite experiment for all surface points. The probability law follows by integrating two explicit planar disk intersections. The exact second moment follows from elementary uniform-coordinate expectations. The endpoint asymptotic follows from a local two-dimensional wedge calculation.

To rerun finite numerical consistency checks, execute `python3 verify_cube.py`. It checks analytic density normalization, surface Monte Carlo CDF and squared-moment comparisons, independently integrated planar area formulas, and upper-tail coefficients. These finite tests cannot independently certify the infinite-dimensional or all-radius assertions.
