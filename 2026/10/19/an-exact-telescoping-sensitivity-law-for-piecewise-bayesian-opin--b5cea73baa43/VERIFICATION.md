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
# Verification of the telescoping sensitivity identity

The proof in `RESULT.md` gives a direct log-odds conjugacy and establishes every claimed finite-horizon and infinite-time assertion for all eligible finite networks. The original paper's Eqs. (4)–(5) were compared against this derivative identity.

## Executed reproducibility checks
Run `python verification_bayesian.py` using the Python standard library. The program passed 1,995 finite arithmetic and asymptotic-limit spot checks. In particular, it checks 480 randomly seeded complete runs involving two through six agents, exact rational update rates selected by piecewise receiver/sender comparisons, endpoint Jacobian telescoping, and the sharp single-agent construction. The exact arithmetic tests verify algebra; no finite experiment is invoked to certify the infinite-time nonpositivity bound or exhaustive network coverage.

## Boundaries and unverified claims
Derivative formulas are asserted only along locally regular branch itineraries for a fixed exogenous update schedule. Cross-switching trajectory differences, randomness of the update schedule under perturbation, boundary beliefs and smoothly variable likelihood ratios lie outside the proof. The result has not been independently audited, and a general published theorem with equivalent implication remains possible.
