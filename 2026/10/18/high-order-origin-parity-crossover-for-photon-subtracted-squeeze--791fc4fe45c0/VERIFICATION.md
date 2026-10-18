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

Run `python verify.py` after installing the dependencies in `requirements.txt` (NumPy, SciPy, mpmath). The program independently prepares truncated squeezed thermal density matrices, computes conditional photon-subtraction parity directly in Fock space, evaluates a high-precision Taylor recurrence for the exact generating function, and compares the expressions in 16 cases. It additionally checks 120 sign cases, 12 large-subtraction leading terms, and 12 near-threshold double-scaled profiles.

Expected output: `VERIFY_OK fock_cases=16 signs=120 asymptotics=12 boundary_layer=12 max_fock_error=3.21e-11`. The last numerical field may change slightly with floating-point implementation.

The core mathematical proof uses analytic Gaussian overlaps, derivative identities, algebraic sign arguments, and uniform square-root singularity transfer. The finite checks establish none of the infinite-order statements independently. The Fock construction truncates Hilbert space to dimension 90; the high-precision recurrence evaluates finite Taylor coefficients up to the tested order. The asymptotic error is proved for parameters in a compact neighborhood of the critical thermal population within the strict covariance inequalities. There is no independent audit or independent experimental validation.
