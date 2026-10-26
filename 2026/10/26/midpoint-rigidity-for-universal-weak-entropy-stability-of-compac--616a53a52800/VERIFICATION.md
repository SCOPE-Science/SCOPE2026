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

The `checker.py` script uses the standard-library rational number implementation; execute with `python checker.py` from the directory containing the script. Its successful execution checks 320 exact coefficient/entropy identities, one explicit strongly convex counterexample with defect \(-1/3072\), 16 rational members of the universally failing non-midpoint class, three midpoint Courant-bound counterexamples, and the full-update Fourier determinant formula. The code is a finite independent algebraic check, not a substitute for the proof of the universally quantified entropy claims. The negative construction and all-convex positive result are proved in RESULT.md; neither relies on numerical extrapolation. No independent scientific audit has been performed.
