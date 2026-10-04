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

The analytic verification follows four exact steps.

1. On each eigenmode \(A u=\lambda u\), solve the two signed proximal first-order equations exactly. Their displacements are \(\lambda/(\Lambda_+-\lambda)\) and \(-\lambda/(\Lambda_-+\lambda)\) times the current coordinate.
2. Insert the symmetric-endpoint paired-merit weights \(\Lambda_+/(\Lambda_++\Lambda_-)\) and \(\Lambda_-/(\Lambda_++\Lambda_-)\). Simplification gives the Hessian eigenvalue \(h(\lambda)=\lambda^2/((\Lambda_+-\lambda)(\Lambda_-+\lambda))\).
3. Pair \(\lambda=t\) with \(\lambda=-t\). Their product is \(t^4/((\Lambda_+^2-t^2)(\Lambda_-^2-t^2))\). The maximum at the outer pair divided by the minimum at the inner pair is at least the ratio of the corresponding geometric means, yielding the strict \(\kappa^2\) lower bound. Sending both regularization parameters to infinity proves sharpness of the infimum.
4. Apply the exact scalar-step minimax formula for an SPD quadratic to obtain \(q_*=(\kappa_V-1)/(\kappa_V+1)\).

`verify_paired_merit.py` replays the mode formulas and inequalities for representative admissible parameter pairs. It is finite numerical corroboration, not the proof of the universally quantified statement.

Unproved limits: no claim is made for accelerated or preconditioned outer methods, asymmetric spectral endpoint classes, inexact inner solves, or general nonlinear objectives.
