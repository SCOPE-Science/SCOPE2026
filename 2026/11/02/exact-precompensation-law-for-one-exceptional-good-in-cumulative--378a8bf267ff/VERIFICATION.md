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

# Reproducibility and proof boundary

Run `python3 verify.py` from the directory containing the included source. It uses only Python 3 standard-library `fractions` and `itertools` and makes no network request. Expected output:

```
VERIFY_OK direct_dynamic_checks=891 integer_midpoint_checks=480 symmetric_witnesses=60
```

For 891 triples of nonnegative prefix/suffix block lengths (each from 0 through 8) and 11 exactly represented rational exceptional values at least one, an exact shortest-path dynamic program exhausts all reachable signed bundle gaps and compares their minimum cumulative absolute gap with the theorem's parity formula. A separately constructed allocation attains the predicted optimum for every triple. For 480 integer large-value configurations, a second closed formula is compared directly with the first. For 60 symmetric even-value instances, the explicit optimum and greedy cost are checked; small members are also checked by the dynamic program.

The finite tests cannot establish correctness for arbitrary block lengths or real exceptional values. The unbounded conclusion relies on the analytically proved telescoping prefix bound, simultaneous attainability of nearest reachable suffix lattice points, and the integer midpoint reduction. Full-text priority comparison with the motivating manuscript was unavailable; computational reproducibility and scientific originality are separate issues. Independent scientific audit has not occurred.
