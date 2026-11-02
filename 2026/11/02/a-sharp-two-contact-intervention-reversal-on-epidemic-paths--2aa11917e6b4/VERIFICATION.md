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

# Mathematical verification

The analytical proof is in `RESULT.md` and defines the edge probabilities, the uniform-seed expectation and all quantified parameter ranges. Reproduce the exact finite calculations with:

```bash
python3 verify.py
```

The checker uses Python 3 standard-library fractions and multivariate integer-coefficient dictionaries, not an external solver. It verifies symbolic identities for every pair on paths of three through six vertices, the general identity for every pair through twelve vertices, and separately reconstructs expected infections from independent enumeration of all bond patterns and all possible seeds for a rational grid including exact tie cases. The completed run reported **794 passing exact symbolic and rational assertions**.

Positivity over the full continuum \(0<q<p\le1\) comes from explicit factored algebraic expressions in the proof. The general \(n\ge6\) claims follow from strict discrete convexity, strict ordering of central sensitivities and finite-parameter continuity; finite checks are not represented as certificates of those infinite assertions. Numerical examples are explanatory, not proof. This verification covers the intended independent-bond model only, without independent validation or claims of empirical epidemic accuracy.
