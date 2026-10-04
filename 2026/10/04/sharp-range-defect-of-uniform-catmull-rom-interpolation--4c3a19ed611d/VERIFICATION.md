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
`verify.py` performs exact rational polynomial algebra. It reconstructs the uniform cardinal Hermite segment and verifies the increment-basis coefficients
\[
q_0(t)=1+\sigma t(1-t)^2,
\]
\[
q_1(t)=t\left[\sigma+(1-\sigma)t(3-2t)\right],
\]
and
\[
q_2(t)=-\sigma t^2(1-t).
\]

It checks the factorization
\[
1-q_1(t)
=
(1-t)\left[1+(1-\sigma)t(1-2t)\right],
\]
the derivative identities locating the two continuous extrema, their exact value \(4/27\), the standard \(\sigma=1/2\) range endpoints, and the strictly increasing witness formula.

The replay is supplementary. The proof that \(q_1\) remains between zero and one and the optimization over the full monotone data cone are analytic arguments in RESULT.md, not finite sampling claims.
