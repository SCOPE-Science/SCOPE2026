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

Run `python3 checker.py` using the adjacent standalone source. No external packages or network requests are required.

The actual run produced the marker `ALL_EXACT_CHECKS_PASSED`, with 4375 nonempty exact counting cells checked. Direct iteration on all zero-root maps covers chain sizes 2 through 16; independent recurrence and fixed-rank support checks cover sizes 2 through 32. An additional algorithm checks monotone-map normal forms up to size 8.

The depth histograms at chain sizes 5, 8 and 12 are, respectively,

- (1, 4, 2, 1),
- (1, 20, 23, 12, 5, 2, 1),
- (1, 143, 360, 269, 139, 64, 28, 12, 5, 2, 1),

ordered by depth starting from 1. They are independently implied by the proved recurrence.

These computations are finite spot-checks and not an exhaustive proof for unbounded chain size. The proof in `RESULT.md` establishes the universal statement by normal forms, an exact recurrence, defect interpolation, and binomial summation. The literature comparison cannot establish global novelty and has the full-text-access limitation identified in `REVIEW.md`.
