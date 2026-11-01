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

## Reproducibility

Execute `python3 verify.py` with Python 3 standard library, in a directory containing the attached `verify.py`. The 13 state face vectors, exact integer cellular cancellations, triviality of the two required fundamental groups, and three relative simplicial collapses are checked from enumerated simplices. The checked relative collapses have 12, 24 and 60 pairs. The recorded output is `verification_output.txt`.

## Limits

The finite program proves the stated finite combinatorial assertions only when its source and mathematical construction are inspected. All-real \(t\) claims depend on the symbolic distance identities and the algebraic classification of crossing values, not on numerical sampling. The integral persistence map assertions follow from the geometric cap-and-annulus arguments in `RESULT.md`. No independent audit has been performed.
