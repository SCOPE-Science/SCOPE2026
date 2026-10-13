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

The proof is analytic. The bundled `verify.py` performs exact rational checks of the recurrence at \(z=2\) and \(z=6\), verifies the closed forms for the second iterate and the characteristic polynomial evaluated at the backward Euler starter, and confirms the stability-boundary identities \(p(1)>0\) and \(p(-1)=0\) at \(z=6\).

The universal statement for all \(z>0\) is not inferred from finite computation. It follows from the sign of \(a\), the opposite-sign characteristic roots, the strict dominance \(|r_-|>r_+\) for \(z>3/2\), and the exact modal-coefficient sign change at \(z=6\).

Unproved extensions include arbitrary starters, systems, nonlinear equations, variable steps, and other Adams–Moulton orders.
