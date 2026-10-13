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

# Verification notes

Run `python3 verify.py` with the Python 3 standard library. This program separately checks Fourier eigenpair relations for the concrete magnetic adjacency operator, finite polynomial and parity consequences for every even order up to 128, an explicit odd-prime amplitude bound for many phases and times, and exact half-flux cancellation numerically up to floating-point error. It samples generic-phase transport fidelity for four and eight vertices. Expected successful output begins with `NUMERIC_GENERIC` and ends with `VERIFY_OK`.

The unrestricted assertions rely on the exact Fourier decomposition, the primitive-root minimal polynomial, the annihilating geometric sums, a product-distance/Cauchy--Schwarz estimate, and the continuous-time Kronecker compatibility theorem. Finite checks cannot establish existence of arbitrarily good times or prove nonexistence outside the checked cases. This is not an independent audit or external certification.
