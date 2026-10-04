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

The proof is analytic and does not depend on a finite enumeration. The critical checks are: (1) the score/curvature information identity at an interior oracle, (2) exponential exclusion of boundary optimizers from fixed score separation, (3) second- and third-moment control for the local optimizer expansion, (4) the uniformly order-\(n^{-1}\) perturbation contributed by fixed MDP prior mass, and (5) harmonic summation of the one-step \(1/(2n)+o(1/n)\) deficit.

The standalone script `verify_half_log.py` is a deterministic finite cross-check, not an infinite proof. It uses \(P=\operatorname{Bernoulli}(0.6)\), \(\mu=0.5\), and \(c=0.9\), for which betting optimization reduces exactly to choosing a Bernoulli parameter and the population regret equals a Bernoulli Kullback--Leibler divergence. It sums the complete binomial distribution for each reported sample size, with no Monte Carlo randomness, and verifies convergence of \(n\) times expected one-step regret to \(1/2\) for the empirical rule and for fixed MDP masses \(\kappa=2\) and \(\kappa=10\).

The computation does not certify the theorem for arbitrary distributions; that scope is supplied by the bounded-score analytic argument in `RESULT.md`. Boundary-oracle cases and growing prior mass are deliberately outside the verified claim.
