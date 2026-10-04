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

The proof was reconstructed from the exact invariant-subspace decomposition of the lexicographic-product adjacency matrix. The hypercube amplitude at Hamming distance \(r\) is
\[
(-i\sin t)^r(\cos t)^{d-r}.
\]
Comparing distances zero and one in the orthogonal-to-uniform sector forces an odd half-period; the uniform sector then reduces exactly to vertex return in the outer graph.

`verify_local_hypercube_pst.py` independently checks the explicit seven-vertex example. It computes the two characteristic polynomials by exact integer polynomial arithmetic, numerically diagonalizes the outer adjacency matrix using a standalone Jacobi routine, verifies return of the middle-vertex state at the required outer times for several hypercube dimensions, and verifies the corresponding hypercube antipodal phase. The replay prints `VERIFY_OK`.

The finite checker is supplementary. The general characterization is supplied by the exact decomposition and algebraic-integer proof in `RESULT.md`.

The direct lexicographic-product source, general state-transfer support theory, and later blow-up literature were compared. No independent audit has been performed.
