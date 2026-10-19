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

Run `python3 check.py` with Python 3 and no third-party dependencies. The output should end with `All finite checks pass; profiles analyzed=30007`.

The program enumerates relevant small multiset vectors and checks pairwise intersections, the explicit two-phase capacity constructions, the `n=q+1` lower-bound construction, the forced heavy profiles at two rigidity endpoints, and the complete ternary optimal-codebook lists at lengths five and six. Its assertions are exact integer tests. The accompanying `CHECKS.txt` records a successful execution. Arbitrary values of the alphabet size and blocklength are covered by the mathematics in `RESULT.md`, not by these finite checks.

No independent external audit has been performed.
