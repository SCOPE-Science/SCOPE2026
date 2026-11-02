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
# Reproducible finite cross-checks

`verify.py` uses Python's standard library. Running `python3 verify.py` checks direct neighborhood-sum constraints by independent last-two-label dynamic programming for all \(2\le n\le80\), \(1\le k\le12\) (948 parameter pairs), including optimal weight and its multiplicity. An additional literal exhaustive enumeration checks 31 bounded parameter pairs, after filtering cases requiring more than 250000 vertex label vectors. Final output is:

```
DP_MATCH 948 cases
EXHAUSTIVE_MATCH 31 cases
VERIFY_OK
```

The program has no third-party dependencies. The formulas for \(n\ge81\) or \(k\ge13\) are not computationally exhausted; they are covered mathematically by the chain-inequality proof in `RESULT.md`. The internal computation of the numbers of optimal functions and a genuinely independent mathematical review are distinct questions: independent audit has not been performed.
