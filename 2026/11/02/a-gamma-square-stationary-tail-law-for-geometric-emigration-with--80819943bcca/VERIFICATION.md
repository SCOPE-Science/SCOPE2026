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

Run `python checker.py` from the same folder. On the recorded Python environment with `mpmath` installed, it printed:

```
PASS: 990 exact and numerical assertions; no infinite theorem is certified by this finite run
```

Checks include rational conditional generating-function and mean identities for several emigration probabilities and states; the stationary gamma-ratio recurrence on explicit rational grids; a closed rational harmonic identity at the critical exponent; and numerical comparisons of gamma/beta constants and recurrence asymptotics. These are supporting finite checks, not a proof of the asymptotic tail or a certification of priority. The argument for the infinite theorem is given in RESULT.md.
