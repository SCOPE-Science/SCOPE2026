---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Constructed the four exact adjacency models from the formulas and verified the supplied root-to-vertex automorphisms and every spanning path witness against these graphs. Positives only require one root because the automorphisms carry the vertex, its opposite class, and each path together. Independently enumerated simple paths recursively, without the submitted subset DP or transitivity reduction, for every starting vertex in the full graph and every deletion and admissible endpoint pair. In H,M,P,D order this checked 98,128,162,200 ordered full cases, all positive, and 294,448,648,900 punctured pairs, with 0,16,0,0 failures. The 16 failures give one per M deletion, precisely the unique original-graph distance-(3,3,4) pair by BFS. For deletion 0, its ends are 10,14. Each of 1,7,8 must use both remaining incident edges; the unused edges therefore have degrees one at the other ten vertices and two at 10,14 in the 15-edge induced graph. Enumerating seven-edge subsets finds six possible unused-edge sets; the residual components have sizes (5,10) or (6,9), three cases each. This corroborates the source obstruction, including its claim of exactly two components. Replay: python3 /workspace/branches/reproduce_discrete.py.

## originality

PASS

Credit prior ordinary laceability where established, the existing hyper-Hamilton-laceability concept, and the prior structural choice of these four graphs. The distinct claim supported here is the full endpoint-resolved one-vertex-deletion classification, particularly the unique distance-defined defect in Möbius–Kantor. Inspected results do not give that classification or imply it by restricting ordinary endpoints. Relevant unavailable full texts remain a limitation, not positive evidence of novelty.

## value

PASS

A natural complete finite classification on the four already distinguished cubic symmetric girth-six graphs. The result resolves a stronger extension property than ordinary Hamilton laceability and gives an intrinsic, unique, checkable witness explaining why the Möbius–Kantor case differs. The endpoint-level characterization provides useful data for comparing fault tolerance without relying on vertex labels or an unmotivated graph slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
