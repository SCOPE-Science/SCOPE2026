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

# Reproducible exact checks

From a directory containing the supplied `verify.py`, run `python3 verify.py`. This uses standard-library arbitrary-precision integers. The exact run produced:

```
support=(3,5,7) eligible=4650 hits=1 smallest_nonample_deficit=79
support=(3,5,11) eligible=3718 hits=0 smallest_nonample_deficit=139
support=(3,5,13) eligible=3459 hits=0 smallest_nonample_deficit=169
witness_N=801204488268064453125 a(N)=841632661765951062016 excess=40428173497886608891
verified=11827 exponent triples; independent divisor and factorization checks passed
```

The coefficient recurrence is obtained by exact formal-power-series comparison, not fitted to the data. All candidate supports are first proved exhaustive using divisor-sum inequalities. The candidate search uses exponent bounds justified by comparison with the exact witness and exact integer products. The complete independent proper-divisor recurrence cross-check covers the witness divisor box. A separate ordered-factorization inclusion-exclusion computation confirms the terminal value. The code asserts all reported values and exits on a mismatch.

Scientific limits: the exhaustive certificate excludes all strictly smaller **odd numbers with exactly three distinct prime factors**; it does not enumerate all larger three-prime numbers or odd ample numbers of four or more distinct prime factors. Independent mathematical audit has not been performed.
