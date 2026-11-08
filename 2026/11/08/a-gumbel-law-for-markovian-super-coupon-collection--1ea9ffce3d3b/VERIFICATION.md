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

Run `python3 verify.py` with Python 3 and the standard library. The script independently enumerates Johnson-graph single-replacement transitions; checks detailed balance and the exact triangular inclusion-coordinate action; verifies single-target stationary entrance flux as rational numbers, and bounds the two-target entrance probability for small instances. Its stochastic sample is a seeded diagnostic only.

The finite enumeration checks 74,138 exact rational equalities and inequalities, then prints a separate finite-sample diagnostic. These checks do not establish the asymptotic theorem, which follows instead from the full argument in `RESULT.md`: eigenvalue gap, stationary flux and killed-chain perturbation, joint avoidance, Poisson factorial moments, and first-moment tail integration. The limit has no independently certified error bound or independent mathematical audit.
