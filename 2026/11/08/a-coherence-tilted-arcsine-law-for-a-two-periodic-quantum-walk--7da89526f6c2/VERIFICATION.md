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

# Verification

The embedded `check.py` was run with NumPy and returned exactly:

`PASS: 198 finite diagnostic assertions; no assertion asserts an infinite-time proof`

It checks nine normalized initial states, including \(a=b\), both orders of unequal hoppings, zero coherence and maximal chirality; it compares the first nine Bloch velocity moments with the claimed formulas and evaluates finite-time wavefunction characteristic functions directly via FFT at two times. The finite-time tests use stated numerical tolerances and provide diagnostics only.

The analytical justification is independent: separated-band Fourier differentiation for unequal bonds, direct homogeneous Fourier analysis for equal bonds, a global angular change of variables for the speed distribution, and density integration for the claimed moments and bias. The proof does not rely on a finite numerical fit. No formal proof assistant or external certification is asserted.
