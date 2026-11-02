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

# Reproduction of the finite checks

Run `python3 verify.py` using Python 3 with no external dependencies. The script calculates the conditional triangle-count mean and variance in two independent ways: the candidate polynomial and an exhaustive weighted enumeration of *every* free-edge state for each selected observation. Its exact `fractions.Fraction` comparisons cover 612 cases, including the path-versus-claw identity and the regular-graph equal-variance identity. The observed output was:

```
PASS: 612 exact independent checks; no external files or packages required.
```

For the theorem itself, inspect the complete six-row dependent-triangle-pair table and the Bernoulli shared-edge covariance computation in `RESULT.md`. In particular the only pair class depending on the detailed degrees of the observed induced graph consists of two triangles each using an internal observed edge and one common outside vertex; it contributes `2*N*w*p**3*(1-p)`. All remaining variance terms depend on the number of observed vertices and edges, not the observed triangles. The proof works for all finite parameter values. Exhaustive small graphs do not establish a general all-size theorem by themselves.

No independent audit or external validation has been performed.
