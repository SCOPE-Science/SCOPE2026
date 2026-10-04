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
`verify.py` uses only Python's standard library and exact rational sparse-polynomial arithmetic. It reconstructs the generalized Sprott M vector field and verifies the identities
\[
LH=-zp(x),\qquad L(z^2/2)=zw,\qquad L(zw)=w^2-bz^2-zp(x)-zw,
\]
with \(p(x)=x^2-bx-a\) and \(w=a+bx+y\), together with the eliminated jerk equation
\[
\dddot x+\ddot x+b\dot x=x^2-bx-a.
\]
It also checks the canonical \(a=b=17/10\) equilibrium polynomial symbolically over the rationals.

The recorded output is `VERIFY_OK`. The invariant-measure, bounded-complete-orbit, Wirtinger-equality, and literature-comparison arguments are analytic inputs and are not machine-certified. No independent audit has been performed.
