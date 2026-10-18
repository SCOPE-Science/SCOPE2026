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

# Reproduction and limits

Run `python verify.py` in an environment with `scipy` installed (also documented in `requirements.txt`). The verifier carries out deterministic quadrature checks of the known Gamma stationary transform against the derived conditional-age transform, Gamma-immigrant and branching-transform identities, derivative checks of the conditional first moment, and Poisson-rate algebra. Its recorded execution passed 308 assertions.

The exact analytic proof is in `RESULT.md`. It uses the source's branching Laplace exponent and stationary Gamma law, the Palm law for independent Poisson immigration, Markov's inequality, and independent Poisson thinning. Numerical checks only assess identities on tested parameter grids and do not establish the infinite-parameter or finite-dimensional theorem.

The originality review inspected the motivating paper and the relevant assumptions of broader immigration-limit literature. Complete global priority search and independent scientific audit are not represented as performed.
