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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 standard library. It independently reconstructs all 7342 nonempty simplices from the degree-at-most-two condition, produces 3663 disjoint discrete-Morse pairs from the listed fixed edge order, and verifies that the directed Hasse graph of 37728 incidences is acyclic by a complete topological sort. Its critical-cell vector is one vertex plus fifteen five-simplices.

It then calculates the exact selected-edge-orbit alternating sum for all 1152 automorphisms and compares with the proposed character. As an independent combinatorial route, oriented fixed-simplex Lefschetz traces are evaluated for the 25 nonswap type pairs and five swap types, including the augmented empty-face correction. The output contains `K44_TWO_MATCHING_EQUIVARIANT_VERIFIED` on success. These calculations are exhaustive because the graph and action are finite and every possible mask or group permutation is included.

Limits: No integral automorphism-lattice decomposition, equivariant topological wedge splitting, or generalized all-parameter formula is claimed. No independent mathematical audit has been performed.
