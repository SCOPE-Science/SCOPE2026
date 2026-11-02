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

# Verification and reproducibility

The companion standalone `verify.py` was executed using Python 3 with SciPy and returned `PASS: 56 finite checks; on/off tail constants, OU generator identity and cycle energy balance.` The program checks Gaussian absolute moments, exact mixed-Gaussian tail formulas and their asymptotic constants at several Pareto exponents, the absorbed-OU flux kernel's large-distance behavior, numerical differentiation of the return Poisson equation, and the algebraic thermal-energy cancellation. Its deterministic quadrature is diagnostic, not a proof of any infinite-limit or all-parameter claim.

The all-order moment thresholds follow analytically from Gaussian moments and the OU killed-potential boundary-value equation, which yields return-occupation growth asymptotic to a positive multiple of the initial distance to the moment order. Both Pareto tail constants are derived using exact Gaussian mixture representations: for exploration, integrate the survival function before conditioning; for return, solve the absorbed OU first-order flux equation and use an exponential endpoint integral. The proof in `RESULT.md` gives the full scope and explicit normalization. No experimental measurements, simulation-based infinite extrapolation, external certification or independent validation are claimed.
