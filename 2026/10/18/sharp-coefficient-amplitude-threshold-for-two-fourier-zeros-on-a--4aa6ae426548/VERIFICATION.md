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

`verify.py` is a standalone Python 3 script requiring only the standard library. It enumerates all frequency differences with pairwise distinct phases for each prime in its 23-element `PRIMES` tuple; verifies the claimed lower ratio numerically; counts all equal-ratio displacements; reconstructs two prescribed Fourier zeros using the cofactor vector; and checks the full frequency grid for each optimum construction at the smallest four primes.

Observed output from `python verify.py`:

`VERIFY_OK finite_chord_comparisons=62664; constructed_null_and_grid_checks=2478; primes=23; p5_delta=12; p_ge7_delta=6`

The script performs finite floating-point tests with the written tolerance. Its checks are not certificates for arbitrary primes or exact transcendental comparisons. The infinite statement follows from the finite-dimensional nullspace identities, exact integer cyclic-gap inequalities, and direct counting in RESULT.md. The Fourier transform is an unnormalized sum; changing normalization does not change the zeros or amplitude ratios.
