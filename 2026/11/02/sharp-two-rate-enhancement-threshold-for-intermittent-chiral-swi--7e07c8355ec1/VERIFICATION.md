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

# Reproducible checks and mathematical limits

The included standalone `verify.py` was run against the package's equations. Its execution reported **160 passed checks**, including independent two-state complex generator inversion, direct time integration of matrix-exponential velocity correlations, symbolic reconstruction of the derivative polynomial, finite-rate optimization sweeps, strict global upper bounds, rapid-switching approximations, the sharp threshold, and the \(|\omega|^{2/3}\) scaling.

To reproduce, run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The script exits nonzero on a failed assertion and reports the total number of successful checks otherwise.

These finite computations validate normalizations and detect algebraic or implementation mistakes, but do not prove statements for all continuous parameters. Universal claims follow instead from exact generator inversion, a strict occupation-fraction inequality, the single-variable cubic sign argument, and its controlled asymptotics in `RESULT.md`.

The full diffusivity formula is contained in existing literature in more general form; the assessed contribution is the global joint two-rate optimization and its sharp attainability and feasibility classification. The result is mathematically self-reviewed, not independently audited or certified. No claim is made about finite-time search, rate-constrained protocols, non-exponential rest durations, or arbitrary resting torques.
