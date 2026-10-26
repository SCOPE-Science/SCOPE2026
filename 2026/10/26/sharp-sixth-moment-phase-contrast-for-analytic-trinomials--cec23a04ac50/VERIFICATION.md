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
# Reproducibility and scope of verification

Install the dependency given in `requirements.txt`; execute `python artifacts/verify.py` from the root of the extracted package. The output recorded in `artifacts/check_output.txt` is:

```
VERIFY_OK exact_identities=5 quadrature_cases=5 root=2.680722225499 sharp_moment_ratio=3.797737522475 sharp_norm_ratio=1.249072051421
```

The standalone checker verifies the degree-six Parseval expansion; exact symbolic normalization using the endpoint asymmetry variable; the derivative sign-polynomial identity; the factorization on the equal-endpoint locus; the quartic derivative; and numerical root uniqueness. It independently evaluates five normalized Fourier integrals on an 8192-point grid, comparing each with the moment expression. The proof in `RESULT.md` establishes every degree-independent and all-coefficient conclusion; finite quadrature is not an exhaustive or infinite proof.

The verifier requires Python 3 and a compatible SymPy installation. No external certificate or independent expert audit is represented by these checks.
