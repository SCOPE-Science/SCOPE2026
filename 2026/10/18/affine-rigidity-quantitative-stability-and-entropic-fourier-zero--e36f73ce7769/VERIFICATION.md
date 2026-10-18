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

The proof is fully included in RESULT.md. The checker `check_fourier_product.py` requires Python 3, NumPy, and SciPy and runs with `python check_fourier_product.py`. It independently locates first Bessel zeros by numerical sign bracketing; checks 409 randomly generated or exact-equality affine product matrices across five dimension partitions; verifies the volume-normalized determinant bound and the polar Frobenius stability estimate; checks a two-factor shear family; and reports balanced-product ratios for dimensions 10, 20, 40, and 80.

The numerical test passed. Its random seed is fixed for reproducibility. It does not certify universal quantifiers or the asymptotic theorem; both are addressed analytically in the proof. No external scientific audit or independent verification has been performed.
