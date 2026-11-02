---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The result is for equilibrium-initialized OU dynamics with an independent rate-r Poisson clock and uniformly sampled full historical position at each jump; it does not claim a stationary path law. Conditional reset mean A_t/t gives w′=2c and c′=D/μ−(μ+r)c+(r/t)w, so w′′+(μ+r)w′−2rw/t=2D/μ. The large-s Laplace condition w(0)=w′(0)=0 selects a unique transform; Kummer inversion yields the exact finite-time formula and the r=μ exponential-integral limit. The two noncritical exponents and critical logarithm follow from large-argument Kummer asymptotics. Independent numerical finite-difference checks verified the differential identity for six parameter triples and three positive times; these do not prove the asymptotic theorem.

## originality

PASS

Two directly inspected same mathematical model primary papers derive one-time Gibbs/relaxation laws, not the specified integrated-position variance. No stronger theorem mathematically implying the two-time Kummer finite-T formula was identified after Resultary and original literature comparisons; priority risks remain.

## value

PASS

The one-time Gaussian equilibrium measure does not determine the empirical-average variance; an exact critical transition among ordinary 1/T, logarithmically enhanced 1/T, and slower power-law concentration is a motivated quantitative stochastic-process finding. Its temporal sampling implications are genuine, though no distributional CLT or almost-sure ergodic claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
