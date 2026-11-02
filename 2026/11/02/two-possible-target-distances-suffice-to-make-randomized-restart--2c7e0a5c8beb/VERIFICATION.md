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

The standalone program `verify_two_target_restart.py` executes entirely with Python standard-library exact rational arithmetic. It certifies the mixed-clock upper bound; a short-duration continuous lower bound; thirty-five closed interval bounds exhausting the finite intermediate range; a long-duration analytic lower bound; and an exact polynomial certificate valid at all positive Poisson reset rates. It derives explicit rational bounds on \(\pi\), square roots, \(e^{-y}\), and \(\operatorname{erf}(\sqrt y)\), rather than trusting ordinary float comparisons. All of its assertions passed upon execution from the actual accompanying file.

The Brownian reflection-principle and renewal identities, the ratio-of-averages distinction, and the analytic monotonicity of the short-range conditional mean are mathematical proof steps, not empirical approximations. The interval program checks their finite arithmetic consequences but does not independently formalize these analytic lemmas. The theorem proves comparison with all sharp and exponential clocks; it does not establish global optimization among general stochastic clocks. Independent scientific assessment has not been performed.
