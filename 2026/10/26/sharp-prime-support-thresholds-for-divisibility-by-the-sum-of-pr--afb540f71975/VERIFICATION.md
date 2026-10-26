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

# Reproducibility and proof checks

The exact proof relies on residue classes modulo 4 and 8, the existence of a 3-mod-4 prime factor of a 3-mod-4 integer, and the elementary nonresiduosity of -1 modulo such a prime. It then uses the prime support and parity of the sum, and separately factor-checks two sharp examples. No unproved computational bound is used in the argument.

Execute `python3 verify.py` from this package directory, using Python 3 standard library only. Observed output:

```
VERIFY_OK: 3654 distinct-prime triples, all n<=300000, two sharp witnesses, 35 qualifying non-prime-powers
```

Finite tests only corroborate, and do not establish, the infinite theorem. The publication-priority check examined several accessible primary full texts and bibliographic records; unindexed equivalent arguments cannot be excluded. Independent audit is not performed.
