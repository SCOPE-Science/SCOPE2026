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

# Reproducible checks and scope

The included `CHECK.py` runs under Python 3 with only the standard library. It verifies the stationary generator identities with exact rational arithmetic, integrates a truncated finite-state forward master equation independently to check its first and factorial-second moments, and numerically evaluates the endpoint integrals for an admissible profile. The stationary mean-field formulas and critical exponents are proved in `RESULT.md`, not inferred from finite runs.

Run `python3 CHECK.py` from the extracted package. The test reports a logarithmic coefficient near \(4\) for \(C=1\), a power-law ratio near \(0.995\) at \(\nu=0.7\) and regularization \(\zeta=10^{-8}\), and a stable finite branch for \(\nu=0.4\). Truncated numerical integration has finite-grid and truncation error and cannot certify an infinite statement.

The exact first-moment identity and known general catastrophe factorial-moment theorem are acknowledged as prior work. The reviewed claim is the integrated within-site co-occupation threshold, its asymptotic constants, and its separation from the mean-density transition. No independent validation or publication-priority certification has been performed.
