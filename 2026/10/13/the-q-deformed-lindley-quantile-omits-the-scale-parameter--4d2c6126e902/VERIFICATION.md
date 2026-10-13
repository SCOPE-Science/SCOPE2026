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
The true CDF uses
\[
A_\theta=1+(3-2q)\theta,
\]
whereas the printed quantile theorem uses
\[
A_0=1+(3-2q).
\]

Let
\[
b=(2-q)\theta.
\]
The theorem as printed inverts
\[
\widetilde F(x)
=
1-
\left(
1+\frac{bx}{A_0}
\right)
\{\exp_q(-\theta x)\}^{2-q}.
\]
Therefore, at the printed quantile,
\[
F(Q_{\rm pub}(u))-u
=
bQ_{\rm pub}(u)
\{\exp_q(-\theta Q_{\rm pub}(u))\}^{2-q}
\left(
\frac1{A_0}-\frac1{A_\theta}
\right).
\]

The corrected shifted Lambert–Tsallis derivation uses
\[
q'=\frac1{2-q},
\qquad
\kappa_\theta=1+(1-q')A_\theta,
\]
and
\[
\kappa_\theta
=
\frac{3-2q}{2-q}
\{1-(q-1)\theta\}.
\]

The bundled checker implements the real lower branch of \(W_{q'}\), verifies the exact residual identity, reproduces the four simulation-design median discrepancies, verifies the corrected medians, and tests the missing real-domain restriction on the unbounded branch.
