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

# Verification

The complete symbolic proof is in `RESULT.md`. Execute the bundled standard-library program with `python verify_projective.py`. It constructs projective point sets over the prime fields of cardinalities \(2\) and \(3\), computes exact linear spans, finds Duquenne–Guigues pseudo-intents by the recursive definition, and checks every root and minimal antecedent against closed forms. It then checks synchronous rounds on every input for \(\operatorname{PG}(2,2)\) and \(\operatorname{PG}(2,3)\), and on selected inputs plus a full-rank lower-bound witness for \(\operatorname{PG}(3,2)\).

Observed checks:

```
OK PG(2,2) points 7 pseudo_intents 21 direct_grouped 49 direct_unit 49 max_rounds 2 subsets 128
OK PG(2,3) points 13 pseudo_intents 78 direct_grouped 312 direct_unit 1092 max_rounds 2 subsets 8192
OK PG(3,2) points 15 pseudo_intents 105 direct_grouped 1365 direct_unit 1365 max_rounds 2 subsets 104
```

The checker is exhaustive only over the explicitly stated finite instances. The all-field and all-dimension claims rest on the algebraic proof, not exhaustive computation. The review status is self-reviewed; no independent audit has been performed.
