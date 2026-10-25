---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For finite noninteracting species with fixed immigration lambda_i>0, local loss mu_i>=0 and a common Poisson clearing clock gamma>0, stationary patch age is Exp(gamma) and the conditional occupancy solves a two-state ODE. Its two exponential Laplace moments yield L_ij=gamma*lambda_i*lambda_j/[(gamma+s_i)(gamma+s_j)(gamma+s_i+s_j)]. Diagonal scaling reduces L to the symmetric Cauchy matrix, so its minors, rank by distinct s_i and stated determinant follow from the exact Cauchy double alternant. Bernoulli variance normalization gives Pearson rho_ij as claimed and strict rho<1/2, sharp as gamma->0 in the identical zero-loss pair. Gamma derivative of log rho is strictly decreasing after multiplying by gamma if local loss is positive, giving exactly one positive cubic root; zero-loss case is strictly decreasing. Deterministic common recovery delay gives rho=1 outside model. Independently solved 48 exact-rational stationary four-state generators, matching marginals/covariances and half bound; finite checks are corroboration only.

## originality

PASS

Best-of-knowledge noncoverage of the specific new claim: A natural ecological null model has only one shared stochastic age variable yet produces arbitrarily high-rank environmental dependence; the complete Cauchy minor/rank law and sharp one-half observable correlation discriminator are concrete nontrivial structural and quantitative facts, not just generic positive-association observations. Prior overlapping premises and historical-priority caveats are explicitly credited and scoped.

## value

PASS

A natural ecological null model has only one shared stochastic age variable yet produces arbitrarily high-rank environmental dependence; the complete Cauchy minor/rank law and sharp one-half observable correlation discriminator are concrete nontrivial structural and quantitative facts, not just generic positive-association observations. The unique optimal catastrophe hazard and nonexponential counterexample sharpen its meaningful physical boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
