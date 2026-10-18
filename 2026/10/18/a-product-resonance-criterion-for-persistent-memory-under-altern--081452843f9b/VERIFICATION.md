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
# Verification

Run `OPENBLAS_NUM_THREADS=1 python3 artifacts/check.py`. The program constructs finite-dimensional physical Hamiltonians and matrix representations of the dissipative generator for odd and even rings, evaluates characteristic spectral data, checks the exact determinant and dark vectors, directly exponentiates one finite-time generator and compares with the predicted limiting density matrix, and independently verifies localized hopping recurrences and normalizing sums.

Checked cases include generic odd cycles, product-balanced even cycles, and nonresonant even cycles. The spectral computations use numerical floating-point linear algebra and an explicit tolerance, not formal or interval certificates. Infinite-size and all-parameter statements are proved in RESULT.md, independent of numerical extrapolation. Symbolic determinant checks at two small sizes additionally use SymPy; numerical routines require NumPy and SciPy. No independent external audit has been performed.
