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
# Reproducible calculation and limits

Run `python3 artifacts/verify.py` with SymPy and NumPy available. The script constructs graph adjacency matrices from edge lists and spectral projectors directly from their exact eigenvalues, and independently computes the spectral projectors of each blow-up adjacency matrix. It verifies all entries of the Schur-squared average against the claimed explicit matrix formula, the rank classification and complete eigenvalue multisets for 14 small exact cases. They include an edgeless one-vertex base, an edge, a path on three vertices, a triangle, a four-cycle, a four-vertex star, and a disconnected edge-plus-isolated-vertex base, each with fibre sizes two and three.

The independent floating-point tests cover 54 more combinations of random undirected graphs on two through seven vertices and fibre sizes two through four. The maximal observed matrix difference between direct spectral calculation and the derived formula was about \(3\times10^{-15}\). The checker verifies the nontrivial boundary examples \(\operatorname{rank}\widehat M(B_2(P_3))=5\) on six vertices and \(\operatorname{rank}\widehat M(B_2(K_{1,3}))=7\) on eight vertices.

A passing replay prints `VERIFY_OK exact_matrices=14 numerical_matrices=54 P3_two_clone_rank=5/6 star_two_clone_rank=7/8` followed by the observed maximum difference. Exact tests establish only their finite cases, and numerical tests are not proofs. The unrestricted statement follows from the two-sector spectral decomposition and positivity argument given in the result. No mathematical software is required for that analytical proof.

Scientific limits: no generalization to varying fibre sizes, Laplacian Hamiltonians, instantaneous uniform mixing or nonuniform observation-time averages is claimed. The proof is a mathematical argument reviewed in the same-model channel; no independent audit or certification has been performed.
