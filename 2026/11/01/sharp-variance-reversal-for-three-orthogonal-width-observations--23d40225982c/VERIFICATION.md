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

`check_frame.py` implements an independent two-dimensional Gauss–Legendre quadrature for the mixed Haar matrix-entry moment and uses 400,000 seeded independent uniform rotations to evaluate the three marginal widths and their perpendicular-pair covariance. It checks six choices of positive box dimensions, including both near-zero-covariance thresholds and elongated and cubic boxes; it separately compares the variance of the average of the three perpendicular widths with the analytic frame formula. Execute `python3 check_frame.py` after installing the two packages recorded in `requirements.txt`.

The expected terminal marker from successful execution is `ALL_ORTHOGONAL_WIDTH_TESTS_PASSED` (observed in the completed execution). All finite numerical tolerances are explicit in the code. Monte Carlo and numerical integration are supplementary; the universal statements follow from the iterated-conditional-expectation calculation and sharp one-variable monotonicity proof in `RESULT.md`. The left sharp bound is not attained by full-dimensional boxes. The full joint width law and an optimality theorem over all nonorthogonal designs remain unproved.
