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

# Reproducibility

Run the included `verify.py` with Python 3.9 or later, using only the standard library. The program independently checks the two original confluence quantifiers on every binary relation for rooted stars with one, two or three leaves; compares the resulting raw labelled and orbit counts with the closed formulas; directly counts permutation-fixed relations through five leaves using admissible successor rows; and evaluates both formulas through six leaves.

The observed output ends in `VERIFY_OK`. This is a finite cross-check of the proof and not a proof of the general theorem by itself. The proof relies on the stated three-case normal form and a Burnside cycle-index argument. No independent mathematical audit has been performed.
