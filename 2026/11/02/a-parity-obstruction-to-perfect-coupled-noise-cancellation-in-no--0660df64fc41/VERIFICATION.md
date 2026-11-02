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

Run `python verify.py` with NumPy. Final package extraction and replay yielded `PASS 915 finite identity, inequality, parity-example and Monte Carlo checks`. Tests independently compare matrix and spectral weighted energies on scalar and multi-block real normal matrices, compare three couplings, verify exact planar cancellation and odd-dimensional noncontraction, and check large-sample Gaussian quadratic energies. Finite floating-point calculations do not prove global optimality, uniqueness or parity; analytical proofs in RESULT.md establish those statements. Ordinary independent scientific validation has not been conducted.
