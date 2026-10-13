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

Run `python verify.py` with Python 3 and NumPy (tested with 2.3.5) from the package directory. The verifier enumerates all spin configurations on paths of lengths 3 through 11 to compute the fugacity polynomial, compares its roots with the analytic circle threshold, independently compares transfer-matrix traces with the Chebyshev expression at complex fields, and checks threshold collision multiplicities. Observed output:

`VERIFY_OK numerical_zero_loci= 135 transfer_identities= 135 boundary_multiplicities= 27 numpy= 2.3.5`

The mathematical proof is in RESULT.md. Finite floating-point checks do not establish the assertion for every length and real parameter. No external or independent audit is reported, and the original Chebyshev partition expression is attributed to antecedent literature.
