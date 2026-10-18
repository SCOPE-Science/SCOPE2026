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

The included standalone `verify_symmetric_stochastic.py` uses Python 3, SymPy, exact rational arithmetic and integral Smith normal forms. From each support decomposition for matrix sizes \(3\) through \(6\), it reconstructs all primitive active rays of the normal fan and verifies the exact toric affine class-group factors and the rational Cartier solution. It independently enumerates all basic feasible vertices for sizes \(3\) and \(4\), without assuming the vertex support theorem.

Expected output includes vertex totals \(5,14,58,238\) for sizes \(3,4,5,6\), followed by `VERIFY_OK`. These are finite consistency tests; they do not prove arbitrary-size claims. The theorem is supported separately by the integral block-reduction and exponential-formula proofs in RESULT.md. Tests do not determine singularities at nonfixed torus orbits or classify nonreduced singular schemes.
