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

The proof checks were performed directly from the definitions stated in RESULT.md.

- For every finite exhaustion stage, the approximating map depends on finitely many equation-membership bits and returns an equational theory, so it is continuous.
- Pointwise convergence follows from finite-premise derivability and the inclusion of every approximating premise set in the full union.
- For the unary witness, cross-variable identities fail in disjoint cycles; same-variable identities with distinct exponents hold under \(f^n=\mathrm{id}\) exactly when \(n\) divides the exponent difference.
- The constant map on a two-element domain satisfies \(f^2=f\) but not \(f=\mathrm{id}\), which verifies the limiting failure.

Limits: no claim is made about uncountable signatures, continuity points other than the exhibited discontinuity, or independent validation. Independent audit has not been performed.
