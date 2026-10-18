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

# Reproducible checks and scope

The mathematical proof uses finite-group character orthogonality, an orthogonal splitting into coordinatewise zero-sum and constant modes, one real symmetric \((d+1)\)-dimensional block, and its explicit Schur complement. The finite checker constructs character tables directly for mixed cyclic and noncyclic factor groups of orders between two and eight, in two to four coordinates, including all binary and several equal-order cases. It compares raw singular values with the block spectral formula, compares log determinant magnitudes with the exact factorization, and checks the proposed real-block inverse by matrix multiplication.

Run `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py` with NumPy installed. All listed inputs passed with worst absolute singular-value error less than \(4\times10^{-15}\), and log-determinant deviations below \(10^{-15}\) on the listed inputs. Because the experiments cover only these finite samples, they do not constitute a proof for arbitrary products; the RESULT.md proof supplies the exact universal argument. This is not an independently audited mathematical result.
