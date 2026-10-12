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

The proof derives each required moment from the full three-visit detection-history law, then algebraically reconstructs \(\pi,c,s,p_1,p_2,p_3\). The identities and nonzero denominators are stated in RESULT.md. The standalone verifier is `verify_model.py` and requires only Python's standard library; run `python3 verify_model.py` after extraction.

Observed exact arithmetic output:

```
VERIFY_OK two_season_alias=1 singular_three_season_alias=1 nondegenerate_exact_reconstructions=554 varying_detection=54 stationary_hidden=30
```

The 554 checked tuples include equal and unequal seasonal detection probabilities, positive and negative hidden transition contrasts, and stationary or nonstationary initial occupancy. The checker also compares every probability in two explicitly distinct but observationally equal two-season models and two equal-transition three-season models. No numerical tolerance is used. The proof, not the finite checked grid, establishes every interior tuple and any longer singular history. No observational data or independent external audit was used. Material public-source access was incomplete for parts of the historical ecology literature.
