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

# Proof checks and reproducibility

The finite Euler entries and all ranges are specified in `RESULT.md`. The main proof reduces the claim to a scalar inequality valid for every \(a\in[0,1]\) and integer \(N\ge1\), then separately verifies the fixed-critical-window remainder through a convergent logarithmic expansion. The Bessel identity is derived by differentiating the proposed primitive, and its angular representation is included to fix normalization.

The standard-library program `check_euler.py` was executed successfully from the current package directory and returned `CHECK_OK 98 finite tests; no claim of exhaustive proof`. It tests 8 center-parameter exact rational identities, 72 uniform-bound/symmetry instances, and 18 critical remainder instances. This is finite corroboration only, not an exhaustive search or an independent validation.

All matrix endpoints are included by continuity. The strong-growth asymptotic is conditional on \(N r(1-r)\to\infty\); the critical correction is conditional on \(r(1-r)=\lambda/N\). No other Schatten class, operator-norm bound, singular-value distribution, or optimum value for the absolute error constant has been proved here.
