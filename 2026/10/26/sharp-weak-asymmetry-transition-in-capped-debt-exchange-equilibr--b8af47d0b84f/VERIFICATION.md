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

Run `python wealth_phase_check.py` with Python 3 using only its standard library. The script independently enumerates small integer-wealth configurations and compares them to the exact sector count, checks detailed-balance equalities as fractions for every admissible move of a finite system, and checks continuity and ordering at several critical parameter values. It performs 278 exact count/detailed-balance assertions and 12 numerical critical-curve assertions, then computes finite-sector expectations at five parameter values and two population sizes. All checks passed in the original execution.

The finite-size expectation table approaches the explicit theoretical debt density but is not a convergence certificate. The infinite proof rests on the stars-and-bars identity, uniform logarithmic asymptotics, strict concavity of the limiting entropy, concentration of aggregate debt and negative-site fraction, and uniform-composition tail ratios. The script requires no external files, downloads, proprietary dependencies, or network access. No independent audit has been performed.
