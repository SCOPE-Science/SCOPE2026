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

For the rigidity direction, equal transformed facet areas are equivalent to
\[
x_j^TQx_j=c
\]
for all design nodes, where
\[
Q=A^{-1}A^{-T}.
\]
Then
\[
q(u)=u^TQu-c
\]
has degree two. If the design has strength at least four,
\[
\int_{S^2}q(u)^2\,d\sigma(u)
=
\frac1N\sum_jq(x_j)^2
=
0.
\]
Since the integrand is continuous and nonnegative,
\[
q\equiv0
\]
on \(S^2\), so \(Q\) is scalar and \(A\) is a similarity.

For sharpness, the packaged checker verifies exactly that the three displayed positive nodes form an orthonormal basis and therefore that their antipodal union is a spherical \(3\)-design. It also verifies
\[
A_0^{-1}A_0^{-T}
=
\operatorname{diag}(5/4,5/4,1/2)
\]
and
\[
x^TA_0^{-1}A_0^{-T}x=1
\]
for every one of the six nodes, while the matrix is not scalar.

The computation only replays the explicit counterexample. The all-design rigidity theorem is the degree-four exactness argument above.
