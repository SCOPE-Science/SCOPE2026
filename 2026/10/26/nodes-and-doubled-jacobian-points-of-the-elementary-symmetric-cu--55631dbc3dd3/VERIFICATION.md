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
# Verification scope

Run `python3 verify.py` using only the Python standard library. The program enumerates every projective point over the field with two elements for dimensions three through twelve, and every projective point over the field with four elements for dimensions three through eight outside the positive-dimensional class. It checks the predicted support sets, Hessian ranks and nonzero radical quadratic values, plus the associated finite point counts. A successful run prints `VERIFY_OK`.

These finite computations test the general symbolic proof but do not exhaust points over arbitrary algebraically closed fields or establish scheme equality by enumeration. The proof of the projective local rings uses localized gradient ideal identities and is given in RESULT.md. The classification of tangent cones uses the polar Hessian and the quadratic value on its radical. No independent audit has been performed.
