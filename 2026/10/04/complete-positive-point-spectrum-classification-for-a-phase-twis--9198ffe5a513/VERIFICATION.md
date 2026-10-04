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
The bundled `verify.py` reconstructs the coefficient formula in the published Floquet determinant, checks the exact affine dependence on the Bloch quantity, verifies the reduction at the only two possible flat-band branches, and tests representative exceptional and nonexceptional parameters.

The analytic proof, not the finite checker, establishes the universal statement. The checker does not assess negative spectrum, endpoint phases, magnetic flux, or unequal edge lengths.
