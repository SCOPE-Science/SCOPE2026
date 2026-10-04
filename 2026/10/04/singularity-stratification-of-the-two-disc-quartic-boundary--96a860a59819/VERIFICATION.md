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

The exact checker is `artifacts/verify_target.py`. It verifies the coordinate factorization and all first derivatives; computes a Gröbner basis after adjoining \(1-tw\), which proves the singular system has no solution on \(w\neq0\); checks the transverse Hessian determinant \(4a^2(a^2-4)\); verifies the nonzero coordinate derivative for the two pinch values \(a=\pm2\); and checks the factorization and nonzero value of the origin discriminant.

Run:

`python3 artifacts/verify_target.py`

Expected terminal line: `VERIFY_OK`.

The checker certifies exact polynomial identities over the rationals. The analytic steps additionally use standard characteristic-zero facts: the analytic inverse function theorem, the parametric Morse lemma for a nondegenerate transverse quadratic form, and existence of analytic square roots of units near the origin. It does not inspect the projective closure at infinity.
