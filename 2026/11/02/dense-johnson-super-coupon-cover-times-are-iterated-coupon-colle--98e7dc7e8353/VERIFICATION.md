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

# Reproducibility and verification

Run `python CHECK.py` with Python 3 (standard library only). It exhaustively compares the first \(11{,}400\) specified fresh-label slot histories with direct transversal enumeration, and checks \(144{,}000\) seeded finite-population time steps against the epoch lower bound. Expected output:

```
FRESH_EQUIVALENCE_OK 11400
FINITE_MONOTONE_OK 144000
```

The finite checks validate small-instance combinatorial identities and implications but do not verify all \(k,s,n\), the limit law or the mean estimate. Those claims follow from the full deterministic interval argument, the sequential coupling collision bound, a uniform finite-block residual-time bound and the classical coupon-collector limit. No independent mathematical audit was performed.
