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

# Reproducibility notes

Run `python verify.py` with the Python dependency in `requirements.txt`. The verification uses exact rational arithmetic to build transfer matrices from the velocity-jump generator on constant-rate segments, calculate the monodromy trace through second order in its eigenvalue, and compare four independently obtained coefficients with the analytically predicted spatial primitive-energy expressions. A profile with positive fourth-cumulant rate is included.

This checks 34 discrete rational test profiles, not an exhaustive family of positive periodic functions. The all-profile result follows from the displayed analytic derivation in RESULT.md. The mathematical originality comparison is limited to the specifically identified primary material. Independent audit status: not performed.
