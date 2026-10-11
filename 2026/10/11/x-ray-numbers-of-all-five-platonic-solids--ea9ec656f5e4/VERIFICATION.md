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

The proof uses the vertex Gauss-image criterion. A direction \(d\) X-rays a polytope vertex when all incident outward facet normals have dot products with \(d\) of one strict sign. Covering all vertices then covers every proper face because a face normal cone is contained in the normal cone of each of its vertices.

For the tetrahedron, the verifier checks the exact Gram relations
\[
v_i\cdot v_j=-1\quad(i\ne j)
\]
and verifies both the four upper-bound directions and the pairwise antipodal supporting-plane witnesses used with the weakly-neighbourly-antipodal lower bound.

For the cube, it verifies the four body-diagonal directions and exhausts all eight coordinate sign cells. Each direction sign cell X-rays exactly one antipodal vertex pair, certifying the four-line lower bound.

For the dodecahedron and icosahedron, `verify.py` implements \(\mathbb Q(\sqrt5)\) exactly as rational pairs. It checks the support values, facet cardinalities, vertex-facet incidences, edge counts, equality of all edge lengths, and every strict normal-dot-direction sign condition used in the proof. The reconstructed counts are
\[
(V,E,F)=(20,30,12)
\]
for the dodecahedron and
\[
(V,E,F)=(12,30,20)
\]
for the icosahedron.

For the octahedron, exact sign-vector facet normals verify that each coordinate axis X-rays its antipodal vertex pair.

No random sampling, floating-point geometry, or partial enumeration is used in the proof certificates. The lower bound \(X(K)\ge3\) and the weakly-neighbourly-antipodal proposition are external theorems cited in the result.
