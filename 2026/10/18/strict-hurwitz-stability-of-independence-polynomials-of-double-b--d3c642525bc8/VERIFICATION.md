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

# Reproducible finite checks

Run `python3 verify.py` from the directory containing the supplied standalone Python script. The checker independently enumerates all vertex subsets of each double-broom and tests the independent-set polynomial against the analytic hub-state expression for every triple \(2\le a,b\le5\), \(1\le d\le6\): 96 graph instances, up to 17 vertices. It also performs an exact rational Routh–Hurwitz test for every resulting coefficient vector and verifies strict stability on each finite instance. The script uses no nonstandard libraries, no remote data, and no external packages.

Expected final lines:

```
VERIFIED: exact exhaustive graph polynomial comparisons 96
VERIFIED: exact Routh-Hurwitz tables 96
MAX_ENUMERATED_VERTICES 17
VERIFIED: no candidate with a,b in [2,5], d in [1,6] failed
```

The calculations are limited to the parameter bounds listed; they are not exhaustive over all integers and are not a proof of the infinite theorem. The analytic argument in `RESULT.md` supplies the universal proof. The full primary 2026 spider paper was not accessible during literature comparison; its abstract was read, and this remains a residual bibliographic risk. Independent audit has not been performed.
