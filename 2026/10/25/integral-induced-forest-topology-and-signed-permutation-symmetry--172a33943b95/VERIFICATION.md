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

For Clebsch Cayley graph on F_2^4 with connection differences 1,2,4,8,15, every one of the 65536 vertex masks was independently tested for induced acyclicity. The 13839 augmented faces have f-vector (1,16,120,560,1780,3696,4376,2560,650,80). Independently reconstructed greedy vertex-pivot Morse matching has 6908 pairs, 19 critical 5-cells and four critical 6-cells; full topological ordering of 77632 oriented incidences proves acyclicity. The signed 19x4 Morse differential was independently reconstructed with exact integer recurrence; rows 0,1,3,4 give a unimodular maximal minor, so the high-dimensional CW cell pairs cancel integrally and F(C) is wedge of fifteen S^5. An independent enumeration of all 1920 graph automorphisms and fixed-face Lefschetz sums gives sign(sigma)*(number of fixed vertices-1) with zero mismatches and confirms the rational sign-twisted augmentation G-module, whose two translation-character orbits have dimensions 5 and 10. No general higher folded-cube claim is proved.

## originality

PASS

The vertex-subset induced-forest complex is not the ordinary independence complex or the graph-edge forest/matching complex. Taylan and Carnero Bravo introduce graph-devoid and induced-forest machinery and calculate other host families; their checked coverage does not imply this nonplanar (16,5,0,2) strongly regular case, or its full 1920-element rational symmetry character. Published Clebsch neighborhood-complex and other graph-complex results use different face predicates. This is a best-of-knowledge PASS limited by incomplete exhaustive bibliography.

## value

PASS

The 5-regular Clebsch graph is a canonical finite strongly regular graph. Determining exact integral homotopy and a nontrivial rational automorphism representation of its induced-forest complex answers natural graph-topological invariants with explicit reproducible finite witnesses, beyond recomputing a known independence-complex table. The rational-vs-integral symmetry distinction is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
