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

# Reproduction

Run `python checker.py` with NumPy installed. The checker constructs skew Paley conference matrices of orders \(8,12,20,24,32\), verifies \(C^2=-(N-1)I\) exactly, enumerates all five-element index sets, and compares their squared-Pfaffian type and exact class-count formulas. It independently diagonalizes representative five-column Gram matrices and compares to the predicted eigenvalues at absolute tolerance \(10^{-12}\). Separately, all \(1024\) five-vertex sign tournaments are checked for the universal parity dichotomy and an independent determinant identity.

Observed output: universal pattern counts \(384\) of type \(r=0\) and \(640\) of type \(r=2\); all Paley cases pass with type counts \((0,56)\), \((132,660)\), \((4104,11400)\), \((12144,30360)\), and \((62496,138880)\) for the five successive orders. All tests passed.

The mathematical proof is exact and covers every existing skew conference matrix of order at least eight. No computer search, numerical tolerance, or finite run is used to prove the general classification or the matrix-independent multiplicities. No independent audit or validation was performed.
