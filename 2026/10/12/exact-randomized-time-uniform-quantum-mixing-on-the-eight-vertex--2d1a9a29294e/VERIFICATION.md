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

# Verification of the eight-path phase law

Execute `python3 verify.py` with Python 3. No network or external packages are needed. The exact run confirmed:

`VERIFY_OK pmf=64 exact_moments=32 exact_projector_entries=64 mod109_affine_rank=16`

The checker constructs the 64 strictly positive integer weights, accumulates 4-by-4 cosine and sine second-moment matrices, proves the eight-path eigenvector-product identities in the degree-six cyclotomic field using exact fractions, and reduces the upper-triangular 64-grid affine-difference matrix modulo the prime 109. Nonzero modular rank is a characteristic-zero lower bound since denominators are coprime to 109. The dimension-16 upper bound, Kronecker density, relative-interior convex transfer, and Carathéodory are analytical proof steps presented in RESULT.md, not numerically simulated. The supporting 2026 literature's full body could not be inspected. No independent audit was performed.
