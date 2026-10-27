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

The standalone standard-library `check.py` was run against the files of this result. It produced `PASS: 3810 exact rational identities across dimensions 1..30; independent Laplacian inversions in dimensions 1..5`.

The checks verify exact Walsh/Krawtchouk kernel arithmetic, strict radial monotonicity, row-sum cancellation, the endpoint absolute-row-sum formula, and independent small-dimension inverses. The unbounded-dimension estimate is proved by binomial concentration, the explicit radial sign cutoff, and a chi-square heat-kernel tail estimate, not certified by finite experiments.

Scientific limitations and literature-access caveats appear in RESULT.md and REVIEW.md. Independent auditing has not been performed.
