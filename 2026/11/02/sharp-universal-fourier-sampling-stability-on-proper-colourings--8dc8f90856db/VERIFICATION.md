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

# Reproducibility

Run `python3 checker.py` from the directory containing this file and the checker. Python 3.10 or newer suffices; no third-party packages are required. The checker enumerates all proper colourings of the listed small cycles and computes exact rational conditional colour probabilities before evaluating their spatial Fourier transforms. It separately performs finite parameter-grid positivity and sharp-bound spot checks. Passing numerical DFT and finite grid tests does not prove the theorem for unbounded alphabets or cycle sizes; the algebraic transfer-matrix and inequality argument in `RESULT.md` supplies that proof.

The exact source date is based on the archived first public submission of the 1994 Potts covariance work. Other papers and literature comparisons are identified in `RESULT.md` and `REVIEW.md`. No independently commissioned proof verification or external mathematical audit has been performed.
