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

# Reproduction and verification

Run `python checks/check_temporal.py` from the package root with Python 3. Only the standard library is needed. The script independently computes the two-state killed-generator survival using time-stepped ODE integration, checks its eigenvalue polynomial and exact two-exponential form, compares the iid-gate maximum with its Gumbel normalization over several parameter sets and sizes, and runs an event-driven Gillespie simulation of the full ON/OFF star contact process. It also separately forms and solves the exact finite-state generator over rational numbers for the two-leaf case with unit rates, obtaining \(268/45\), and compares its value to a seeded simulation.

The packaged checker was executed successfully and reported 195 passed assertions/diagnostics. The supplementary simulation produces finite-sample variability; its pass tolerances are deliberately broad, whereas the stated theorem follows from the analytic concentration, pathwise sandwich, killed-generator, and maximum asymptotics in `RESULT.md`.

The exact finite-state calculation concerns \(n=2\) only; it does not independently certify the infinite-size Gumbel law, the expectation constant, or historical originality. No independent audit has been performed.
