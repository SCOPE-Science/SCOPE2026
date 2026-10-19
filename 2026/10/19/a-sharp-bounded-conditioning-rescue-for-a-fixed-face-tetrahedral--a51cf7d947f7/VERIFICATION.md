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

# Reproducibility

Run `python3 check.py` with a standard Python 3 installation. The checker reconstructs signed oriented tetrahedral face incidence columns, confirms their unique boundary relation and independent three-face Gram matrix, and directly reproduces the weighted up-Laplacian reduction. It uses exact `fractions.Fraction` arithmetic to verify the factorization and characteristic-polynomial coefficients for eight positive rational parameters, then performs numerical symmetric eigenvalue tests against the analytical correlation bound and two limiting constants. One execution prints `PASS: 74 tetrahedral exact rational identities / numerical spectral checks`.

The asymptotic optimality result holds for every positive diagonal retained-face scaling, but checking finitely many parameters cannot establish that universal quantifier. The universal lower bound follows from the exact invariant correlation of the leading principal block; the upper bound follows from the simple distinct roots of the exact cubic. No floating-point stability theorem or general-complex extrapolation has been verified.
