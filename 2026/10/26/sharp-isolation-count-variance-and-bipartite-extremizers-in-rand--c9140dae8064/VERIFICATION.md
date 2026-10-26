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

The accompanying standalone `verify_isolation_variance.py` requires only Python's standard library. Executing `python verify_isolation_variance.py` returned:

```text
VERIFY_OK 125 exact independent-rank, integral, and variance comparisons
```

For every \(1\le d\le3\) and every \(0\le t\le d\), complete rank enumeration of all continuous-mark orderings checks the exact nonadjacent pair probability. For \(1\le d\le29\), rational binomial expansion checks the adjacent triangular integral, variance formula on \(K_{d,d}\), and the sharp coefficient. These are finite exact tests; the proof covers all positive integer degrees and host orders analytically. Neither independent review nor computational verification of the infinite collection is claimed.
