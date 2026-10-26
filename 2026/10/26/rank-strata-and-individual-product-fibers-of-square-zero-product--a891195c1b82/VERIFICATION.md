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

The embedded `verify.py` requires only the Python standard library. It independently constructs matrices over small prime fields, checks idempotence and product-square-zero by actual matrix multiplication, and performs independent finite-field Gaussian elimination to obtain ranks.

Run `python3 verify.py` from the extracted embedded files. The observed markers were `VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_PRODUCT 342` and `VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_FIBERS 2378`. The first count comprises complete fixed-first-factor joint-rank cells over seven small parameter pairs. The second comprises individual-target exact-factorization counts for each square-zero matrix over six parameter pairs. The largest enumerated case for fixed first factors is dimension four over the binary field.

The theoretical proof is field-uniform over all prime-power orders: finite examples do not constitute infinite-field verification, nor do they check simultaneous-conjugacy or nilpotency index above two. The submitted claim rests on the reversible subspace proof in RESULT.md.
