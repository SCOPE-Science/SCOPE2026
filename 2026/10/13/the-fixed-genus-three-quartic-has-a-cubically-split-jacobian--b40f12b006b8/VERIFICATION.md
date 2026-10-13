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

The verifier `verification/verify.py` uses exact rational arithmetic. It checks the two invariant-field discriminants, the determinant of the full Klein-four quotient conic, the Weierstrass invariants for both signs of the quartic coefficient, and the exact value \(j=148176/25\).

The isogeny step is not inferred from finite computation: the proof uses the action of the Klein four group on \(H^0(C,\Omega_C^1)\). The full quotient has genus zero, while each nontrivial involution quotient has genus one, forcing the three nontrivial character spaces to occur once each. Thus the product pullback map has an isomorphism on tangent spaces and is an isogeny.

The verification does not compute the exact kernel or polarization type, and no claim about either is made.
