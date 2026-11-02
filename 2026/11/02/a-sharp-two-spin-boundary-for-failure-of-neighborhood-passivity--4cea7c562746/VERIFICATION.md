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

Run `python verify.py` from this directory with Python 3; only standard-library modules are used. The script independently constructs the \(4\times4\) Glauber transition matrix using exact rational acceptance probabilities, propagates the specified Gibbs distribution, and checks the normalized populations, their difference, the strict negative neighborhood-passivity fraction, and the next-step activity. The analytic scalar threshold is numerically bracketed over 1,000 deterministic random parameter triples with 5,000 assertions, but the proof of the parameter-uniform theorem is the derivative calculation in `RESULT.md`, not the finite sampling.

Observed standard-library output:

```
exact stationary and transition identities: PASS
P_(--): -293719/163334085 approximately -0.001798271316118739
next-step activity: 2139045589/5553358890 approximately 0.38518050631516093
parameter diagnostics: 5000 PASS
nominal example B_star: 5.039024061640582
```

The scope of the check is restricted to the stated two-spin Glauber model. The rational negative certificate is exact; the decimal threshold and sampled parameter tests are diagnostic. No separate validation by an independent party has been performed.
