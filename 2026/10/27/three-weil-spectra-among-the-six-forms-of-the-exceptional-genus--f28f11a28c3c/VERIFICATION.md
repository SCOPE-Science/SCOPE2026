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

The standalone `verify.py` performs exhaustive finite-field counts for all six models over degrees one, two and three, computes their Weil polynomials using Newton identities and the genus-three functional equation, checks all Hasse–Witt coefficients, and prints `VERIFY_OK`. Polynomial moduli have degrees two and three and are checked for absence of roots; hence each yields a field. The finite computations do not by themselves prove a statement for all extensions; the Weil functional equation gives that extension. Smoothness, twists, and isomorphism classification use the proofs and cited theorems in RESULT.md. No independent audit or validation has been performed.
