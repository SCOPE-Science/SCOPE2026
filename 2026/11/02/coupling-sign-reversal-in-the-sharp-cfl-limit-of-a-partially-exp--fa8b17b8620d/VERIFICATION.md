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
# Reproducibility and limits

Run `python verify.py` from the same directory with SymPy 1.10 or newer. Exact symbolic identities cover the dispersion polynomial, discriminant, boundary determinant, constant term and three critical squared-step values. The program also evaluates 880 finite representative modal parameter sets for both sides of the analytic threshold. Expected output:

`VERIFY_OK: 5 symbolic identities, 3 exact boundary values, 880 independent modal grids`

The mathematical proof in RESULT.md, not finite tests, establishes the universal statement. Boundary Jordan growth follows analytically from a scalar characteristic root of multiplicity two. Independent audit: not performed.
