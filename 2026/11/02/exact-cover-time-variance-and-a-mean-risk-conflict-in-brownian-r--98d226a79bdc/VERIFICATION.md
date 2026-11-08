---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently reconstructed all three Neumann/Dirichlet killed-Brownian hitting transforms and their s derivatives, survival renewal formula (1−F(s+r))/(s+rF(s+r)), and inclusion–exclusion for visiting both ends with persistent history. Differentiating at zero yields E[T] and E[T²] with the stated ± weighting. Global mean optimization follows from polynomial derivative negative for z²≥1 at scaled rate 1, not a sampled spatial grid. Independently evaluated hyperbolic closed forms at 45 digits: midpoint minus endpoint mean 0.06615949286375077 and endpoint minus midpoint variance 0.039652244765270864, both strictly positive; package gives rational Taylor enclosures. Verified 99 additional interior values as corroboration.

## originality

PASS

General renewal transform and arbitrary-location cover mean are known. Inspected midpoint distribution and asymmetric-interval mean papers did not establish the combination of arbitrary-location finite-rate variance and global mean-boundary versus lower midpoint variance. A general transform could implicitly determine higher moments after differentiation, so novelty attaches to the explicit certified design conflict.

## value

PASS

The observable comparison is mathematically motivated: the globally mean-optimal reset position demonstrably differs from a lower-variance design in a canonical continuous Markov first-cover problem; the exact finite-rate second moment quantifies stochastic design risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
