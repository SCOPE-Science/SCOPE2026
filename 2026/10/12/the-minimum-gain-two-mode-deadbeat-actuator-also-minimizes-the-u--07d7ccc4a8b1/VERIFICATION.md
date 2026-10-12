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
The universal theorem is analytic. The standalone checker replays exact identities and the rational equality example.

For
\[
a=\frac45,
\qquad
d=\frac35,
\qquad
b=\left(\frac45,\frac35\right)^{\mathsf T},
\qquad
k=(4,-3)^{\mathsf T},
\]
it verifies
\[
A-bk^{\mathsf T}
=
\frac{12}{5}
\begin{pmatrix}
-1&1\\
-1&1
\end{pmatrix}
\]
and
\[
(A-bk^{\mathsf T})^2=0.
\]
Because this matrix has rank one, its spectral norm equals its Frobenius norm, which the exact entries give as
\[
\frac{24}{5}.
\]
The feedback norm is exactly
\[
5,
\]
matching
\[
\frac{a^2+d^2}{a-d}.
\]

The checker also verifies the trace/determinant pole equations and the closed-loop norm identity on several rational choices of \(a,d,b_1^2,b_2^2\). These finite checks are corroborative only; the all-parameter minimizers follow from the two sharp inequalities in `RESULT.md`.
