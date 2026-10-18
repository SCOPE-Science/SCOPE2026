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

Run `python3 verify.py` with Python 3 and SymPy. The verifier executes independent exact multinomial coefficient expansion for the four paired Cartier coefficients in characteristic \(41\), verifies both polynomial factorizations and their greatest common divisor, and checks squarefreeness, explicit finite-field Frobenius irreducibility, the nonvanishing at singular boundary \(v=4\), the nonsquare rational coarse parameters and the root-orbit degrees.

Expected terminal token: `VERIFY_OK`.

The symbolic checks are finite identities, not a computational search for all curves over an algebraic closure. Exhaustiveness follows from the diagonal Cartier matrix, the irreducible polynomial factorizations, and the published geometric-isomorphism criterion. Independent audit has not been performed. The argument makes no claim about the complete \(41\)-divisible group or minimal fields of definition of normalized equations.
