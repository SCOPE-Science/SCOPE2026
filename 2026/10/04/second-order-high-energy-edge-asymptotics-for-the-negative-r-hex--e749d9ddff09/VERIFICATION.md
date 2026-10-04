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

The analytic check starts from the exact functions \(h_+(k)=(1-18k^2+9k^4)/(3k^2+1)^2\) and \(h_-(k)=(1-3k^2)/(1+3k^2)\). For even centers it expands \(\cos(2l\delta)=h_+(K_m+\delta)\); for odd centers it expands \(-\cos(2l\delta)=h_-(K_m+\delta)\). The simple roots of the scaled limiting equations justify the local branches.

The bundled `verify.py` solves the exact unexpanded equations by bisection at \(l=0.8,1,1.7\) and both parities, checks convergence to the displayed energy expansions over increasing indices, and checks the flat-band parity. It prints `VERIFY_OK`.

Finite numerical checks are supplementary and are not used to prove the all-large-index statement.
