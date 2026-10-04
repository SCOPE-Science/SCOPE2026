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

For \(1<c<2\), every vertex has active-normal pattern
\[
s_i e_i,
\qquad
s_i e_i+s_j e_j+e_k,
\qquad
s_i e_i+s_j e_j-e_k.
\]
Choosing the unique tetrahedral direction with
\[
d_i=-s_i,
\qquad d_j=-s_j
\]
gives active dot products \(-1\), \(-1\), and \(-3\) in some order.

At \(c=2\), the second coordinate facet becomes active as well and has dot product \(-1\) with the same direction.

For \(2<c<3\), the active-normal pattern is
\[
s_i e_i,
\qquad s_j e_j,
\qquad s=(s_1,s_2,s_3),
\]
and the same rule gives dot products \(-1\), \(-1\), and either \(-1\) or \(-3\).

The packaged `verify.py` exhausts all coordinate choices and sign patterns for these three cases. It also checks the explicit endpoint illuminating sets and the discrete incompatibility structure used in the endpoint lower bounds.

The actual replay output was:

`VERIFY_OK cube-octahedron illumination phase profile`

The universal lower bound \(\mathfrak I(K)\ge4\) is proved analytically by convex separation. The endpoint lower bounds are likewise analytic. No finite sample is used to infer a statement for a continuum of parameters.
