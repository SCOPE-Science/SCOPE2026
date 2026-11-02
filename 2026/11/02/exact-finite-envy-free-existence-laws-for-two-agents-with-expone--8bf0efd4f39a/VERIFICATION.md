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

Run `python3 verify.py`. The standard-library checker evaluates exact tetrahedron determinants and rational chamber masses; its asserted exact outputs are:

```
EXACT_GEOMETRY_OK tetra 8/3 positive_octant 1/2 even_sign 3/16 odd_sign 1/16
EXACT_CHAMBERS_OK dominant 4 x 1/8 non_dominant 8 x 1/16
EXACT_SUCCESS_PROBABILITIES_OK m=1: 0 m=2: 1/2 m=3: 3/4 m=4: 29/32
```

A seeded randomized second check directly searches every subset of the sampled chores and compares this result against equality of sign chambers on 30,000 / 40,000 / 60,000 samples for 2 / 3 / 4 chores. In the recorded execution all assertions passed and the measured success frequencies were 0.495967, 0.754975, and 0.907967. The random experiment does not prove exact probabilities. The general result is proved by the analytical chamber geometry in `RESULT.md`; exact rational arithmetic checks specific algebraic and volume identities.

The source PDFs themselves are not dependencies. The standalone package contains the full proof and runnable `verify.py`.
