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

# Reproducibility checks

Run `python gap_check.py` with Python 3 and `mpmath` installed. The standalone script was executed and printed `PASS 125 independent Fourier/matrix/asymptotic checks; high-precision arithmetic 36`. It checks twelve explicit periodized finite generators (four sizes times three exponents), Fourier eigenvectors/eigenvalue minimality, the marginal correction at four sizes, and monotone numerical crossover convergence for five values of the moving-exponent parameter at five sizes.

The spectral-minimum and compact-uniform convergence are proved analytically in RESULT.md. Finite computation cannot certify an asymptotic or prove universal novelty. The physical quantum mapping is an effective strong-dephasing statement taken from the cited literature, not a new uniform finite-dephasing theorem. Independent audit: not performed.
