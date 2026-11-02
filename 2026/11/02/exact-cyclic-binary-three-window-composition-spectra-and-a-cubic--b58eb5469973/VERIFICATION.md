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

Run `python3 verify.py` using standard Python only. The script enumerates all binary words at lengths 3 through 18, directly counts circular windows, compares the observed set with the theorem's inequalities, tests the three explicit period-three formulas, and validates a newly constructed realizing word for every allowed profile through length 45.

Expected terminal records:

```text
EXHAUSTIVE_OK lengths=3..18 words= 524280
CONSTRUCTIONS_OK n=3..45 profiles= 51223
```

These are finite checks. The infinite argument relies on the run identities, the full integer feasibility interval, and coefficient extraction in `RESULT.md`. In particular, neither a finite match nor a successful program run independently proves novelty or correctness for all lengths.
