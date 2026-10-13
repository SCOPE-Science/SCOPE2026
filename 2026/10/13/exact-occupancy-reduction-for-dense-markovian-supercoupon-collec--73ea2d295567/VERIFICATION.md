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

# Reproducibility and limits

The accompanying `verify.py` requires only Python 3 standard-library modules. Execute `python3 verify.py` in the directory containing the file. On the tested runtime it printed:

```
EXACT_PATH_CHECKS_PASS comparisons=510 n=2..6 t=1..6 s=1..n-1
n=2 s=1 mean=2 variance=0
n=3 s=1 mean=2 variance=0
n=4 s=2 mean=7/2 variance=3/4
n=7 s=3 mean=47/10 variance=99/100
n=10 s=9 mean=7409/280 variance=7782021/78400
```

The exact independent checks enumerate all omission paths up to six rounds for universe sizes two through six, compare their distinct-omission counts with Stirling-number occupancy probabilities, map them to the number of uncollected \(s\)-sets using the exact combinatorial formula, and check the cover-time CDF against independent truncated geometric convolutions. Sample moment values are computed as rational numbers from the analytic expressions.

**Scope of verification:** enumeration is finite; no numerical evidence establishes the formulas for arbitrary \(n\) or time horizons. The infinite statements are proved algebraically by the pathwise complement identity, the exact Markov transition kernel, and standard independent-geometric waiting-time and Lyapunov arguments described in `RESULT.md`. The process has no identical consecutive missing elements; it is the distinct-count process, not the omission sequence itself, that matches independent occupancy.
