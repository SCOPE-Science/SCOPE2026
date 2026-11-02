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

# Verification and scope

The self-contained `verify.py` uses only Python 3's standard library, implements exact binary finite fields by polynomial quotient arithmetic, and enumerates all normalized projective points of the surface over fields of cardinalities 2, 4, 8, and 16. Run `python3 verify.py` to reproduce `VERIFIER_OUTPUT.txt`; the terminal status is `VERIFY_OK`.

The proof, not finite experimentation, establishes irreducibility, normality, the unique geometric singularity, the 16-dimensional Tjurina algebra, birationality over the base field, twelve geometric lines through the singular point, and the all-extension point-count formula. The finite checks test algebraic identities and four extension fields, not the infinitely many extension fields.

This calculation concerns the singular quartic itself. It does not construct or count points on its minimal resolution, and it does not classify lines not passing through the singular point. No independent scientific audit has been performed.
