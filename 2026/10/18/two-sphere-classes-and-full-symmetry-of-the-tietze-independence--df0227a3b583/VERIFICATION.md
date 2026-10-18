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

The standard-library program `verify.py` reconstructs the canonical graph, all 177 simplices, all 87 Morse pairings and the oriented 177-vertex Hasse digraph. It performs a full DAG topological sort and verifies that only one dimension-zero critical face and two dimension-two critical faces survive. It then derives each of the twelve graph automorphisms from permutations of the five Kneser labels, checks edge preservation, and verifies its signed simplicial Lefschetz number against the indicated rational character. No external services, precomputed logs, or unexamined files are needed.

Limitations: this is an exact finite verification of the specified twelve-vertex complex. Character equality is used only over \(\mathbb Q\). Independent external audit has not been performed.
