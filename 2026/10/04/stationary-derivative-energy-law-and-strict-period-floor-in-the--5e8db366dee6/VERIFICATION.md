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
`verify.py` uses only Python's standard library and exact rational sparse-polynomial arithmetic. It reconstructs the generalized Sprott L vector field
\[
\dot x=y+\alpha z,\qquad
\dot y=\beta x^2-y,\qquad
\dot z=\gamma-x,
\]
sets \(v=\gamma-x\) and \(w=-(y+\alpha z)\), and checks exactly that the polynomial certificate
\[
C=\frac{w^2}{2}+\frac{\alpha v^2}{2}+\alpha zv
-\frac{\beta}{3}(\gamma-v)^3
\]
satisfies
\[
LC=\alpha v^2-w^2.
\]
It also verifies the eliminated jerk relation
\[
\dot w+w+\alpha v+\alpha z+\beta(\gamma-v)^2=0.
\]

The recorded output is `VERIFY_OK`. The variation-of-constants positivity argument, invariant-support rigidity, Wirtinger inequality, strict equality exclusion, and literature comparison are analytic inputs and are not machine-certified. No independent audit has been performed.
