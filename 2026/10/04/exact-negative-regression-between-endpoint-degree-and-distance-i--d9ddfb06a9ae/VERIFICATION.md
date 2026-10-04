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

The proof is analytic. The accompanying checker uses exact integer and rational arithmetic.

It exhaustively enumerates all Prüfer codes for \(2\le n\le8\), reconstructs the joint law of the distance between two fixed labels and the degree of one endpoint, and checks the exact distance distribution and every conditional degree probability.

For \(2\le n\le80\), it constructs the claimed binomial-plus-Bernoulli conditional laws directly and verifies strict stochastic decrease in distance, the conditional mean formula, and the covariance identity.

The asymptotic Rayleigh statement is not inferred from finite replay. It is proved in `RESULT.md` from the exact distance mass function and an exponential product bound that gives moment convergence.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK trees_enumerated=280392 distance_mass_checks=28 conditional_probability_checks=84 mean_checks=28 stochastic_tail_checks=85241 covariance_checks=7`.
