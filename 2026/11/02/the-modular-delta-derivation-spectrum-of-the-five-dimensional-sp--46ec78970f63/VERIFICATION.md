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

Run `python verify.py` with Python 3 and SymPy. The checker builds the fifty-by-twenty-five defining matrix independently from the seven nonzero brackets. Its exact polynomial row eliminations only divide by unit coefficients \(\pm1\), hence remain valid in every characteristic. It checks all nineteen reduced rows against the independently typed polynomial certificate before testing the dimension formula over every parameter of six odd prime fields and at five rational parameters.

Observed results include dimensions \(8,1\) at \(\delta=1,-1\) in characteristic three, respectively, and dimensions \(6,5\) at \(\delta=1,-2\) in characteristic five; the complete output is `verify_output.txt` and ends in `VERIFY_OK`.

The finite-field tests are not an infinite-field proof. The exact, symbolic unit-pivot matrix equality plus the five-equation kernel calculation in `RESULT.md` supplies that proof. No numerical floating-point arithmetic or external certification is used. Independent audit has not been performed.
