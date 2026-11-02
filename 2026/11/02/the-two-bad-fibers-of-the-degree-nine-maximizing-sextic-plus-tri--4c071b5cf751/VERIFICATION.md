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

# Reproducibility and scope

Run `python3 verify_maximizing9.py` in the containing directory with Python 3.8 or later. No third-party packages are used. The program reconstructs the integral degree-nine equation, verifies exact mod-two and mod-three special-fiber identities and the complete three-generator Jacobian identities, substitutes the characteristic-two normalization forms, verifies its node's formal quadratic tangent cone, counts characteristic-two and characteristic-three rational support points, checks the node Hessian determinant in the displayed generic coordinates, and tests the integral marked-sign reductions.

A successful execution prints `MAXIMIZING9_ALL_CHARACTERISTIC_IDENTITIES_NORMALIZATION_AND_MARKED_COLLISIONS_PASS`. This is an exact executable check of its stated finite polynomial assertions, not independent mathematical review. The full all-characteristics classification, Bézout irreducibility argument, local coordinate reductions and saturated-ideal argument are written in RESULT.md; their proofs do not rely on sampling primes. In particular the numerical tests at small odd primes are not used to certify that no other exceptional primes exist. The supplied proof and code make no claim about intrinsic positive-characteristic freeness or a model-independent degeneration.
