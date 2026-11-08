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

The graph is exactly GP(6,2) with 12 vertices, 18 edges and the higher-independence predicate requiring every induced connected component to have <=r vertices. Independently enumerated all 4096 subsets with component BFS for r=1,2,3, obtaining augmented face totals 171,810,1469. Constructed and independently topologically sorted the greedy nonempty-face Hasse matchings: pairs 84,401,721 and checked directed incidences 462,3180,6528 with no directed cycles; the critical-cell distributions are (0:1,2:1), (0:1,3:4,4:2), (0:1,3:1,4:8,5:16). Independently performed signed gradient-path integral reduction, obtaining d4(r2)=[[-1,-1],[0,0],[0,0],[0,0]], d4(r3)=[-1,1,0,0,0,1,0,-1], and the 8×16 d5(r3) with specified 7×7 determinant +1 and d4*d5=0. Primitive cell cancellations are homotopy-valid because remaining attaching maps lie in the Hurewicz dimensions of wedges of spheres; yields S2, wedge3S3∨S4, wedge9S5. Inclusion maps are null because the sources have homotopy dimensions 2 and 4 and the targets are 2- and 4-connected respectively. No unproved general generalized-Petersen formula is asserted.

## originality

PASS

Checked actual theorems and their implications, original sources and relevant published exact results, including already-known special cases; none of those inspected entails the full target claim, subject to the explicit best-of-knowledge residual risks. This does not infer novelty from a failed search.

## value

PASS

The Dürer graph is a natural small cubic polyhedral generalized Petersen graph. Its r=2 mixed-dimensional wedge, r=3 nine S5 and null inclusion maps are exact structural topological facts that differ from known Petersen and simple family outcomes. The integral signed-attaching computation is substantive rather than a routine Euler table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
