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

The standalone standard-library checker verifies semiring laws, monotone evaluation on exhaustive bounded extensions, the two-domain test, and collapse of the designated sentence at caps one and two. Run `python3 checker.py`; observed output:

```
ALL_CHECKS_OK axioms=1295 extension_pairs=10269 witness_cases=13
```

The infinite formula nondefinability theorem is proved by the additional-monomial argument in `RESULT.md`. No finite test covers every existential sentence. The longer arXiv manuscript was not fully accessible for textual priority comparison. Independent audit has not been performed.
