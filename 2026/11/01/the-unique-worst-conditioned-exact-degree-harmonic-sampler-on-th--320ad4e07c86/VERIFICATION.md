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

Execute `python3 h3_cert.py` with a standard Python installation. The script uses exact rational pairs to represent \(\mathbb Q(\sqrt5)\), constructs the thirty vectors without external data, checks the degree-twelve spectral identities and exact rational root brackets, and uses a fraction-free Sylvester test on rigorous dyadic Gram enclosures for every needed degree below 500. It separately verifies the elementary rational inequalities supporting the integral/Legendre tail bound and reports `H3_ALL_DEGREE_CERTIFICATE_OK`. The exact signed Legendre recurrence and the matrix projection identities supply the nonstandard algebra. The analytic integral inequality, rather than finite calculation, handles all degrees at least 500.

Only the new scientific result has undergone self-review. Independent audit and external validation have not been performed.
