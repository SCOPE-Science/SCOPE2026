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

The mathematical claim is proved in `RESULT.md`. `verify.py` is standalone, with libraries in `requirements.txt`. It checks symbolically that the paper's payoff difference is exactly the claimed quadratic at the selected parameters and numerically reproduces the forced return-map fold, phase-zero/half-period equality, unit multiplier, asymptotic fold coefficient, and period-budget identity. Tests cover frequencies 0.7, 1 and 2 with modulation amplitudes 0.02, 0.05 and 0.1, plus both noncritical periodic branches for frequency 1 and amplitude 0.05. The file should be run from the extracted package directory as `python verify.py`.

The computation does not exhaust all frequencies, all initial conditions, or all schedules; the global extinction conclusion, orbit-count trichotomy and sharp asymptotic follow from the analytical proof. Small-floater numerical residuals are not proof of global dynamics. The source's 2023 initial-public version was checked independently of its 2024 journal date. No independent audit or external validation is claimed.
