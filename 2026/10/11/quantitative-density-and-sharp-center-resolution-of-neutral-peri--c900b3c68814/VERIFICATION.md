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

The complete universal argument is in `RESULT.md`: inverse base branches yield a periodic point for the mixed word; exact center push/pop cancellation gives the chosen neutral fiber; every balanced center word has reduced prefix-replacement form giving the sharp depth bound.

Run `python verify_general_neutral_localization.py` using Python's standard library. This script uses `fractions.Fraction`, not floating point, and tests all base words through length three and all center words through length three for three rational parameters at each of dimensions two, three and four. It checks word length, symbolic admissibility, exact periodicity for two interior points per fiber and prescribed center-prefix containment. Expected last line: `PARAMETER_UNIFORM_NEUTRAL_LOCALIZATION_CHECK_OK`.

Finite replay does not prove all parameters or arbitrary word lengths. No independent audit or external certification has been performed.
