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
The universal contradiction is analytic.

Let
\[
q_i=\frac{p_iM}{a_i},
\qquad
M=n+\sum_i a_i.
\]
Then condition (5) gives \(0<q_i<1\). Using
\[
R_i\le\frac{1-q_i}{2}
\]
and
\[
c_i<p_i,
\]
one obtains
\[
c_iR_i
<
\frac{a_i}{2M}q_i(1-q_i)
\le
\frac{a_i}{8M}.
\]
Summation gives
\[
\sum_i c_iR_i<\frac18,
\]
while condition (6) requires
\[
\sum_i c_iR_i>1+\sum_i b_i>1.
\]

The bundled checker verifies the algebraic identity, the quadratic maximum, and exact rational sanity checks. The finite checks are not used as proof of the universal claim.
