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

# Reproducibility

Execute `python verify.py` with Python 3 and `mpmath`. The script checks 35 exact absorbing probabilities via a vacancy-mask Markov recursion independent of the derived open-path recurrence, 21 exact-versus-series generating coefficients with high-precision evaluation, two large-order simple-pole asymptotics, and the numerically evaluated symmetric root and its parameter derivative. Success produces a single `PASS` line. The coefficient proof and analytic perturbation appear in `RESULT.md`; experiments are finite and not independent proof of the general statement. No external validation has been performed.
