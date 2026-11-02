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

# Verification and scope
The elementary proof in `RESULT.md` establishes all dimensions \(d\ge3\) and the full real truncation interval \(0\le t<1\). The two nonstandard steps are (a) the exact reduction of all John halfspace contacts to one determinant optimization and (b) the explicit positive two-orbit Löwner moment/contact certificate. The final derivative and sharp limit are algebraic consequences.

Run `python3 verify.py` from the extracted package directory. It uses only Python's standard library, checks 225 finite dimension/parameter configurations, and ends with `VERIFY_OK`. Its checks include all support equalities, both endpoint-orbit gauge values, the weighted covariance normalization, exact ratio inequalities and sampled strict monotonicity.

For an independent numerical approximation, run `python3 independent_numerics.py` if NumPy and SciPy are installed. This separately optimizes the determinant with nonlinear inequality constraints for the John and Löwner ellipsoids in dimensions 2, 3 and 5, each at four nonzero truncation depths. All 24 optimization problems solved successfully in the recorded run; the largest parameter discrepancy was below \(3.2\times10^{-9}\). Two-dimensional cases are consistency checks, not novel claims.

No finite grid verifies the full real parameter interval. No computer-assisted global optimality, independent scientific audit or historical-priority certification is claimed. Planar trapezoid ellipses and the untruncated simplex case have established predecessors; the new higher-dimensional frustum theorem must be assessed separately for historical priority.
