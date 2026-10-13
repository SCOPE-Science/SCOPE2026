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
The bundled `artifacts/verify.py` reconstructs the negative-energy Floquet polynomial from the published coefficients and checks symbolically that its derivative with respect to the Bloch quantity is exactly \(2\kappa(1+\kappa^2)\sinh(\kappa\ell)\). It also verifies that removing this affine term leaves an expression independent of the Bloch variable.

The universal claim is analytic. No finite grid, timeout, or numerical sample is used to infer absence of point spectrum. The proof is restricted to \(E<0\) and does not assess the positive spectrum or endpoint phases.
