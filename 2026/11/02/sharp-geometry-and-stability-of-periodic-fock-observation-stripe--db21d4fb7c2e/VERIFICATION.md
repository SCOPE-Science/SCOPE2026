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

The proof establishes the exact multiplier, strict periodic Gaussian monotonicity via Jacobi's product, both strict bathtub comparisons, and the exchanged-mass estimates. Large-period and fine-microstripe limits are obtained analytically, not by extrapolating finite computations.

The included standalone `check.py` executes `python3 check.py` using the Python standard library. It compares periodized Gaussian values with their Poisson Fourier series; tests extrema of reference intervals and valid exchange bounds at finitely many sampling points; and checks the Gaussian-tail and leading-harmonic expansions. The number of successful assertions is printed on successful completion. These tests are finite and subject to floating-point tolerances. No computational test verifies all measurable masks, all periods or historical novelty.

No independent audit was conducted.
