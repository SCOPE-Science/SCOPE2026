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

# Verification information

Run `python checker.py` with NumPy and SciPy installed; the recorded check output appears in `checker_output.txt`. The code compares finite matrix singular values with exact regularized-beta formulas for six weights, verifies the beta recurrence across multiple radii and monomial degrees, and checks representative numerical asymptotic ratios in all three Schatten regimes and all operator-norm regimes. Slow convergence near the logarithmic and integrability thresholds is explicitly visible in the printed finite-scale ratios; passing these bounded finite comparisons is not a numerical proof of an asymptotic equivalent.

The theorem's infinite-dimensional claims rest on the analytic steps in `RESULT.md`: orthonormal weighted monomial normalization, the beta recurrence, the exact weighted-shift representation, gamma-ratio bounds, Riemann sums with near-zero and far-tail control, and the unimodal unweighted-mode ratio. No external proof certification or independent audit has been performed. The self-review status is separately recorded in `REVIEW.md` and `AUDIT.json`.
