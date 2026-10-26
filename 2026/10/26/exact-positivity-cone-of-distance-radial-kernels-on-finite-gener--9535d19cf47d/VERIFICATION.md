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

## Checks performed

Symbolic calculations in `checker.py` verify the six independent exponential-kernel sector factorizations (four diagonal sector formulas and two determinants), both scalar factors, and the nullspace dimension identities. The script constructs the full 30-vertex symplectic generalized quadrangle over the binary field, derives all graph distances by breadth-first search, verifies the exact incidence spectrum and compares four kernel spectra and ranks with the theorem.

## Boundaries of verification

The checker is a finite diagnostic, not an infinite proof. The complete universal result rests on the incidence/SVD decomposition in RESULT.md. Sources were checked by material and implication; coverage of all mathematical literature was not established. Independent audit and validation remain unperformed.
