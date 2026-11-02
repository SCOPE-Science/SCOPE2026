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

# Verification details

The claim is proved by a uniformly convergent 2-adic falling-factorial interpolation, a uniformly convergent divided-difference family, exact derivatives modulo two and four, and three local isometries. These steps cover all positive dyadic exponents without reliance on enumeration.

Replay the embedded `verify.py` using `python3 verify.py`. It independently constructs derangements by recurrence, compares with the integer inclusion–exclusion sum through index 120, checks finite derivative congruences, and exhaustively compares all residue multiplicities for moduli from two through 32768. The observed output concludes:

```
VERIFY_OK exhaustive_fibers=65534 levels=1..15 derivative_mod4_test_points=32 exact_formula_n=0..120
```

The finite tests do not prove behavior outside the tested range. The proof establishes all levels. The historical-priority assessment is based on specific published source comparisons; independent mathematical review is not performed.
