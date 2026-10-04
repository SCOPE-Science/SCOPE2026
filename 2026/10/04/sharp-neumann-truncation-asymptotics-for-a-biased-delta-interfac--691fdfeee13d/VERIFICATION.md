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
The scientific proof is analytic and starts from the exact finite-interval eigenvalue equation
\[
k\tanh(kd)+\sqrt{V_0+k^2}\tanh\!\left(d\sqrt{V_0+k^2}\right)=\alpha.
\]
For \(0<V_0<\alpha^2\), expanding at the unique infinite-volume root \(k=a\) gives the stated coefficient. For \(V_0=\alpha^2\), the root first satisfies \(kd\to0\); expansion in \(y=k^2\) gives the resonance prefactor.

`artifacts/verify_asymptotics.py` independently solves the exact scalar equation by bisection for representative parameters and checks convergence of the two rescaled expressions. The finite numerical cases are corroborative only and do not substitute for the limiting proof.

Limits: no explicit uniform remainder constant is certified; the displayed subcritical coefficient excludes \(V_0=0\); no statement is made about the full three-dimensional geometric truncation error.
