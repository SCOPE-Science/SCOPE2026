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

The executable `verify_intensity.py` was run with Python and SciPy after being written from this package. It passed 15 deterministic assertions. The code checks the exact integrated harmonic Feynman–Kac coefficient against the published Gamma ratio for three parameter pairs; it checks that the exact finite-time second moment tends monotonically toward that coefficient for three growing times at each pair; and it checks the elementary Gaussian-error-function integral for the universal coefficient at three strengths.

The program does **not** simulate the full stochastic dynamics, prove a uniform approximation to them, or independently certify originality. The fixed-threshold distributional limit and small-threshold limit follow from the analytic arguments in RESULT.md. A stochastic Monte Carlo or a finite quadrature table alone would not suffice.
