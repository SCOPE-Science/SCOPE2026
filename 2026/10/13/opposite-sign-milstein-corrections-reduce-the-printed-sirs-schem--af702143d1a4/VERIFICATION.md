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

The source recurrence and its cited Milstein formula were compared symbolically at the level of the diffusion field. For \(g(x)=-qx\), the product \(g(x)g'(x)=q^2x\) is positive, fixing the second-order correction sign.

The accompanying checker evaluates the exact finite-step mean-square identities for both signs on a decreasing mesh. It verifies convergence of the printed-sign normalized error to \(2e^{q^2T}q^4T\) after division by \(h\), and of the correct-sign normalized error to \(e^{q^2T}q^6T/6\) after division by \(h^2\).

The exact strong-order calculation is for the scalar multiplicative-noise test. No executable code from the motivating article was inspected, so this package does not infer which sign was used to generate its figures.
