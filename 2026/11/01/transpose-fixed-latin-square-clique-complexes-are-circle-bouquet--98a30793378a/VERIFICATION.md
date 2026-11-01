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

# Reproduction and boundaries

Run `python verify_transpose.py` with Python 3.9 or later; no external packages are required. Expected final line: `VERIFY_OK`.

The checker independently computes original group-table graph adjacencies and compares every complete pair of row/column-swap vertex orbits to the structural orbit-graph formula for \(q=4,8,16,32\). It verifies all maximal faces by exhaustive clique enumeration and calculates full reduced mod-two simplicial homology for \(q=4,8\), with resulting ranks 3 and 21 in degree one and zero elsewhere. At those two orders it independently constructs respectively 10 and 176 exact elementary simplicial free-face collapse pairs to connected graphs with cycle ranks 3 and 21, proving the corresponding finite homotopy equivalences directly. The checker also verifies the exact vertex counts and proposed maximal-simplex counts in the tested cases.

No finite test proves the unlimited family. The unrestricted homotopy classification follows from the orbit-fixed triangulation, complete-cross-adjacency lemma, disjoint-interface decomposition, and homotopy pushout along nullhomotopic contractible components given in `RESULT.md`. Integer torsion-freeness follows from the actual wedge decomposition; mod-two test results alone would not justify it. Not covered: other coefficient representations, other automorphisms, or arbitrary abelian groups.
