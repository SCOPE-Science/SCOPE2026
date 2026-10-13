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

# Verification record

The included standalone `verify.py` program uses only Python standard-library `itertools`, `math`, and `fractions`. Run `python3 verify.py`. It computes complete small color-assignment censuses and compares actual recursively formed pointed types with the formula, constructs the full unary term clones for three small frames via Boolean operations and the successor diamond, and checks closed-form rational leading coefficients.

Observed replay output:

```
VERIFY_OK type_censuses 51 direct_closures 3 equal_order_reconstruction 31 leading_binary 1/32768 leading_fiveary 1/2985984000000
```

This checks 51 parameter triples against exhaustive valuations, three full unary-operation closures, and 28 further coefficient cases. It does *not* exhaust all heights, branching factors, arities, or formulas. The inductive proof in `RESULT.md` supplies the unrestricted statements. No independent validation or external certification is claimed.
