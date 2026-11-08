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

PASS: Reconstructed GP(10,3) independently on twenty graph vertices and computed every BFS distance; the 190 unordered pairs distribute by distance 1..5 as 30,60,60,30,10. Hence the inclusive graph-vertex Rips complex changes only at integer thresholds. At r=2 independently generated all 260 cliques and read the actual 140-step r2_steps.json: all 120 pair deletions are genuine free-face/coface collapses in the entire active complex, all 20 critical deletions are maximal, and the full 260-node reversed Hasse graph topologically sorts without cycle, leaving one critical vertex and 19 critical 2-cells. At r=3 regenerated all 3,200 cliques and checked the entire actual 1,601-step r3_steps.json: 1,599 legal free-face pair deletions, only a critical vertex and one critical 3-cell, no leftovers, and complete Hasse acyclicity over 3,200 cells. Thus K₂≃wedge^19 S² and K₃≃S³ integrally by elementary collapses and Forman, not by mod-two ranks. K₁ is a connected triangle-free 20-vertex/30-edge graph with cycle rank 11; r<1 is 20 points; at r=4 the ten distance-five pairs are disjoint, so the flag complex is the join of ten S⁰= S⁹; r≥5 is a full simplex. Adjacent stages have homology in distinct degrees, so all reduced persistence groups are free, all consecutive maps vanish, and the claimed half-open integer barcode follows.

## originality

PASS

PASS best-of-knowledge: broad graph-power Rips results require higher girth or classify other graph families; these hypotheses fail for Desargues girth six. A published exact Desargues scale-three Čech nerve is a different complex with different face vector and homotopy. The complete intrinsic graph-vertex Rips filtration and integral persistence are not covered by inspected source theorems.

## value

PASS

PASS: Complete integral homotopy persistence on the canonical Desargues graph reveals an unusual natural progression from 19 two-spheres to a 3-sphere to a 9-sphere at consecutive thresholds. The full barcode and exact collapse certificates resolve a meaningful graph-metric topological invariant at the first low-girth regime where high-girth graph-power theorems fail. It is a finite complete classification, not arbitrary test sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
