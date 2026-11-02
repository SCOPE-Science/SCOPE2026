---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For the explicitly fixed 18-vertex LCF Pappus cubic graph, independent perfect-matching enumeration found exactly 42 facets and 15,819 nonempty subsets, excluding the 19,548 ordinary nonextendible matching faces. A custom independent toggle Morse matching found 7,905 pairs and critical counts one 0-cell, one 2-cell, six 3-cells and one 4-cell; topological sorting all 78,921 directed incidences certified acyclicity. Independent signed integral Morse differential reconstructed d3=(0,-1,-1,1,0,0) and d4=0. The primitive unit d3 removes the 2-cell and one 3-cell. The resulting 3-skeleton is five 3-spheres, so pi3~=H3=Z^5 by Hurewicz; zero d4 therefore forces null-attached final 4-cell. Hence precisely 5 S^3 vee S^4, not only mod2 Betti ranks. This is an exhaustive finite proof for the specified LCF graph, not a graph-family theorem.

## originality

PASS

Closest published calculation concerns the ordinary Pappus matching complex, with 35,367 rather than 15,819 faces and wedge of 40 S^5; it expressly uses all endpoint-disjoint edge sets and does not imply the perfect-matching extendability subcomplex topology. Primary Bayer/Jelic Milutinovic/Vega paper covers perfect matching complexes of planar honeycomb regions; the Pappus symmetric cubic incidence graph is different. A distinct Heawood perfect-matching result does not imply the Pappus complex. No exact mixed 3-/4-sphere Pappus-extendability result found; priority remains best-of-knowledge and limited by possible unindexed computations.

## value

PASS

The Pappus graph is a distinguished cubic Levi graph, and extendible matchings define a canonical pure high-dimensional complex. Its integral mixed sphere-wedge differs dramatically from the already published ordinary matching complex, making this complete finite invariant useful to comparisons of matching-complex functors. The 495 minimal extension obstructions motivate the face predicate and show the difference is structural.

The dated certificate retains the supplied scientific assessment, sources and limitations.
