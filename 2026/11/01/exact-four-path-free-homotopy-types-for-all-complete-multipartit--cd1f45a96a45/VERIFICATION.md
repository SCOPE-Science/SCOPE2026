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

# Reproducibility and limits

Run `python check_pf4.py` with standard Python 3 (no third-party packages). The program enumerates all four-vertex subgraph paths, all faces of the corresponding path-free complexes, every matched Hasse arrow, and all mod-two simplicial boundary ranks for 14 tuples of part sizes. For each case it verifies the structural face criterion, absence of directed cycles in the matching, the predicted critical-two-cell count, Euler characteristic, and the complete mod-two Betti vector. Its printed final line reports 14 passing exhaustive finite examples.

The unbounded theorem is established by the universal face classification, the owner-pivot acyclic matching, simple connectivity of the full two-skeleton, and the Hurewicz/Whitehead homotopy equivalence argument in RESULT.md. The finite checker does not verify all positive part sizes or substitute for any of these proof steps. No external independent validation has been performed.
