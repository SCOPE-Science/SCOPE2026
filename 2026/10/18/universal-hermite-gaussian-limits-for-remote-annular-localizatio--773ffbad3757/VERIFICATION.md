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

# Verification and reproducibility

Run `python3 check_annular_hermite.py` with Python 3, `sympy` and `mpmath` available. The submitted standalone checker was executed successfully: `PASS 160 cross-checks`. It verifies exact polynomial identities, Laguerre/Charlier density equivalence, discrete normalization, and remote-annulus numerical consequences at three radii for window orders zero through three.

The general limit and mode classification require the analytic arguments in `RESULT.md`, notably compact-uniform Charlier-to-Hermite convergence, Poisson large-deviation tail control, and the first Edgeworth correction. The checker samples only finitely many orders, indices, radii, and widths and is not an infinite-dimensional certification. Independent mathematical audit is not yet performed.
