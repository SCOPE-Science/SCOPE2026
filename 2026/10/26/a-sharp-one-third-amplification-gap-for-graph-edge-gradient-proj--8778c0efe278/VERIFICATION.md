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

# Verification of the graph-gradient gap

The analytic argument in RESULT.md is the verification of the full universal theorem. It derives the exact deleted-edge electrical row formula, checks the discrete maximum principle and the two lower bounds for every nonbridge edge, minimizes the resulting elementary function, and analyzes equality using harmonicity. It separately establishes the bridge and cactus cases.

The included `verify_graphs.py` constructs incidence matrices and compares the exact prescribed gap and equality class against numerical Moore–Penrose projections for every connected unlabeled graph of three through seven vertices with at least one cycle in NetworkX's graph atlas. It reports the checked and equality counts by order; tolerance is \(10^{-7}\), and all examined graphs conform. Numerical agreement is finite evidence only and is not an infinite proof or an exact-arithmetic certificate.

The operator is measured in the edge-coordinate maximum norm under counting-measure Euclidean projection. No statement is made for positive conductance weights, parallel edges, infinite graphs, or alternative projection choices. Independent audit: not performed.
