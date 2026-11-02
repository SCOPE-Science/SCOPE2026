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

The proof is self-contained in `RESULT.md`: exponential-reset regeneration gives the integral stationary law; strict likelihood-ratio comparison gives monotonic adjacent ratios; the Markov stationary balance equation yields unimodality and strict threshold ordering. All positive parameter values are treated analytically. The finite exact-rational computations are corroboration rather than a proof of universal quantification.

Run `python checker.py` with a standard Python 3 interpreter. It uses exact fractions for the Beta moment expansion and the generator equations, verifies the three sample vectors, exhaustively checks differences and adjacent-ratio monotonicity on a specified finite rational parameter grid, and verifies rational brackets for the two illustrative threshold equations. These checks neither cover real parameters exhaustively nor provide independent audit. Scientific limitations and historical-priority risks appear in `RESULT.md` and `REVIEW.md`.
