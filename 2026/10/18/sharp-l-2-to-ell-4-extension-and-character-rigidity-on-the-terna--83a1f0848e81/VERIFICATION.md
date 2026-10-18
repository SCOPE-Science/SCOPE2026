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

# Reproducible verification

Run `python artifacts/check.py` with Python 3 and SymPy installed (no other third-party packages). The checker was executed against the actual included source and returned:

`VERIFY_OK symbolic_identities=7 random_complex_cases=350 Fourier_values=3150 equality_modulations=9 constant_energy=77`

It verifies the complete nine-point convolution formula against an independent symbolic sum, reconstructs the antipodal-balancing dependence and symmetric reduction, differentiates the mixture and scalar ratios exactly, proves the closed-form radical simplification, tests 350 fixed-seed complex inputs against both direct Fourier evaluation and the inequality, verifies every additive-character equality case, and checks the constant-input convolution energy.

These computations are corroborating evidence only. The unrestricted inequality and equality classification rest on the symbolic identities, monotonicity/end-point arguments, one-line Plancherel bound, and triangle-equality constraints in the written proof. No finite random test is claimed as a universal proof. No independent audit has been performed.
