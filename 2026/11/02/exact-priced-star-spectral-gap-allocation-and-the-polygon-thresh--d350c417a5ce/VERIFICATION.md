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

# Verification

The theorem's all-parameter justification is the analytic primal/dual and Cauchy–Schwarz proof in `RESULT.md`; no finite enumeration certifies an infinite family.

The accompanying standalone `verify_star_budget.py` uses Python's standard-library exact `fractions.Fraction` arithmetic. Replay with `python verify_star_budget.py`. Actual run output:

```
VERIFY_OK 13940 exact-rational assertions
```

Checks include all lists of two, three or four spoke-lengths from \(\{1,2,3,4\}\) (their price vectors are the squares), additional deterministic seeded tests through seven leaves, exact positivity and cost of every proposed edge, every principal minor of the reduced semidefinite slack, the dominant-regime dual resultant and kernel identity, and direct zero-sum Rayleigh-form reconstruction. In the polygon regime, the analytic closed-polygon Gram witness supplies the dual optimality proof; no numerical polygon construction is relied upon.

The verifier contains no optimizer invocation and therefore does not independently search over all candidate edge rates. It tests necessary certificate identities for the explicit analytic solution. Completeness, uniqueness and the phase law follow from the written proof. Independent mathematical review has not been performed.
