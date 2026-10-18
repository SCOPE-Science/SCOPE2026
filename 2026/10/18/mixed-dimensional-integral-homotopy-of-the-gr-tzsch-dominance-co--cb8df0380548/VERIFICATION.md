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

# Verification and reproducibility

Reconstruct all files in `evidence/` preserving their given relative paths. Execute `python3 evidence/verify_morse.py` and `python3 evidence/verify_incidence.py` from any working directory. Each uses only the Python standard library. Both emit `VERIFY_OK`, while the second also emits `VERIFY_PRIME3_OK`.

The Morse verifier reconstructs the 11-vertex 20-edge graph from the explicit Mycielski definition, checks every one of the 1,435 faces, the fixed 716 augmented pairs, their 715 nonempty-pair restriction, every reversed Hasse incidence and the full 1,434-vertex acyclicity order, then computes both exact integral boundary coefficients in the 1-by-2 Morse chain matrix. The second code constructs the graph using a separate adjacency-matrix implementation, finds all 91 minimal dominating sets as a complete search over subset sizes, generates the face complex from their complementary facets, and performs independent mod-two and mod-three rank computations on the original simplicial chain groups.

The precise finite result is \(\mathcal D(\mu(C_5))\simeq S^5\vee S^6\vee S^6\). Finite-field ranks alone cannot establish this integral homotopy type; the complete acyclic matching together with signed integer cellular boundary and the degree classification \(\pi_5(S^5)\cong\mathbb Z\) provides the proof. No claims are made for larger Mycielski graphs. This is not an independent mathematical audit.
