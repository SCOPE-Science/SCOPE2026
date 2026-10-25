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

Run `python verify_weighted_tga.py` with Python 3.10+ and NumPy, SciPy, SymPy. The checker verifies the exact radical witness by symbolic multiplication, the balanced-threshold positive factorization, the ratio-reversal symmetry, 4,000 parameterized numerical stationarity constructions, and eleven numerical frontier checks. Its terminal success token is `VERIFICATION_OK`. The universal if-and-only-if result is proven algebraically in `RESULT.md`; a finite program cannot prove it for all positive real parameters.

Scientific limitations: This check assumes the indicated ordinary Euclidean inner product and the exact small-dimensional update; it is not a floating-point reliability or physical-model validation test.
