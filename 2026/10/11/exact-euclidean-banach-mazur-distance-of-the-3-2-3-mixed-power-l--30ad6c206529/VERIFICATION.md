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
The proof is global and analytic. Coordinate-sign averaging reduces arbitrary ellipses to diagonal candidates without increasing distortion. On the unit sphere the squared quadratic comparison is exactly
\[
F_r(t)=r t^{4/3}+(1-t)^{2/3},\qquad 0\le t\le1.
\]
Its critical-point equation is
\[
t(1-t)=\frac1{8r^3}.
\]
Thus there are no omitted interior critical points: below \(r=2^{-1/3}\) there are none, and above it there are exactly two, \(u\) and \(1-u\).

At critical points,
\[
F_r(u)=\frac{2-u}{2(1-u)^{1/3}},
\qquad
F_r(1-u)=\frac{1+u}{2u^{1/3}}.
\]
The optimum occurs when the lower critical value meets the endpoint value \(r\). This gives \(u^{1/3}(2-u)=1\), hence \(u=z^3\) with \(z^3+z^2+z-1=0\). The distortion decreases before this transition and increases after it, as shown by the explicit derivatives in RESULT.md.

For the numerical consistency check,
\[
z=0.54368901269207636157\ldots,\quad
r_*=0.97495070568547563567\ldots,
\]
and
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=1.09486791757088648907\ldots .
\]
These decimals are not used as proof.

The elimination identity
\[
W^3+76W^2+4080W-5488=0,\qquad
W=d_{\mathrm{BM}}(X,\ell_2^2)^6,
\]
is a consequence of the displayed cubic relation for \(z\). No finite enumeration, timeout, or external certificate is used.
