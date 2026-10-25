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

# Reproduction of exact finite certificates

Run `python verify_dyck.py` from the same directory as `requirements.txt`. The checker constructs the standard 32-vertex cubic graph using the stated LCF sequence, performs exhaustive simple-cycle searches at lengths six and eight, and enumerates every disjoint cycle pair. The integer two-cell boundary and torus cycle chains are assembled from first principles.

The checker verifies every signed boundary composite and torus cycle, uses exact sparse arithmetic modulo \(101\) to show the second-boundary rank is at least \(928\), and chooses 104 square-coordinate rows independent modulo two. It then computes exact column Hermite normal forms and integer Smith normal forms. The full 186-torus coordinate matrix has Hermite form \(I_{104}\); the shortest 72-column matrix has 72 Smith units; the hexagon-involving 168-column matrix has Smith factors \(2,2\), with all other 102 invariant factors units.

All 192 automorphisms are enumerated using graph isomorphism checks. The two eight–eight orbit additions, of sizes six and twelve, each restore Hermite form \(I_{104}\).

These finite exact certificates prove the stated integral subgroup and quotient calculations when combined with the cubical deformation-retraction theorem. They do not prove any result about arbitrary graphs, longer cycles, more particles, or independent validation. Dependencies are provided separately; the code does not fetch papers or data.
