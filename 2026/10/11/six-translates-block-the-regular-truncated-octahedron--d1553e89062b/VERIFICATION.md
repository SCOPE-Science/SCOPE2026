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

The checker reconstructs
\[
P=[-1,1]^3\cap\left\{\lVert x\rVert_1\le\frac32\right\}
\]
from exact rational vertices.

It verifies that the six normalized centers
\[
z_1,\ldots,z_6
\]
all belong to \(\partial P\). For every distinct pair it verifies
\[
z_i-z_j\notin\operatorname{int}P,
\]
which is exactly the pairwise nonoverlap condition after the actual translation vectors are doubled.

The six coordinate facets and eight sign facets are reconstructed from their defining equalities. Exact edge-length tests show that the former have four equal edges and the latter six equal edges, each with squared length \(1/2\).

Every facet is triangulated from its centroid. A triangle is accepted only when one center makes all four defining inequalities for membership in a translated \(\operatorname{int}P\) strict at all three vertices. Otherwise the triangle is divided into four midpoint triangles. The deterministic recursion terminates with \(438\) terminal triangles at maximum depth \(3\).

For each accepted triangle, convexity upgrades the three strict vertex memberships to containment of the entire triangle. The least exact slack among every certified triangle vertex and every defining inequality is
\[
\frac1{16}.
\]
Thus the coverage certificate has positive rational clearance.

The checker uses no random sampling or floating-point comparison in the scientific tests. The universal blocking implication is supplied by the standard centrally symmetric boundary-cover lemma; the finite code verifies its hypotheses for this body and these six vectors.

No lower bound on the blocking number is verified or claimed.
