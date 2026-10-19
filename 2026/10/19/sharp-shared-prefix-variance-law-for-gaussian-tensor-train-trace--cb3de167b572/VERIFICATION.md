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

Run `python3 verify_shared_tt.py` with NumPy >= 1.24. It uses a fixed local random seed and reads no external input files. The program was executed on the included exact code and produced `PASS: 11529 exact algebraic/asymptotic and supporting Monte Carlo checks`.

Its exact-rational assertions test the finite formula, the independent-core special case, the single-probe case, the monotone variance reduction in the number of suffix resamplings, and positivity of the shared-prefix floor. Floating-point checks cover representative points on the proportional-order limit. Direct simulated Gaussian TT contractions test the separable-witness fourth moment and shared cross-probe moment for four parameter choices. An independent two-mode nonseparable contraction tests the inequality away from an extremizer.

The proof in `RESULT.md`, not Monte Carlo, establishes universal sharpness, exact moments, almost-sure nonconsistency and weak convergence to the lognormal prefix law. Numerical tolerances are explicitly coded and do not constitute infinite-dimensional verification. The source comparisons and independent publication audit remain subject to the stated bibliographic limitations.
