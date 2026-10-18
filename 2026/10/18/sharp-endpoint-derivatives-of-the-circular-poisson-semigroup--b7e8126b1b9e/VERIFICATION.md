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

Run `python checker.py` with Python 3.9+, SymPy and mpmath alongside `RESULT.md`. Actual package-path execution passed 72 algebraic, numerical quadrature, high-order cosine-constant and Taylor-series assertions. The exact symbolic checks independently differentiate the kernel and verify all cubic sign identities. Integral tests sample positive times before and after the third-derivative nodal threshold, and the first 12 sharp constants are independently compared with numerical integrals. Analytical proofs in RESULT.md, rather than finite tests, supply the universal statements for all positive times and derivative orders. No external validation or independent audit has been performed.
