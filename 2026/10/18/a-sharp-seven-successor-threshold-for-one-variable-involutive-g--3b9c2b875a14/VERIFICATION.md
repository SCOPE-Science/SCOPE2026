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

The proof is self-contained in `RESULT.md` and depends on the fixed-order property of the four leaf functions \(0,1,p,\sim p\) over the two intervals separated by one-half. This property is checked symbolically there; no sampling assertion substitutes for it.

The included `check.py` was executed with Python 3 using only the standard library. It returned:

```
PASS: five crisp stratum tests, 101 degrees
PASS: sharp six strict separation witnesses and 1715 short-star multisets
PASS: 22500 arbitrary nested-formula root comparisons
PASS: each of seven leaves is indispensable for exact root-value preservation
ALL TESTS PASSED
```

The checker's finite 101-point grid and its 22,500 randomized comparisons cannot certify assertions over all \([0,1]\)-valued valuations or arbitrarily many formula occurrences; that generality follows from the displayed induction. It does not test fuzzy accessibility or multi-variable formulas. No independent audit has been carried out.
