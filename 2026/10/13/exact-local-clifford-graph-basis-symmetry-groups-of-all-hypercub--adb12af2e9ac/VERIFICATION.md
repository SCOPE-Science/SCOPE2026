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

The binary-symplectic verifier `verify_hypercube.py` requires only Python 3 standard-library modules. It builds the entire linear stabilizer-preservation system for \(1\le d\le5\) from adjacency data, solves it over \(\mathbb F_2\), checks the determinant condition on every qubit for all sixteen linear-space solutions, and verifies that all accepted matrices map the stabilizer generators into the same graph stabilizer. Its terminal line is `VERIFY_OK: exact GF2 linear solution spaces and all Clifford determinant and graph-space conditions for d=1..5`.

The independent complex-statevector verifier `verify_hypercube_statevectors.py` generates all six one-qubit symplectic matrices from the actual \(H\) and \(S\) unitary matrices, then checks every state of the graph basis for hypercubes with \(d=1,2,3\). Its terminal line is `STATEVECTOR_VERIFY_OK 1624 individual basis permutations`.

The statement for all \(d\ge1\) is proved analytically using the hypercube two-step neighborhood structure. Computational checks do not establish the infinite-dimensional quantifier, independently establish novelty, or certify general local unitary symmetries.
