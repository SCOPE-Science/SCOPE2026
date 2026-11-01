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

# Verification scope

The accompanying `check_spectral_onset.py` uses only standard Python modules. Run `python3 check_spectral_onset.py` to verify independent finite-product evaluations of the harmonic multiplier against its Gamma form; sign equivalence of the positive-ratio and two-term coefficient formulas; first-positive-index computations for selected fixed dimensions and small positive exponents; and finite-scale diagnostics of the derived crossover.

The script passed **176 finite diagnostic assertions** during package preparation. The complete infinite statement instead follows from the uniform Gamma-ratio estimate, the quadratic-root expansion, and a two-sided argument for the least positive index in `RESULT.md`. Finite numerical checks do not prove eventual positivity, exact asymptotic constants, or the existence of a counterexample. The last implication uses Feng–Zhang's proved fixed-degree lower bound and applies for sufficiently small amplitude chosen *after* the degree and exponent.

The result does not assert uniform amplitude bounds, optimize the actual second variation, or cover simultaneous dimension growth. No independent validation has been performed.
