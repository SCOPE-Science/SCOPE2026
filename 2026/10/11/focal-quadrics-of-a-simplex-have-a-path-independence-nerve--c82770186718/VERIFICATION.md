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
M(x)=D-xx^{\mathsf T},
\qquad
D=\operatorname{diag}(d_1,\ldots,d_n),
\qquad
d_1>\cdots>d_n,
\]
Cauchy interlacing gives
\[
d_1\ge\mu_1\ge d_2\ge\mu_2\ge\cdots\ge d_n\ge\mu_n.
\]
A repeated \(d_k\) therefore occupies
\[
\mu_{k-1}=\mu_k=d_k,
\]
which excludes adjacent focal indices.

For any nonconsecutive set \(S\), the proof explicitly chooses an interlacing target spectrum with
\[
\mu_{k-1}=\mu_k=d_k
\]
exactly for \(k\in S\). With
\[
p_D(t)=\prod_i(t-d_i),
\qquad
p_\mu(t)=\prod_i(t-\mu_i),
\]
the quantities
\[
x_i^2=\frac{p_\mu(d_i)}{p_D'(d_i)}
\]
are nonnegative by sign interlacing. The partial-fraction identity
\[
\frac{p_\mu(t)}{p_D(t)}
=
1+\sum_i\frac{x_i^2}{t-d_i}
\]
and the determinant lemma give
\[
\det(tI-(D-xx^{\mathsf T}))=p_\mu(t).
\]
This proves the all-dimensional realization.

The bundled checker exactly verifies the construction for every independent index set in dimensions \(2\) through \(10\), the path independent-set counts through dimension \(14\), and the source's four-dimensional example:
\[
x_1^2=\frac{36}{7},
\qquad
x_3^2=\frac67,
\qquad
\det(tI-M(x))=(t-6)^2(t-1)^2.
\]
Since
\[
\|x\|^2=6,
\]
the Jacobian spectrum is
\[
\{3,3,-2,-2\}.
\]

The finite checker is supplementary; finite enumeration is not used as proof of the all-dimensional statement.

The verification does not address coincident semiaxes or the topology of higher focal intersections.
