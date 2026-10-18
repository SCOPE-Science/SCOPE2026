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

# Reproducibility and check boundaries

The quantitative statements follow from the explicit Markov generator and integrals in `RESULT.md`, not from simulation. `CHECK.py` runs with Python 3 and the dependency in `requirements.txt` and was executed successfully with 49 deterministic assertions before packaging. It checks the direct two-rate finite-state generator solution against the general integral moment formulas at four redraw rates, the exact deterministic-rate independence boundary, rational partial fractions, gamma-rate slow-refresh approximations for three density exponents, the key integral identity, and the exponential-rate finite-refresh and limiting formulas. The gamma-law comparisons use finite redraw rates and have explicit numerical tolerances; they cannot establish a limit for all rate laws. The exact symbolic reduction and full asymptotic proof are stated in `RESULT.md`.

Checks do not certify originality and do not establish a joint scaling limit of the full stationary particle distribution. All stationary moments are defined with the environmental refresh rate strictly positive before taking the slow-refresh limit. The accessible 2025 literature describes related one-particle and simultaneous-reset models; implicit consequences of more general Cox-process theorems remain a residual originality risk.
