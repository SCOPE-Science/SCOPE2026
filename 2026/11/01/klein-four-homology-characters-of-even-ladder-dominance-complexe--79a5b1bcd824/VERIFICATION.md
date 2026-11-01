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

Execute `python3 checker.py` using a standard Python 3 installation; no third-party packages or downloaded data are needed. The checker constructs exact integer transfer matrices and checks the two finite-dimensional identities used to prove the universal trace formulas. It also independently enumerates face orbits under the four symmetries for five even widths and computes reduced mod-two simplicial homology using boundary-matrix elimination for three widths.

Exact saved output appears in `checker.out`. The marker `LADDER_DOMINANCE_KLEIN_FOUR_EXACT_OK` is reached only after all assertions. Exhaustive finite checks supplement the explicit transfer-matrix recurrence proof; they do not by themselves certify all widths. The external nonequivariant homology theorem is cited rather than re-proved. No independent audit was performed.
