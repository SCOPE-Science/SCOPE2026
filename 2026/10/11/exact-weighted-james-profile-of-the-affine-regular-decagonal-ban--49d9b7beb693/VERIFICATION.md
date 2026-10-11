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
The correctness certificate is `verify.py`.

It works over the exact quadratic field
\[
\mathbb Q(\sqrt5)
\]
using rational coefficient pairs and exact sign comparisons.

The ten norm supports are the two signs of
\[
u+v,\qquad
ru+v,\qquad
rv,\qquad
ru,\qquad
u+rv.
\]
After symmetry reduction,
\[
x=(-1+\alpha,-\alpha),
\qquad
0\le\alpha\le\frac12,
\]
and each of five representative edges is parameterized by
\[
y=p+\beta(q-p).
\]
Writing
\[
w=t\beta
\]
turns
\[
ty=tp+w(q-p)
\]
into an affine expression on the triangular-prism domain.

For each of the two \(t\)-intervals and every ordered pair of norm supports, the certificate maximizes the minimum of two affine excesses exactly. It enumerates the domain vertices and all intersections of the equality plane of the two excesses with pairs of active domain facets. This is exhaustive for a minimum of two affine functions on a polytope.

The certificate checks all one thousand edge-interval-support cases and verifies that the maximal simultaneous excess is nonpositive. It separately verifies the two sharp pairs and the algebraic conversion from the radius profile to the \(\lambda\)-profile.

No finite sampling is used as proof. No independent audit or independent validation has been performed.
