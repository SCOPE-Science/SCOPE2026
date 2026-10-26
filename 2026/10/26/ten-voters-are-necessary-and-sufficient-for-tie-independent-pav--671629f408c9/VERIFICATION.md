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

The complete arithmetic proof is contained in `RESULT.md`: it uses the two singleton strict inequalities, the two pairwise harmonic PAV strict inequalities, integrality, and an exact witness. Its universal assertion does not depend on computation.

The standalone standard-library program `verify.py` exhausts 19,448 anonymous approval profiles on the seven nonempty ballot types, for all voter counts from zero through ten. It independently confirms zero strong nonnesting instances below ten and three at ten, and checks the witness's exact scores. Execute: `python verify.py` (Python 3.10+). Profiles with empty ballots do not change winners and are covered analytically by the lower-bound proof.

No claims about more than three candidates, arbitrary approval weights, or universally nested optimal committees are made. No independent audit was performed.
