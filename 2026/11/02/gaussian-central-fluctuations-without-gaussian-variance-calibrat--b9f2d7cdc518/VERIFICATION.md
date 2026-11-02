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

# Computational and analytical verification

Execute `python checker.py` with NumPy and SciPy installed. The standalone program checks 18 independently evaluated quantities across three thermal parameter triples, including equal and unequal wall temperatures. The script directly simulates the distribution of each outgoing Rayleigh velocity, checks cycle duration and reward moments, and independently quadratures the positive two-flight survival probability at two large thresholds per configuration. It also checks positivity of the proposed limiting variance coefficients. The script was actually executed successfully.

The limit laws themselves are proved analytically in RESULT.md using a normal-domain-of-attraction triangular-array argument, renewal-clock inversion, a marked renewal integrability bound for reward fluctuations, and a covariance estimate. Finite experiments alone do not establish distributional or second-moment asymptotics.

The nonequilibrium coefficient for the full current variance was separately checked against the previously published thermal-wall result, Horii et al. (2022), Physical Review E 106, 034130, Equation (61), with the appropriate cycle convention and interval-length scaling. This publication establishes the raw variance, not the newly assessed distribution-level theorem. Historical originality and independent scientific validation have not been certified.
