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
Let
\[
a=\alpha/2
\]
and
\[
C=(2\sigma)^q\Gamma(a+q)/\Gamma(a).
\]
The corrected survival is
\[
S_Z(t)
=
1-G(t/(2\sigma);a,1)
+
Ct^{-q}G(t/(2\sigma);a+q,1).
\]

Two independent derivations were checked:

1. direct complementation of Proposition 2.4;
2. conditioning on \(X\) in the quotient representation \(Z=X/Y\).

The bundled checker verifies
\[
1-F_Z(t)=S_Z(t)
\]
and numerical differentiation of the CDF against the published density.

For \(\mathrm{SCHI}(1,3,1)\) at \(t=8\), it obtains
\[
S_Z(8)=0.3624233453475855\ldots,
\]
while the printed formula gives
\[
-0.270399933969123\ldots.
\]

It also verifies
\[
t^qS_Z(t)/C\to1
\]
and
\[
t\,h_Z(t)/q\to1.
\]
