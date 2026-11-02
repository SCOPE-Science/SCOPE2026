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

The analysis is a finite-word exact counting proof for all finite control patterns. The two inverse branches of the tent map have slopes of absolute value two, so their itinerary is a sequence of fair independent sign symbols under normalized Lebesgue measure. The active plateau is the occurrence of \(RL\) in the two symbols following a controlled instant; consecutive requested occurrences cannot overlap, and blocks separated by a free instant use disjoint symbol coordinates. Exact run counts and the strictly positive block-merger identity establish all universal statements and equality cases.

Run `python verify_tent.py` with Python 3. The code uses `fractions.Fraction` and compares direct exact branch-cylinder orbit tests against the product formula for every deterministic control schedule through eight steps, and checks the fixed-budget sharp min/max for all budgets at those horizons. Its assertions are supplementary consistency checks and do not enumerate all possible horizons. No numerical approximation, external data, or infinite-machine certification is used.

An independent audit has not been performed. The scientific limits and incomplete source access are set out in `RESULT.md`, `REVIEW.md` and `AUDIT.json`.
