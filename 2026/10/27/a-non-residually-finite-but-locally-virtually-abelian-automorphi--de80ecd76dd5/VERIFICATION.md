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

# Verification record

Use `python verify.py` from the directory containing this report. On the present package the command completed with output:

```
VERIFY_OK checked_cases= 28279 models= 5
```

The checker constructs five finite-support gap-permutation/translation examples and inverse maps, examines shift equivariance over integer translations and gap parameters, checks local-window consistency at a radius of 50 over a bounded family of configurations, and recounts legal blocks for lengths 1 through 39. Its successful output is a finite consistency check, not an exhaustive classification of all block maps or a proof of non-residual finiteness. Those conclusions require the topological and finite-radius arguments in RESULT.md. The only unreviewed question is bibliographic priority under alternate formulations; no independent audit was performed.
