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

The analytical derivation solves the three first-step equations for an absorbing continuous-time Markov chain. The denominators remain nonzero for arbitrary strictly positive local extinction rates and for both endpoints of the colonization budget. Differentiation of each exact mean gives the same negative quadratic curvature. Convex-combination averaging then proves the unique global constrained optimum, including all endpoint equalities.

Run `python verify.py` with a standard Python 3 interpreter. In the supplied run, the exact rational checker passed 2916 assertions covering independent generator inversion, special parameter boundaries, objective curvature, the closed-form optimum, and the example. Computation is supplementary; these finite tests are not a substitute for the all-parameters proof. The package does not verify finite-horizon survival optimization, quasi-stationary optimization, or any model with demographic abundance or exogenous recolonization. Historical scientific priority has not been independently certified.
