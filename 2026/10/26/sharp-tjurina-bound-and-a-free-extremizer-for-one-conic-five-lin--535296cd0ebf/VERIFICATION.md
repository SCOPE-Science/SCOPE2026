---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and scope

The unchanged companion `verify.py` uses exact integer polynomial arithmetic. With standard Python 3, `python3 verify.py` checks both cubic Jacobian syzygies, the determinant \(-147f\), selected tangent and point incidences, and the multiplicity and Tjurina totals; its expected indication of success is `VERIFY_OK`. The proof in `RESULT.md` accounts for all local branches and gives the classification in the stated stratum by normalizing the five lines to a grid and solving the two remaining tangency equations. Neither projective uniqueness nor the comparison with earlier extremizers is a claim of the computational check.
