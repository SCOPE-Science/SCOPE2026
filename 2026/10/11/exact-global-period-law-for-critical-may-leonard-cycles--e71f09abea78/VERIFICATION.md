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

# Reproduction
Use Python with SymPy and mpmath available; execute `python verify.py`. The script proves the central rational polynomial identity by exact symbolic reduction and compares four independently integrated real periods with the closed hypergeometric expression at 65-digit working precision. It also checks the first subleading asymptotic term at two small products. The script is a finite reproducibility check, not an exhaustive proof of period monotonicity, and no independent audit has been performed. See RESULT.md for the analytic all-parameter argument and exact domain.
