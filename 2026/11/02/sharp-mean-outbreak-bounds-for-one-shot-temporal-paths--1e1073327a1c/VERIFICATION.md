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

# Reproducible checks

Run `python verify.py` using Python 3 standard library. The code independently simulates each epidemic contact for every seed, every Bernoulli success pattern and every distinct contact ordering on paths with two through seven vertices; the probabilities \(1/2\), \(2/3\), and \(1\) use exact rational arithmetic. It checks the all-order pair expression, both extremal formulas, their full equality conditions, and the uniform-random-order average. The observed replay output was:

```text
ALL_CHECKS_PASSED assertions=10494; exact event simulation through 7 vertices; probabilities=1/2,2/3,1
```

The infinite family of statements is proved analytically in `RESULT.md`; exhaustive finite tests do not establish the all-size conclusions. The comparisons with published research are documented in `REVIEW.md` and `AUDIT.json`. No independent mathematical audit has been performed.
