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

# Verification and reproducibility

The general argument is contained in `RESULT.md`, Steps 1–5. The self-contained standard-library program `CHECK.py` provides supplementary finite arithmetic checks. Run `python CHECK.py` from the extracted directory. It prints exactly:

`VERIFY_OK: 625 exact four-parameter ray/edge tests; 23 family cases`

The program verifies, using exact rational arithmetic, all 18 wall-relation degrees and each ray's convex-hull vertex status for all parameter quadruples with coordinates in the inclusive range from \(-2\) to \(2\). It also checks the infinite-family formulas for the 23 integer values \(2\le m\le24\). An additional independent linear-program cross-check on 250 randomly chosen integer quadruples in the range \([-15,15]\) agreed with the four ray predicates, and 361 restricted-slice cases agreed with their previously reported classification.

Finite checks cannot certify the universal all-integer claim. The mathematical proof establishes that claim independently through strict-inequality elimination and a complete symbolic wall table. The precise assumptions and the residual literature risk are given in `RESULT.md` and `REVIEW.md`. There has been no independent audit.
