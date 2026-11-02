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

Run the standard-library standalone script `python3 corona_negative_type_checker.py`. It constructs the graph adjacency lists and shortest-path matrices from first principles, independently compares each entry with the proposed distance classes, verifies the global contrast and both standard-block bilinear forms for seven exponent choices, and checks the critical-root equation, positivity of the noncritical determinant, strict monotonicity, and both asymptotic scaling laws. The observed run printed `CHECKS_PASSED 26836` and the illustrative critical exponent values in `RESULT.md`.

These are finite reproducibility checks. The universal statements, strictness at the endpoint, and Euclidean embedding ranks depend on the complete analytic symmetry decomposition and inequalities in `RESULT.md`, not on extrapolating the finite checks. All source comparisons are bounded by the material actually inspected. No independent audit or independent mathematical validation has been performed.
