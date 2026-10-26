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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.9 or later; the program uses only the standard library and terminates with `VERIFY_OK` on success. It checks exact rational modal-energy conservation and the factorized mode comparison for two and three modes at several step sizes. It then checks the finite-iteration transfer to the highest-frequency mode, numerical estimates of the exact geometric ratio and convergence to the two-mode slow-time implicit formula as the base step decreases.

The proof in `RESULT.md`, not any finite computation, establishes strict modal-ratio decay for all steps, positivity of asymptotic constants, the uniform \(O(h^2)\) approximation of the slow-time ODE and the \(h^{-3}\) physical-time correspondence. Diagnostics use a selected finite number of steps and are not exhaustive. All files necessary for the computation are included here; no external paper or data file is a runtime dependency.
