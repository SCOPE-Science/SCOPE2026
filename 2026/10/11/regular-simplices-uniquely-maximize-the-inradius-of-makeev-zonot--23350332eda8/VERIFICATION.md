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
R_\Delta=[0,a_0]+\cdots+[0,a_d]
\]
with
\[
\sum_i a_i=0,
\]
the zonotope is centrally symmetric and
\[
h_{R_\Delta}(u)
=
\sum_i\max\{0,u\cdot a_i\}
=
\frac12\sum_i|u\cdot a_i|.
\]

Fix \(i\ne j\). Because the centered simplex has exactly one linear dependence among its \(d+1\) vertex vectors, the \(d-1\) vectors with indices different from \(i,j\) are independent. A unit normal \(u_{ij}\) to their span satisfies
\[
u_{ij}\cdot a_k=0
\qquad(k\ne i,j).
\]
The zero-sum relation then gives
\[
u_{ij}\cdot a_i=-u_{ij}\cdot a_j,
\]
so
\[
h_{R_\Delta}(u_{ij})
=
\frac12
\left|u_{ij}\cdot(a_i-a_j)\right|
\le
\frac12\lVert a_i-a_j\rVert.
\]
Taking the minimum over directions proves
\[
2r(R_\Delta)\le\lVert a_i-a_j\rVert
\]
for every edge.

For a regular unit-edge simplex, the published strip description places every strip boundary at distance \(1/2\) from the origin, proving the reverse bound.

`verify.py` constructs deterministic centered simplices, numerically computes the special normals \(u_{ij}\), and verifies the exact support identity within numerical tolerance. It separately checks the regular-simplex tight-frame identity and the support lower bound.

These finite calculations are diagnostic only. The quantified theorem is the exact linear-algebra argument above.
