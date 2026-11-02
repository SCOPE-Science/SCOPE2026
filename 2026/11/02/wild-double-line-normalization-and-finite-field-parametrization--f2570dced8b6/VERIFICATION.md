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

# Reproduction and scope

Run `python3 verify_steiner_char2.py` with a Python 3 interpreter and SymPy. The script prints `VERIFY_OK` after polynomial identity checks and independent exhaustive finite-field enumerations for orders 2, 4, 8, and 16.

The exhaustive computations test representative finite fields, not all finite extensions. The proof in RESULT.md establishes the general normalization, local conductor and ramification identities, exact finite-field formulas, and their assumptions. The three length-two determinantal local schemes are deduced from the explicit differential minors; their length is not extrapolated from the enumerations.

No independent mathematical audit has been conducted. Historical-priority uncertainty remains regarding older general discussions of characteristic-two Steiner ramification; the arithmetic-image formula was compared separately.
