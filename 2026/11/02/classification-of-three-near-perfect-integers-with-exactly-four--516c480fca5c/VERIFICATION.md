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

Run `python3 near3_verify.py` with the Python standard library. It constructs all candidate prime pairs from the inequalities proved in `RESULT.md`, checks exact primality by trial division, constructs each full divisor list from its factorization, independently computes the surplus by both a closed formula and divisor summation, and compares all unordered triples of distinct proper divisors. The code checks the full set of 25 integers and the 17/6/2 shape counts.

Expected header:

```
VERIFY_OK cases=48 by_shape=32,12,4 solutions=25 by_shape=17,6,2 witnesses=32
```

The verifier then prints all 25 integers and all 32 unordered triples. The proof's infinite component is the preceding analytic reduction to the 48 candidate cases. There is no independent audit or external certificate.
