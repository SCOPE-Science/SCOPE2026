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

# Reproducibility record

Run `python verify.py` with SymPy and SciPy installed. The executable file in the same package performs 64 assertions and reports `64 reproducibility assertions passed` on success. It independently checks the renewal-reward expansion, the Hermite recursion, both optimizer derivatives, numerical exponential-cycle integrals, exact variance against finite-time moment ODE solutions, and strict conditional-variance splitting at sample parameter values.

The analytical proof in `RESULT.md`, not sampling or numerical ODE integration, establishes positivity and optimizer uniqueness for every stated positive parameter. The regenerative proof uses the exponential moment of the cycle duration and the linearly bounded conditional variance; the direct moment hierarchy provides a second nonasymptotic route to the limiting fourth-cumulant coefficient.

Verification is an ordinary same-model mathematical and computational review. No independent audit has been performed.
