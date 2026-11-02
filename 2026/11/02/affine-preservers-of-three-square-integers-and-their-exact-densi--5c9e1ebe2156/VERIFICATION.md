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

Run `python3 artifacts/verify.py` with Python 3 (standard library only). This independently computes the three-square representability characteristic function through 1200 by enumerating triples of squares; compares it with Legendre's congruence criterion; verifies the proposed affine classifier against exact representability for 16512 integer slope-intercept pairs and every eligible input below 1600; and checks the exact square-box counting recurrence for boxes through 256.

Expected output:

```
VERIFY_OK tested_pairs=16512 predicted_good=2479 predicted_bad=14033 three_square_sieve_through=1200 input_test_range=0..1599 exact_recursion_X_through=256
```

These experiments are finite, and no arbitrary large-scale enumeration proves the general result. The proof separately verifies the critical 2-adic inverse-image rigidity for odd slopes, the obstructed valuation-one slopes, reduction by factors of four, and the asymptotic geometric sum. The public source gives the classical forbidden classes; it does not supply the new affine-map classification. Independent audit has not been performed.
