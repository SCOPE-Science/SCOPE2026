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

Run `python3 check_constraints.py` from the package directory. It checks the numerical cases and the cubic–cubic congruence. The proof in RESULT.md separately establishes the projective geometric premises: every A5 point on a smooth cubic and line is a saturated flex contact, a D4 singularity has three transverse local branches, and all line pairs are accounted for exactly once. This is a finite self-check, not an independent audit. The remaining (2,3;3,0,9) case is not decided.
