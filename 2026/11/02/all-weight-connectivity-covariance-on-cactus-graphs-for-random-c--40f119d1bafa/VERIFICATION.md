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

Run `python3 verify_cactus.py` using Python 3 standard library. Expected output:

```
PASS polynomial coefficients: 21 nonnegative; nonnegative cross-spanning H
PASS exact rational covariance inequalities: 13560
PASS graphs: 7 ; weight patterns: 2; models: forest, q=1/3,2/3,2
```

The code independently expands the exact four-cell polynomial and checks its 21 nonzero coefficients, checks the nonnegative cross-spanning polynomial, and enumerates all edge configurations for seven cactus graphs under two nonuniform rational weight patterns for the forest and three random-cluster parameters. It uses exact fractions and verifies every vertex-pair indicator covariance numerator, totaling 13,560 finite exact inequalities. General finite cactus graphs are proved by the analytic independent-block reduction and the displayed polynomial identities, not by exhaustive finite tests. Independent mathematical audit has not been performed.
