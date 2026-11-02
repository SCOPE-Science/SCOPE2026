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

# Reproducibility and limits

Run `python3 VERIFY.py` (Python 3 standard library only). The program enumerates homomorphisms by possible generator images, counts automorphisms exactly, compares them against the classical partition formula, and independently counts partitions by square-part weights through 23. Verified output:

```
VERIFY_OK automorphism_formula_exact_cases=17 square_partition_weights=24 primes=2,3
```

This check is finite and tests critical structural lemmas only. The probability-one simultaneous law is proved by weighted empirical measures and independent Borel–Cantelli; the infinite one-third threshold is proved using a generating-product upper bound and an explicit disjoint exponential family. The theorem excludes the critical endpoint and assumes independent idealized Cohen–Lenstra samples, not observed number-field class groups.
