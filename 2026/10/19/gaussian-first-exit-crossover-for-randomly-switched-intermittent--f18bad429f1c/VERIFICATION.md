---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The exact z=(2x)^(-alpha) updates give a uniform positive fast decrement, terminal z in (0,1], and uniform errors O(z^-1) and O(z^(-1-2s)). The fast-choice conditional drift of the decreasing potential bounds E sum_{i<tau} z_i^-u by O(Z^(1-u)), O(log Z), or O(1), according as u<1, u=1, or u>1. The time of ceil(Z/c_alpha) fast choices dominates tau; summing the decrements gives tau=Z/(alpha p)-S_Z/p-M_tau/p+O_P(log Z). The occupation bound and a Bernoulli maximal inequality give tau/Z -> 1/(alpha p). Independently of the fluid Riemann-sum proof, for 0<s<1 telescope z^(1-s)/(1-s). Its fast decrement is alpha z^-s+O(z^(-1-s)); the slow decrement is O(z^-2s), since z_next/z is uniformly bounded away from zero. The total errors are o_P(Z^(1-s)) by occupation. Replacing the fast indicators by p has variance bounded by pq E sum z^-2s, which is o(Z^(2-2s)); the same estimate replaces the slow indicators by q. This gives S_Z/Z^(1-s) -> q/[alpha p(1-s)]. For s>1/2, the occupation estimate directly gives S_Z=o_P(sqrt Z), including s>=1. The Bernoulli functional CLT and convergence of tau/Z to a constant give M_tau/sqrt Z => N(0,q/alpha) without independence of the clock and increments. Substitution gives both Gaussian variances q/(alpha p^2), the critical shift -2q/(alpha p^2), and the asserted negative subcritical correction. The frozen script was inspected, not executed; its seeded ensembles are finite consistency checks, not evidence for convergence or Gaussianity.

## originality

PASS

The leading inverse interval and first-order clock are established in the earlier random LSV literature. The supported distinct result is the annealed second-order clock crossover, including its coefficient and variance. Neither the strongest matching inverse asymptotics nor the checked Birkhoff-sum CLT yields that result under its stated hypotheses.

## value

PASS

Laminar exit time controls the duration of intermittent excursions. Once the first-order clock is known, comparing the systematic slow-step correction with fast-step sampling noise is a natural next question. The exact exponent threshold and shifted law resolve it and are not obtainable from a first-order bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
