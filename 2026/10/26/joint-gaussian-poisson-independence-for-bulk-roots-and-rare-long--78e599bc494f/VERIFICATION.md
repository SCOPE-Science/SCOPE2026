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

Run `python verify.py` using Python 3 standard library. The enumerator checks all 5,040 circular permutations of 7 sites and all 40,320 permutations of 8 sites. It verifies root mean/variance, exact first gap means, and conservation of total root number and total cycle length. This checks normalization and finite definitions only. The joint asymptotic independence proof is the local-deletion Poisson Stein argument in `RESULT.md`; no finite enumeration can prove that limit.

The general Stein indicator solution bounds and the exact neighboring gap probabilities are mathematical inputs; consult the cited mathematical references to reassess their applicability. No independent audit or third-party certification has been conducted.
