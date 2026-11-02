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

The analytical argument decomposes the entire zero-sum space into the \(b-v\)-dimensional incidence kernel, \(v-1\) paired singular blocks, and a final one-dimensional constant-population component. Endpoint signs and the exact nullspace are proved in RESULT.md; strictness below the endpoint and finite-dimensional Schoenberg embeddings are invoked explicitly.

Replay `python steiner_negative_type_check.py` with NumPy >= 1.24. It reconstructs finite affine planes of orders 3 and 5 and binary triple systems of orders 15 and 31, tests shortest-path distance matrices against design identities, and evaluates centered powered-distance eigenvalues below, at, and above the claimed critical exponent. The endpoint dimension predictions are respectively 17, 49, 29 and 61. Finite floating-point eigenvalue tests are diagnostics, not the all-orders proof; the proof is independent of numerical rounding and is not independently audited.
