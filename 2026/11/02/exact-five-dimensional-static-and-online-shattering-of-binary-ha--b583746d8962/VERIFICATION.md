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

Execute `python3 verify.py` beside `witnesses.json` with Python 3.9 or later. The script checks that the five stored queries in seven bits realize all 32 Boolean patterns, that the listed centers are distinct and in range, and that the exact distance predicate is applied correctly. It also checks the key fiber cardinality constraints in dimensions seven through ten. The recorded output is:

```
FIVE_QUERY_SHATTERING_PASS patterns=32 distinct_centers=32
STRUCTURAL_FIBER_SMOKE_PASS dimension=7
STRUCTURAL_FIBER_SMOKE_PASS dimension=8
STRUCTURAL_FIBER_SMOKE_PASS dimension=9
STRUCTURAL_FIBER_SMOKE_PASS dimension=10
DISTANCE_TWO_ALL_CHECKS_PASS
```

The infinite proof is the four structural lemmas in `RESULT.md`; no finite execution is asserted to verify every dimension. The case of other radii or alphabets was not studied. Independent audit and independent validation have not been performed.
