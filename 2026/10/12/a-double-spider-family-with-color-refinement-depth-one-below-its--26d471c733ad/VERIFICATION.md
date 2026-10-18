---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a≥1, centers x,y have arm lengths (a,a) and (a,a+1). The graph has n=4a+3 vertices and diameter 2a+2. Starting from uniform colors, the rooted depth-r universal-cover representation (on a tree, the actual truncated rooted tree) shows x and y indistinguishable through depth a and separated at round a+1 by the extra y-arm edge. By that round D_j have unique colors while the three equal-length positions A_i,B_i,C_i remain a triple. At each next round, the split of the predecessor class forces C_{k+1} to separate from A_{k+1},B_{k+1}; a one-step neighborhood argument prevents earlier splits for more distant triples. At round 2a+1 the remaining A_i,B_i pairs are automorphism orbits and all others singletons, hence stable; at 2a last triple intact. Independently coded color refinement for every 1≤a≤40 and checked all 860 asserted middle/subsequent partitions, and all depths. This finite census corroborates the uniform proof, not replaces it.

## originality

PASS

Krebs–Verbitsky gives the covering-tree/color-iteration correspondence and near-linear general graphs, while Kiefer–McKay gives sharp n−1 iteration numbers on general graphs. Neither inspected relevant text establishes this explicit double-spider two-stage propagation law or unbounded stabilization-minus-radius difference on trees; searches for double spiders with these parameters did not find an exact equivalent. Best-of-knowledge with possible unindexed folklore tree example.

## value

PASS

The family isolates a nontrivial two-way information propagation mechanism in the simplest trees with two adjacent branching centers. Stabilization takes diameter−1 rounds despite radius only a+1; the gap a grows unbounded. This clean infinite family sharpens intuition about color refinement on acyclic graphs and distinguishes single-tree depth from general graph-pair bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
