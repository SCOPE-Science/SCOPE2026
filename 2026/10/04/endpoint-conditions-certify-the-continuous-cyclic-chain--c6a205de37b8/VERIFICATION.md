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

The analytic verification uses the definitions in the continuous model and differentiates them directly. The included `verify.py` checks symbolically that
\[
E'=-LE,\quad r'=rB,\quad y'=-yA,
\]
\[
A'=rB+yA,\quad B'=-(rB+yA),\quad A+B=\kappa+D.
\]
It also verifies the initial identities
\[
E(0)=d(\kappa+D)-\kappa c,
\]
\[
A(0)=1-u-c-d,\qquad B(0)=c.
\]

The global step is not delegated to computation. It uses the sign of the derivative at a hypothetical zero and the constant sum \(A+B=\kappa+D>0\). Exact endpoint matching is essential because it supplies \(B(s)=u+v-d>0\) and \(x(s)=u>0\).

Limits: no numerical endpoint solve is certified; no optimality statement is checked; no finite-chain convergence theorem is assumed or proved.
