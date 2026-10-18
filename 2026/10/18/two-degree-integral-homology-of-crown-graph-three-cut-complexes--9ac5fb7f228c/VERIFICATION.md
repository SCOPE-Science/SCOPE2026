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

# Computational verification and mathematical limits

Execute `python3 artifacts/verify.py` from the directory containing this document and its `artifacts/` subdirectory. The program uses only Python 3's standard library. Expected final output: `VERIFY_OK cases=5`.

The verifier constructs the graph adjacency relation from the stated definition, enumerates disconnected triples, and forms the dual by testing avoidance of every disconnected triple. A separate capacity-and-index-condition generator constructs the multiple chessboard complex. For \(n=5,6,7\) it verifies equality of all simplices after adding precisely \(n\) matched-pair edges and checks the exact face vector. The reduced mod-two homology of the chessboard part and dual are independently obtained by bit-column elimination in the augmented simplicial chain complex.

For \(n=5,6\) it constructs the **ordinary cut complex directly** by checking whether the complement of each subset contains a disconnected triple, then calculates the reduced mod-two homology in all degrees. These computations give respectively \((\widetilde\beta_4,\widetilde\beta_6)=(1,5)\) and \((\widetilde\beta_6,\widetilde\beta_8)=(19,6)\), agreeing with the theorem.

Finite tests do not establish the infinite-range theorem and mod-two ranks cannot certify torsion-freeness. The all-parameter argument is mathematical: precise face classification, the published multiple chessboard shellability theorem, integral Euler characteristic, elementary homotopy of edge attachments, and integral combinatorial Alexander duality. The original cut complex's homotopy wedge decomposition, if any, is unproved.
