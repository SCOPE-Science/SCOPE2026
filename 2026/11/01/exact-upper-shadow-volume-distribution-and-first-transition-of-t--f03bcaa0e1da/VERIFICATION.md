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

# Reproducible verification

Run the standalone standard-library program `python verify.py` in the same directory as the accompanying result. It enumerates 192 integer orbit representatives, obtains 384 nearest edges, proves combinatorially that there are no nearest-neighbor triangles, checks the cap lens by numerical quadrature at six thresholds, and compares five upper-tail values with a seeded 240,000-direction simulation. The observed outputs were:

```
threshold 2.40370085 exact 0.600979925 sample 0.5994375
threshold 2.41 exact 0.567417458 sample 0.5665875
threshold 2.43 exact 0.438906113 sample 0.438029167
threshold 2.46 exact 0.186554738 sample 0.186241667
threshold 2.49 exact 0.008646668 sample 0.008733333
VERIFY_OK: 192 centers, 384 triangle-free nearest edges, six lens integrals, five Monte Carlo tails, quadratic coefficient
```

The integer enumeration is exhaustive for the finite center orbit, while the Monte Carlo trial and quadrature are diagnostic only. Analytic identities and the exact quadratic asymptotics are established in `RESULT.md`. No independently performed mathematical audit is asserted.
