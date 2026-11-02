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

# Verification notes
The theorem has a self-contained analytic proof based on exact cut counting. Its decisive identity expresses the difference between the two sides of the universal cut inequality as a sum of squared row and column imbalance terms. The equality conditions and the optimal image-distance profile are proved analytically for every integer \(n\ge3\).

Run `python3 check.py` from the same directory as the supplied file. It needs only Python's standard library and reports `CHECK_OK` with three counts: `distance_pairs=8755`, `cut_certificates=80088`, and `embedding_pairs=1086`. The checker reconstructs the graph adjacency relation and breadth-first distances, exhausts all cuts for \(n=3,4\), tests deterministic pseudorandom cuts through \(n=12\), and computes exact rational permutation-cut embeddings through \(n=6\). The calculations are finite corroboration; they do not certify the infinite range independently.

The result concerns equal square boards and unit graph-edge lengths only. Historical literature comparisons include limited-access older material; mathematical priority remains open to independent investigation. No independent audit or external validation is represented by this document.
