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

# Reproducibility and verification

The analytic proof works for all allowed real detunings, nonzero equal exchange couplings, complex pure charger amplitudes, arbitrary battery input phases, and generic collision times. Numerical testing is not an exhaustive proof.

Run `python verify.py` using Python 3 with NumPy and SciPy installed. The deterministic check constructs the complete 8-dimensional Hamiltonian (not the compressed two-sector derivation), uses the matrix exponential, and compares measured battery excitation against the closed formula for random complex states. It also constructs and checks four local product-measurement branches, tests 200 randomly sampled bright-free states at five phases, tests generic phase-cancelling bright states, and checks the opposite-polarization coherent product state.

Observed result: `PASS: 4600 finite-dimensional assertions; independent proof required for all-parameter statement`.

The algebraic proof in RESULT.md supplies the universal quantifiers and treats boundary pulses separately. The checker compares floating-point expressions to stringent absolute tolerances but does not establish an independent formal or expert certification. In particular no assertion is made about the variance of individual energy eigenvalue measurements, only the branch-conditional mean energy after adapted charger readout.
