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

# Reproducibility and limits

The standalone `verify_rook.py` requires Python 3.8 or later and only the standard library. Execute `python verify_rook.py` in the directory containing that file. The script reconstructs the rook graph Laplacian, applies an exact modular Kalman rank computation, independently constructs the Kronecker eigenmodes, and enumerates minimum-size coordinate leader sets in four small parameter pairs.

Actual execution returned `PASS` and displayed full counts: \((3,3)\): \(126\) candidate subsets, \(81\) tree complements, \(36\) controllable; \((3,4)\): \(924\), \(432\), \(432\); \((4,4)\): \(11440\), \(4096\), \(3936\); \((3,5)\): \(6435\), \(2025\), \(2025\). It also passed \(48\) selected full-Kalman comparisons for larger cases, full \((3,3)\) Kalman comparisons, and exact zero-forcing tests at \((3,3)\) and \((3,4)\). All arithmetic used for linear-algebraic ranks is modulo prime \(1000003\), avoiding floating-point eigenvalue clustering.

This is finite regression evidence, not a proof for arbitrary dimensions or a formal machine certification. The general result is established by the separate analytic graph/eigenspace proof in RESULT.md. Eigenvector robustness under heterogeneous graph weights, finite-precision conditioning, and independent audit have not been checked.
