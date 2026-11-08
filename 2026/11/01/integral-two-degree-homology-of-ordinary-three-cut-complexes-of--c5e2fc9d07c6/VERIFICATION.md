---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed Alexander dual K: subsets with every three vertices connected in Qd. Because the cube is bipartite and triangle-free, its triangles are unique-center length-two paths and its tetrahedra are exactly coordinate squares; no five-face can exist (three same-parity vertices). Each square has two free elementary collapse pairs, deleting one square tetrahedron and one diagonal so K collapses onto the cubical two-skeleton plus all Hamming-distance-at-least-three edges. The cubical two-skeleton is simply connected since higher-dimensional cells do not change π1; Euler characteristic gives μ=2^(d−3)(d²−5d+8)−1 free two-spheres. Long edges add h=2^(d−1)Σ_{j=3}^d C(d,j) loops, and the resulting two-complex is homotopy equivalent to the stated wedge. Integral UCT and combinatorial Alexander duality yield H_(2^d−5)=Z^μ, H_(2^d−4)=Z^h, all else zero; pure non-shellability follows from lower-degree homology. Independent enumeration of all connected triples and squares gives (d3:24 triangles,6 squares,μ1,h4) and (d4:96,24,μ7,h40), not a substitute for the uniform proof.

## originality

PASS

Best-of-knowledge PASS for the all-d ordinary cut homology and explicit dual collapse beyond the known d=3 instance. The exact Q3 prior result is the theorem’s base case; its full RESULT.md limits itself to Q3. The high-girth cut theorem cannot cover Qd because it has many four-cycles; the foundational complete-codimension-one-skeleton theorem fails because each coordinate square creates a nonface of the required size. A hypercube Lovász neighborhood complex has the same μ formula but distinct common-neighbor faces, not the cut complex or long-edge h. The Q4 total-cut calculation uses complements of independent (not all disconnected) triples. None supplies the d≥4 two-degree formula.

## value

PASS

All binary cubes are a canonical infinite family, and the theorem solves complete integral homology for every dimension while identifying an elementary geometric dual model, explicit two distinct positive degrees and a uniform non-shellability obstruction. The square-plus-Hamming-chords decomposition is structural rather than a table extrapolation; the known Q3 case is a natural boundary, not the whole contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
