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


# Verification of the mathematical result

The analytic computation differentiates the exact polar Fock Toeplitz matrix twice. The two lowest monomial degrees form an isolated spectral cluster, so the second derivative of their eigenvalue sum equals the diagonal matrix second derivative plus the external second-order Rayleigh terms. Terms linking only the first two monomials cancel on summation. Strict Fourier-coefficient ordering follows from comparing explicit falling factorials for **all** integer frequencies, rather than sampling them.

The standalone `verify.py` uses only Python standard-library arithmetic. It checks 1,060 exact rational coefficient/ordering identities and 12 numerical centered second differences of the two largest eigenvalues of separately integrated perturbed-domain matrices. It prints:

```
RATIONAL_IDENTITIES_OK 1060
DIRECT_SHAPE_SECOND_DIFFERENCES_OK 12
ALL_CHECKS_OK
```

Run `python3 verify.py` from the directory containing this file. The numerical tests use finite sections and finite differences, not an exhaustive verification of the infinite-dimensional statement; the analytical proof supplies that step. No independent mathematical audit was performed.
