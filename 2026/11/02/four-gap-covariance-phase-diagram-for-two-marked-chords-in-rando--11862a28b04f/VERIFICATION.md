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

# Exact verification and scope

Run `python verify_two_marked_chords.py` with Python 3; no nonstandard libraries are required. The script independently enumerates residual perfect matchings for all four-gap compositions and all three ways to pair the four prescribed endpoints for \(n=4,5,6,7\). It compares exact rational means and covariance against the claimed formulas. It also independently evaluates the unfactored pair-indicator expression and the closed form for every four-cell composition with an even total from 4 through 28.

The checked output reports 1,710 exact marked layouts, 866,880 layout–matching combinations and 19,149 exact algebraic comparisons. It separately tests crossing configurations with negative covariance \(-4/9\) at four chords, positive covariance \(36/245\) at six chords, and negative covariance \(-48/245\) at six chords. The script enumerates all strictly positive four-gap compositions at \(n=4\) and \(n=5\) and confirms none has positive covariance. The proof in RESULT.md, rather than finite enumeration, justifies the formula for arbitrary \(n\).

The paper comparisons were made against available primary preprints and their relevant methods and statements. A negative search alone is not a proof of absolute novelty. Independent audit has not been performed.
