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

The program `verify.py` uses rational arithmetic to check the inverse-branch sum and exact transfer identity at 858 grid points and to compare eleven exact rational return tails with independently integrated polynomial expressions. It tests a large scalar-iteration instance of the asymptotic limit and runs without third-party dependencies.

Command: `python3 verify.py`

Observed output: `VERIFY_OK exact_transfer_grid=858 exact_return_tails=11 asymptotic_steps=100000`

The mathematical proof in `RESULT.md` establishes all identities for infinitely many return times. The program is a finite consistency test and does not certify publication priority, mixing, or independent validation.
