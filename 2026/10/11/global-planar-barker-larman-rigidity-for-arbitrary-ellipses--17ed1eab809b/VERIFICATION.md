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

For
\[
E=c+Q^{1/2}B_2
\]
and
\[
H_u=\{x:u\cdot x=r\},
\]
pulling the line back through \(Q^{1/2}\) gives a disk chord at signed distance
\[
\frac{r-u\cdot c}{\sqrt{u^{\mathsf T}Qu}}.
\]
In two dimensions the affine stretch along that chord direction has squared factor
\[
\frac{\det Q}{u^{\mathsf T}Qu}.
\]
Multiplication yields
\[
\frac{L_E(u)^2}{4}
=
\det(Q)\,
\frac{u^{\mathsf T}Qu-(r-u\cdot c)^2}
{(u^{\mathsf T}Qu)^2}.
\]

Antipodal subtraction gives the exact odd identity
\[
\frac{L_E(u)^2-L_E(-u)^2}{16r}
=
\det(Q)\frac{c\cdot u}{(u^{\mathsf T}Qu)^2}.
\]
The proof then uses only unique factorization in
\[
\mathbb R[x_1,x_2]
\]
and the fact that a positive-definite binary quadratic has no real linear factor.

`verify.py` checks the affine formula directly by solving the line--ellipse quadratic for several deterministic nonconcentric ellipses and directions. It separately checks the odd identity. Those finite tests are diagnostic; they do not replace the polynomial proof.

The only unresolved verification issue is bibliographic rather than mathematical: the full 2001 Barker--Larman article was not obtained during bounded lawful-access checks, so a differently phrased historical conic special case cannot be excluded absolutely.
