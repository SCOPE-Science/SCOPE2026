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

Execute `python3 verify.py` with Python 3.9 or later in the same directory as this file. The program needs only the Python standard library; it neither contacts an external service nor depends on a prior calculation. The reference run is recorded in `verification_output.txt`.

The executable independently reconstructs both Cayley/rook adjacency masks, checks all degree and common-neighbor conditions, distinguishes their local graphs, and tests every one of the \(65,536\) vertex subsets by the maximum-induced-degree test and a separately implemented induced-component exploration. It counts all faces and maximal faces, rebuilds the exact pivot matchings, checks every covering pair and complete directed Hasse graph, and verifies that Kahn's algorithm visits every nonempty face. A separate simplicial chain-rank algorithm computes mod-two boundary ranks as a check on the critical-cell count.

The checks establish a finite acyclic matching certificate with one critical zero-cell and only critical three-cells, so Forman's theorem proves the full *integral* homotopy equivalences. The mod-two calculation alone would not prove them. The certificate is specific to the two stated graphs. No independent review or complete global publication-priority certificate is claimed.
