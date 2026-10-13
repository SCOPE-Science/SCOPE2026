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
The two density equivalents are
\[
f_C(x)
\sim
q(q+1)2^{-q}\beta^q\frac{\Gamma(2q)}{\Gamma(q)}x^{-q-1}
\]
and
\[
f_S(x)
\sim
q\beta^q\Gamma(q+2)x^{-q-1}.
\]
Integrating them gives the survival constants and
\[
R(q)=\frac{2^{-q}\Gamma(2q)}{q\Gamma(q)^2}.
\]

For \(0<q\le1\), the beta-integral bound gives \(R(q)<1\). For \(q\ge1\),
\[
\frac{d}{dq}\log R(q)
=
\log2-
\int_0^\infty\frac{e^{-qt}}{1+e^{t/2}}\,dt
>
0.
\]
Since \(R(2)=3/4\) and \(R(3)=5/4\), there is exactly one crossing. The bundled checker solves it numerically and evaluates exact mixture integrals to verify the predicted tail constants and hazard normalization.

Finite computation is not used to prove the asymptotic theorem.
