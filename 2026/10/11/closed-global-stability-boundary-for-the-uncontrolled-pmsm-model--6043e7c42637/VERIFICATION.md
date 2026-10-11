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

The exact derivative identity was replayed from the bundled `verify.py` using a dependency-free polynomial arithmetic check. The checker confirms coefficient-by-coefficient equality between the derivative of the proposed quadratic storage function and \(-x^2-(y-z)^2-(1-\gamma)z^2\), and checks the algebraic substitution for the two nonzero equilibria when \(\gamma>1\).

The proof of global convergence at \(\gamma=1\) is analytic: the zero-derivative set is \(x=0, y=z\), and remaining there requires \(\dot x=y^2=0\). Thus its largest invariant subset is the origin. No finite simulation is used as a substitute for this step.

Limits: this verification covers the zero-input, zero-load autonomous model with \(\sigma>0\). It does not certify controlled or perturbed variants.
