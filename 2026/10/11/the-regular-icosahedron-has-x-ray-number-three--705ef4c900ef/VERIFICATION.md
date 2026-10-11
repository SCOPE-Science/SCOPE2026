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

The checker works in exact arithmetic over \(\mathbb Q(\sqrt5)\). It constructs
\[
\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
It defines adjacency by squared Euclidean distance \(4\), yielding exactly thirty edges, and identifies triangular facets as three-vertex edge cliques. Exactly twenty facets are obtained and every vertex lies on five facets.

For each facet, the cross product of two edge vectors gives an exact normal, oriented outward by its support value on the origin-centered polytope. For each vertex, the checker tests the three coordinate axes and verifies that for at least one axis every incident outward facet normal has a nonzero component of the same sign. This is precisely the strict hemisphere condition needed to make the corresponding orthogonal great circle miss the vertex Gauss image.

All twelve vertices pass, and each is assigned to the axis on which its coordinate has absolute value \(\varphi\). Since the Gauss image of a face is contained in the Gauss image of each of its vertices, this finite facet-normal check proves coverage of every face, not merely the vertices.

The checker also enumerates all pairs of incident unit facet normals and verifies that the least cosine is
\[
\frac13.
\]
Because the three-dimensional almost-smooth threshold is \(1/2\), this independently confirms that the almost-smooth theorem does not supply the result.

The only non-computational lower-bound input is the standard theorem \(X(K)\ge d\) for every \(d\)-dimensional convex body, as stated in the cited X-ray-number paper.
