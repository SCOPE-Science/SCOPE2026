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

The proof in `RESULT.md` is the primary verification. It derives necessary and sufficient conditions directly from the strong defensive inequalities and induced connectivity for the unique bridge.

`verify.py` provides an independent finite consistency check. For every pair \(3\le r,s\le7\), it constructs the dumbbell, enumerates every nonempty subset, checks induced connectivity, checks the defining neighbor inequality at every selected vertex, and compares the complete cardinality distribution with the displayed formula. It also checks \(a(D_{r,s})=\min\{\lceil(r+1)/2\rceil,\lceil(s+1)/2\rceil\}\). Formula evaluation for every \(3\le r\le s\le40\) independently checks the stated unimodality classification.

Replay output:

`VERIFY_OK pairs=25 subset_checks=61479 coefficient_checks=275 minimum_checks=25 formula_unimodality_checks=741 max_order=14`

The exhaustive range is finite. It is evidence against implementation or boundary mistakes in the formula, not a substitute for the all-parameter proof.
