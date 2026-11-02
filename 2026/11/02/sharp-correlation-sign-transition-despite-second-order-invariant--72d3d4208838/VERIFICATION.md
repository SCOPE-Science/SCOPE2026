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

The exact stationary covariance follows from the explicitly displayed three-state discrete Lyapunov equation, which is solved symbolically by `verify_bdf2.py`. Running `python verify_bdf2.py` with SymPy 1.10+ returned:

`VERIFY_OK Lyapunov symbolic identities, variance inequalities, 120 exact parameters, 3335 rational covariance checks`

The program checks the exact analytical formulas and selected rational lag recurrences. The infinite-lag classification is established by the real-root amplitude inequalities or the complex-root sinusoidal argument in RESULT.md. No independent audit has been performed. Scope: scalar Ornstein–Uhlenbeck process, stationary law, correct reused-increment BDF2–Maruyama implementation, exact arithmetic.
