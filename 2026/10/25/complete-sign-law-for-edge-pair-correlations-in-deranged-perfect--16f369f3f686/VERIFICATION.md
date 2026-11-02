---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Independent enumeration of every perfect matching and distinct allowed edge pair for n=2..6 verifies D_n and all four edge-incidence orbits. Inclusion-exclusion gives D_m=2(m-1)(D_{m-1}+D_{m-2}); transitivity p=1/[2(n-1)]; conditioning on an edge gives c=2(n-1)D_{n-2}/D_n and exact gamma_2, gamma_3, gamma_4. The recurrence proves gamma_3,gamma_4>0, gamma_2 positive n=2,4 and negative n=3 or n>=5; asymptotics use known D_n count. At n=4 gamma_2=1/180, exactly confirmed.

## originality

PASS

Statement-level search and implication audit, not a novelty proof from a failed search. Conditioned matchings and associated random-permutation derangements differ as probability spaces. Uniform matching results on broader regular expanders imply marginals but not exact n^-4 covariance signs. Poisson overlap distribution does not logically force a fine signed covariance coefficient without controlled higher-order error; earlier work is explicitly credited. Best-of-knowledge originality survives with the stated residual risk.

## value

PASS

The excluded-perfect-matching cocktail-party graph is a canonical deranged matching model. Sharp finite-size pair-correlation signs unexpectedly mix dependence, with an exceptional n=4 sign and delicate n^-4 anti-correlation; those precise facts cannot be inferred from Poisson overlap asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
