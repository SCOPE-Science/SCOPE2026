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
# Reproducible checks

Run the included `CHECKER.py` with Python 3 and the standard library. It enumerates all \(q^9\) ring elements over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), computes squares and every product of the resulting square-zero elements in the monomial basis, and checks the closed annihilation relation for all ordered pairs.

Observed output:

```text
CHECK 2 squarezero 32 base 4 ordered_zero_products 640
CHECK 3 squarezero 243 base 9 ordered_zero_products 24057
SQUARE_ZERO_ANNIHILATION_OK
```

The theorem predicts \(q^5\) square-zero elements and \(q^9+q^8-q^7\) ordered annihilating pairs. The computations verify these two cases, including every pair, and confirm that all products agree with the leading-coefficient bilinear criterion. They do not verify larger finite extensions or independently validate the proof for arbitrary \(q\). The complete general proof is in `RESULT.md`.
