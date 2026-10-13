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

The proof is analytic. Starting from
\[
F_\infty^{-1}(u)=\frac{-\log(1-u)}{u},
\]
the substitution \(u=1-e^{-E}\) gives the exact transformed-exponential representation.

For survival \(q\in(0,1)\),
\[
x(q)=\frac{-\log q}{1-q},
\qquad
h(x(q))=\frac{(1-q)^2}{1-q+q\log q}.
\]
Differentiation reduces strict DFR to
\[
L-2+e^{-L}(L+2)>0,\qquad L>0,
\]
whose derivative is \(1-e^{-L}(L+1)>0\).

For every integer \(m\ge1\),
\[
\mathbb E Z_\infty^m
=
\int_0^\infty\frac{t^m e^{-t}}{(1-e^{-t})^m}\,dt
=
m!\sum_{n\ge1}\binom{m+n-2}{m-1}n^{-(m+1)}.
\]
The bundled `verify.py` independently checks the hazard formula numerically, strict decrease on a deterministic grid, the endpoint behavior, and the first three moments by numerical quadrature and partial series.

Successful output ends with:
`VERIFY_OK mean=1.644934066848226 variance=0.584060049418607 hazard_endpoints=(2,1)`.

Finite numerical checks are regression tests only and do not establish the all-parameter theorem.
