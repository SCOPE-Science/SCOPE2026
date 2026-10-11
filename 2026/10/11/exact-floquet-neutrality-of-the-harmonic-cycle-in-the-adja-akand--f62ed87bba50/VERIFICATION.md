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

The final package includes `verify.py`, a dependency-free exact-arithmetic replay of the algebra used in the proof.

For each integer \(0\le n\le64\), it represents
\[
S_n(x)=\sum_{\ell=0}^{n}x^{2\ell}
\]
as a polynomial coefficient dictionary and checks exactly that
\[
(1-x^2)S_n(x)+x^{2n+2}-1=0.
\]
It then checks the polynomial identity equivalent to
\[
\dot R=-2xy\bigl(y+S_n(x)\bigr)R
\]
for the planar vector field. The output is `VERIFY_OK`.

The Floquet integral is verified analytically, not by quadrature:
\[
\oint xS_n(x)\,dx=0
\]
because it is an exact one-variable differential around a closed curve, and
\[
\int_0^{2\pi}\cos t\sin^2t\,dt=0
\]
by an elementary antiderivative. Therefore the normal characteristic exponent is exactly zero.

The finite \(n\le64\) code replay is only an implementation check. The proof for all \(n\ge0\) is the geometric-series identity in `RESULT.md`. No claim is made about higher-order nonlinear stability when the unit multiplier is present.
