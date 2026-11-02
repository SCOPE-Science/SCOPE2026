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

Run `python3 verify_mod9.py` with Python 3.8 or later; no third-party libraries are required. The script creates Fibonacci integers and exact Fibotorial products, performs exact integer division, and independently compares every coefficient in rows 0 through 160 with the theorem's modular prediction. It also checks the four-block 3-adic unit factorization at each tested index. It prints:

```
VERIFY_OK integer_pairs= 13041 rows= 161 unit_product_checks= 161 modulus= 9
```

Direct finite enumeration does not prove a result for all integer indices. The proof in RESULT.md uses an exact matrix binomial identity and a separate ternary carry argument to cover arbitrarily large indices. No independent audit has been performed.
