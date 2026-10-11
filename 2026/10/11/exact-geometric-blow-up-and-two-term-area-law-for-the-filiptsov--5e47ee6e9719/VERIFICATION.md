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

# Reproduction and limits

Run `python3 verify_filiptsov_area.py` using Python 3 standard library. The script checks by rational arithmetic the two coefficients of the polynomial surrogate for the exact scaled area integral, the limiting coordinate maxima, and numerically evaluates the exact finite-parameter integral for three positive parameters. Output `CHECK_OK` indicates these diagnostics passed.

The proof in `RESULT.md` independently establishes the positive-root domain, exact integral, uniform error estimates, Hausdorff limit, and maxima for all \(0<a<3/13\). Finite quadrature cannot establish asymptotics by itself. The historical 1973 article was not available for a conclusive priority audit, and independent assessment has not been performed.
