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

The analytic proof in `RESULT.md` establishes the all-iteration recurrence and verifies both line-search stages.

`artifacts/verify_soft_threshold_tail.py` replays representative rational instances of the source formulas. It checks exact soft-thresholding, positivity of the corrected denominator, cancellation of the three-term correction, acceptance of the full trial and Armijo steps, and the geometric iterate formula.

The finite checks are supporting evidence only; the universal statements over the displayed parameter basin follow from the symbolic inequalities in the proof.
