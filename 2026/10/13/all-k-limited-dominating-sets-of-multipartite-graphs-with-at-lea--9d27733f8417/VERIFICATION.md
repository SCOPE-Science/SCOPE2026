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

The analytic proof is the primary evidence.

`artifacts/verify.py` enumerates every nondecreasing part profile of total order \(3\) through \(9\) with at least three parts. For every profile and every integer \(1\le k<\Delta(G)\), it checks every vertex subset directly from graph neighborhoods.

The script compares that direct definition with the support/omission criterion, independently expands the displayed cardinality enumerator coefficient by coefficient, and compares the least feasible cardinality with the closed support formula.

Replay output:

`ALL CHECKS PASSED; profiles=67; parameter_cases=367; subset_checks=121480; orders=3..9`

The finite computation is corroborative only. The arbitrary-order characterization, enumerator, and minimum formula are proved in `RESULT.md`.
