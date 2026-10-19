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

# Reproducibility

Run `python verify.py` with SymPy installed. The test enumerates \(16\) decorations when \(m=4\) and \(1024\) when \(m=5\), checking all first moments and all entries of the proposed covariance matrix with exact rational arithmetic, without relying on the proof's symbolic derivation. It constructs the defining real algebra multiplication matrices of block idempotents and verifies their characteristic polynomials for all \(m=4\) decorations and seven fixed \(m=5\) decorations. A seeded 10,000-sample \(m=6\) simulation independently checks expected profile means within the stated tolerance. Passing output ends with `VERIFY_OK`.

## Proven versus checked

The proof is uniform in every integer \(m\ge4\). Finite enumeration does not establish the infinite-dimensional Gaussian theorem; its proof uses a summable variance estimate, Borel–Cantelli and the binomial central limit theorem. Scientific correctness, novelty and value received self-review. Independent audit remains unperformed.
