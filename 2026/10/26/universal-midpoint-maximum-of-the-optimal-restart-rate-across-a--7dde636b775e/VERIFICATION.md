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

# Reproducibility and mathematical limits

Execute `python check.py` with Python 3.9 or later and no third-party libraries. The checker evaluates the no-reset transform in two algebraically independent ways: the explicit closed form and the exact solution of the matching two-region boundary-value problem. It then compares the mean obtained through global resetting renewal to the dimensionless formula, compares analytic first/second derivatives to finite differences, evaluates second-derivative positivity, and tests the optimal-rate midpoint and permeability trends on deterministic parameter sweeps.

Observed result: `PASS: 1461 deterministic tests; direct boundary, renewal, derivatives, convexity, midpoint and resistance monotonicity`.

The mathematical proof is in `RESULT.md`. Its decisive steps are the exact backward-interface solution, renewal identity, strictly positive second derivatives on the entire open domain, unique optimum by coercivity, and implicit/envelope differentiation. Numerical checks at finitely many parameter choices do **not** establish continuum claims, source novelty, or an independent audit. The asymmetric/reset-screened or infinitely impermeable regimes are outside scope. The independent-audit channel has not been performed; the above checks are internal mathematical corroboration only.
