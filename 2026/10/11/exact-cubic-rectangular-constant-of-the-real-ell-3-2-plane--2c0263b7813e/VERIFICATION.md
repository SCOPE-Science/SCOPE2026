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
The exact reduced objective is
\[
R(u,h)=\frac{u^2(1+u)+h^3(1+u^2)}{(u+h)^3+u^2(h-1)^3},
\qquad u,h\ge1.
\]
The numerator resultant of its two first derivatives is
\[
4u^{13}(u+1)^4Q(u)P(u),
\]
with \(Q(u)>0\) for \(u>0\) and \(P\) as displayed in `RESULT.md`. Exact Sturm counting gives one root of \(P\) above \(1\), isolated by
\[
16.1428<u_0<16.1429.
\]
The reduced linear subresultant is
\[
4A(u)h-B(u),
\]
and exact sign isolation gives
\[
4<h_0=\frac{B(u_0)}{4A(u_0)}<5.
\]
Substituting that rational function for \(h\) into both derivative numerators gives polynomials divisible by \(P\).

The bundled `verify.py` rederives the resultant and subresultant, performs the Sturm count and sign isolation, checks the two finite-boundary identities, and reports the numerical value only after the exact certificates pass.

No independent audit or independent validation has been performed.
