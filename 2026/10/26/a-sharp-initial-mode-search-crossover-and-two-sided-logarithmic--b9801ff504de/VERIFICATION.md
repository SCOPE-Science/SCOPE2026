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

The calculation uses explicit initial-mode first-arrival transforms from Flaquer-Galmés, Campos and Méndez (2024), equations (22) and (25), and the complete-Poisson-reset renewal identity from their equations (35)–(38). The comparison is reduced to the sign of two exponentials. Positivity, uniqueness, the sharp parameter threshold and both asymptotic logarithmic coefficients are established algebraically in RESULT.md.

`verify_mode_crossing.py` runs direct symbolic checks of the two pivotal polynomial identities using SymPy, numerical crosschecks against the separate source transform formulas for multiple positive parameter choices, and sample endpoint-limit convergence ratios. It also tests a reentrant search-preference example. These computations are checks on, not substitutes for, the all-parameter proof.

No stochastic simulation, infinite computer certification, statistical confidence interval, or independent human audit is asserted. The published paper contains the full raw transforms; an unindexed independent global comparison remains an originality risk.
