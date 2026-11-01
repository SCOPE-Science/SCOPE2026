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

# Reproducible finite checks

Run `python verify.py` from the directory containing this file; no third-party packages are required. Exact finite-field arithmetic is represented by Python integers and bitwise XOR.

The script constructs the adjacency of the edge-deleted hypercube independently, computes matrix powers and Gaussian-elimination ranks over \(\mathbb F_2\) for dimensions two through eight, and checks exact periodic fixed-space dimensions, nilpotent-power ranks and identities. It then exhaustively iterates every state in dimensions two through four over \(\mathbb F_2\), and dimensions two and three over \(\mathbb F_4\), independently discovering the transient time and primitive period of each state. Expected populations are computed from the theorem. These 98 algebraic check groups and 131,600 exhaustive finite-field initial-state checks all passed. The recorded output is `verification_output.txt`, ending in `EDGE_DELETED_HYPERCUBE_ALL_CHECKS_PASSED`.

These are finite computational cross-checks, not an exhaustive test of all dimensions or a proof of novelty. The independent audit channel has not been performed. The infinite-family conclusion relies on the symbolic proof in `RESULT.md`.
