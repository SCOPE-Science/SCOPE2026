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
# Reproducible mathematical checks

Run `python3 verify.py` using only the Python 3 standard library. The check reconstructs the exact rational cubic coefficient for the specified two-patch example, numerically brackets nonuniform fixed points at five supercritical parameters, evaluates both original update equations, computes the two Jacobian eigenvalues and checks their moduli, and confirms a strict equilibrium biomass deficit.

The global uniqueness below and existence above threshold, the general all-equilibrium biomass inequality, the local analytic branch and multiplier expansions, and the extinction spectral-radius identity are proved in `RESULT.md`. The finite tests do not certify those theorems for untested parameter values, and are not independent scientific validation.

The nonhyperbolic threshold's nonlinear global behavior and remote equilibrium enumeration remain unproved. Some scientifically plausible related older publications were accessible only through abstracts; complete publication-priority verification remains open.
