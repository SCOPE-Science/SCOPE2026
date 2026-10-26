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

# Reproducibility checks and mathematical limits

Run `python3 verify.py` with Python 3 and only the standard library. The exact rational example uses rates \(a=1\), \(b=2\), load ratio \(k=1/16\), and separations \(s=\log(9/4),\log4,\log16\). It checks the three derivative signs \(17/1296,-1/16,1/128\), giving \(2,1,2\) strict local maxima. The script also tests 15,000 reproducible random positive parameter tuples, exact continuity at the second outfall, direct derivative signs, and the downstream analytic critical point. Expected output:

```
Phase witnesses: 3 exact rational cases
Randomized derivative/comparison checks: 15000
```

The finite checker cannot prove global uniqueness, any \(k\)–\(s\) phase boundary, asymptotics or the universal \(e^{-2}\) limit. Those statements rely on the derivation and strict monotonicity in RESULT.md. The code does not simulate flow changes, direct oxygen shocks, settling, initial deficit or field measurements. The available literature evidence leaves historical priority uncertainty as documented in REVIEW.md and AUDIT.json.
