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

# Reproduction

Use Python 3.9+ and run `python verify.py` from the directory containing the embedded artifacts. The script uses only the standard library, enumerates labeled-stub perfect matchings for the listed small degree profiles, and checks loop counts and simple-vertex cycle multiplicities directly against exact `Fraction` formulas. An observed passing run reported 549 exact rational comparisons and 148080 enumerated matching-cases, plus regular sign checks for all valid parameters with 3<=n<=13 and 2<=d<=8.

The mathematical proof in RESULT.md establishes the unrestricted claims: probability 1/P_r for each specified stub-cycle, the loss of potential loops on its vertices, and subtraction of moments. Finite checks confirm sample cases but do not certify infinite ranges. The 1981 short-cycle historical paper was not accessible in full; literature-priority uncertainty remains. No independent audit has been performed.
