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

# Reproducible verification

The theorem is established by the stationarity-generator identities and a sign-variation argument for an explicit quartic. Run `python check_moments.py` from this package using Python 3 and SymPy. The checker derives the mixed-moment recurrence, verifies the centered third-moment identity by exact polynomial cancellation, checks the zero-reset limit and the auxiliary coefficient inequalities, and samples several physical parameter sets to illustrate one positive root. All symbolic identities are exact; the finitely many numerical examples are not claimed as an exhaustive proof. Existence, uniqueness, and the sign behavior over the entire parameter domain rest on the analytic proof in `RESULT.md`.

The orientation is *unchanged* at position resets. No independent auditing, external formal verification, or literature-priority certification is implied by these calculations.
