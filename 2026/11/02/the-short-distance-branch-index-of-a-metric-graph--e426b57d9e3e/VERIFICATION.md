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

# Reproduction and limits

Run `python verify.py` in an environment with Python 3 and standard library only. This runs an independent exact-rational integration of geodesic-route inequalities in each ordered edge-parameter rectangle using rational polygon clipping and shoelace areas. It compares the resulting exact probabilities against the theorem for 24 example/radius pairs and checks algebraic invariants and the circle/star ambiguity.

Observed result:

```
EXACT_RATIONAL_ALL_ENDPOINT_ROUTES_AND_INTEGRALS_PASSED 24
BETTI_BRANCHING_IDENTITY_AND_SUBDIVISION_PASSED
CIRCLE_THREE_STAR_LOCAL_AMBIGUITY_PASSED
ALL_CHECKS_PASSED
```

The mathematical proof additionally exhausts all possible short geodesics on **every** finite connected simple metric graph; code only verifies particular examples. No claim of independent review, exhaustive testing of all graphs, or finite-sample statistical guarantee is made.
