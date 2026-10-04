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
The proof depends on the published identity
\[
g
=
1+
\frac{1}{2}
\left(
\sum_i\binom{d_i+k}{k+1}
-
n
-
1
\right)e
\]
for a one-dimensional Fano scheme.

Setting
\[
q=k+1,
\qquad
R_i=\binom{d_i+k}{k},
\]
the expected-dimension equation
\[
q(n-k)=1+\sum_iR_i
\]
and
\[
\binom{d_i+k}{k+1}
=
\frac{d_i}{q}R_i
\]
give
\[
qB
=
\sum_i(d_i-1)R_i-(q^2+1).
\]

The target \(B\ge2\) is therefore equivalent to
\[
\sum_i(d_i-1)R_i\ge(q+1)^2.
\]
The proof checks this exactly in the three possible ranges for the number of defining equations, with equality only for three quadrics and \(q=2\).

The bundled checker exhausts a finite parameter box, verifies every admissible instance in that box, and confirms the unique equality pattern. This finite replay is regression evidence only.

Limits: general complete intersections over \(\mathbb C\), \(n\ge4\), \(k\ge1\), and expected dimension exactly one.
