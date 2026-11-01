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

# Verification record

The standalone `verify.py` uses SymPy and Python's exact rational arithmetic. It checks the golden-ratio algebra, the invariant density, the stationary mean, the four-by-four transfer matrix, its spectrum, the first sixteen exact lag covariances and their two-exponential formula, the finite geometric-sum formula for each of sixteen time horizons, and integer-expansion digit/displacement identities on several exact rational orbits.

Run with `python verify.py` in a working environment with SymPy installed. The expected terminal result begins `PASS: invariant density` and identifies the other checked components.

The infinity of parameters and orbit times is justified by the inequalities, semiconjugacy and transfer-operator recurrence proved in `RESULT.md`, not by the finite test runs. The stationary initialization is specified explicitly, and no statement is made about a stochastic perturbation or independent external verification.
