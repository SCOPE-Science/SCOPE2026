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

# Reproducibility and bounds

`python3 verify_wheels.py` requires Python 3 and its standard library only. The program constructs wheel neighbor sets explicitly, examines every binary activity profile for rim sizes \(3\le m\le13\) and thresholds \(2\le r\le m+2\), and compares against the stated formulas. It independently counts maximal independent sets of cycles for \(3\le m\le18\), checks all their sizes, and evaluates the Perrin recurrence through \(m=100\).

Observed output:

```
OK: 99 wheel parameter cases; 425952 full binary profiles; 16 independently enumerated cycle tables; 98 Perrin values; unique equilibrium only at (m,r)=(7,3) within tests
```

The mathematical proof in RESULT.md handles all integers in the stated domain. The script checks finite instances only; it does not certify an infinite theorem, publication originality, or the absence of other equilibrium notions.
