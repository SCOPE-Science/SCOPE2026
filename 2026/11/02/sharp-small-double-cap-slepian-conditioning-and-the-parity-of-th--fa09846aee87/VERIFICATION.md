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

The proof supplies the exact invariant-block quadratic form, derives every block's leading minimum with the monic Jacobi norm, and selects the global minimum by a strict finite comparison; the largest eigenvalue is independently determined by the two-point spherical reproducing kernel. All asymptotic statements keep the spherical harmonic cutoff fixed.

The bundled `check_caps.py` is self-contained apart from the public Python package `mpmath`. Execute `python check_caps.py`; this checks 85-digit generalized beta-moment eigenvalues for cutoff degrees one through six and three shrinking-cap parameters, including the azimuthal parity, two leading asymptotic coefficients, and monic Jacobi polynomial norms. Direct numerical tests cannot prove behavior for arbitrary bandwidth or arbitrarily small cap radius.

Independent auditing and independent validation are not performed.
