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

# Verification notes

Run `python3 verify.py` with Python 3. The program builds finite stage prefixes from binary de Bruijn cycles and checks the exact unmarked-factor and unmarked-reflection-class formulas for lengths two through nine. `check_output.txt` contains a captured successful execution, with the length-nine row reporting 3072 unmarked factors and 2352 unmarked reflection classes.

The prefix checks do not verify all future stages; completeness for arbitrary length follows from the binary de Bruijn property plus three distinct starting phases, while the bound on marked factors follows by separating short markers from long markers. Analytic steps and their quantifiers appear in RESULT.md. No independent audit or external proof certification is claimed.
