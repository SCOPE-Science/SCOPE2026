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

The all-odd-base formulas are proved by cases and exact finite symbolic sums in `RESULT.md`. Run `python3 verify.py` (Python 3 standard library). The program independently performs base-dependent four-digit integer subtraction, checks every difference state for each odd base from 5 through 101, verifies the unique three-step state, compares exact multiplicity sums, and then directly enumerates every ordered nonconstant four-digit word for bases 5, 7, 9 and 11.

`verify_output.txt` is the recorded output of an actual run. These computations do not check infinitely many bases; the displayed general argument establishes the formula. No independent audit is claimed.
