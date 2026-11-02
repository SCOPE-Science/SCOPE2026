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

# Reproduction and evidentiary limits

Run `python switching_exit_checks.py` with NumPy and SciPy. The code independently builds the finite-state tilted generator and evaluates its matrix exponential instead of substituting the closed form into both sides. It also solves the backward coupled boundary-value problem by finite differences. The 144 exponential checks had maximum error \(2.69\times10^{-15}\); the six finite-difference checks had maximum error \(1.45\times10^{-6}\); and the 24 rate-ordered mode samples passed. These are numerical checks, not exhaustive verification of the theorem.

The mathematical proof is in `RESULT.md`: a strictly positive causal Green kernel certifies negativity of the switching-rate derivative of each clock mode, nonnegative spectral heat-content weights certify the stated uniform-start stochastic ordering, and a scalar Dirichlet resolvent comparison certifies the fixed-position interval mean order. No external or independent validation has been performed. The closely related Jain–Sebastian 2016 full text could not be accessed.
