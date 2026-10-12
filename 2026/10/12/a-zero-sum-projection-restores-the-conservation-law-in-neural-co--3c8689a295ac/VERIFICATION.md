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

Let
\[
\mathbf 1=(1,1,1)^\top
\]
and
\[
P=I-\frac13\mathbf 1\mathbf 1^\top.
\]
The bundled checker verifies with exact rational arithmetic that
\[
P^\top=P,\qquad
P^2=P,\qquad
\mathbf 1^\top P=0.
\]

For representative positive rational states and two distinct SIR parameter pairs, it reconstructs
\[
f_{\mathrm{true}}-f_{\mathrm{dist}}
\]
and checks that its three components sum to zero.

For representative arbitrary residual targets \(Y\) and exact zero-sum residuals \(r\), it also verifies the exact identity
\[
\|Y-r\|_2^2
=
\|PY-r\|_2^2+\|(I-P)Y\|_2^2.
\]
This certifies the finite algebraic replay of the projection argument.

The general conservation law and non-worsening theorem are symbolic consequences of the published SIR and hybrid equations; the checker is not used as an empirical substitute for proof.
