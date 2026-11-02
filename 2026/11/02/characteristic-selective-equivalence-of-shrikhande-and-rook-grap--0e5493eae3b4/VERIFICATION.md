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

The exact standalone finite checker is `artifacts/verify.py` and requires Python 3 standard library only. Execute `python3 artifacts/verify.py`; its recorded successful output is in `artifacts/verify_output.txt`.

The checker independently constructs the two sixteen-vertex adjacency matrices, verifies their strongly regular parameters and nonisomorphic open-neighborhood structures, checks the four local complementations and explicit vertex permutation edge by edge, and compares every one of the \(65536\) labeled binary cut ranks. It exhaustively verifies maximal absolute determinants \(2\) and \(3\) for all binary \(3\times3\) and \(4\times4\) matrices. For each graph it checks all \(1820\) four-vertex subsets by independent modular Gaussian elimination over \(\mathbb F_3\) and \(\mathbb F_5\), and by direct \(3^4\)-coefficient left-null-vector enumeration. It checks integer alternating cut-row relations on the deficient induced four-cycles.

The finite enumeration supplies an exhaustive certificate for the stated graph pair and the determinant bounds; analytic steps in `RESULT.md` prove the prime-uniform extension, graph-state cut-spectrum statement, and local-unitary obstruction. No independent scientific audit, external expert validation, composite-dimensional extension, or numerical simulation of all prime-dimensional quantum states is claimed.
