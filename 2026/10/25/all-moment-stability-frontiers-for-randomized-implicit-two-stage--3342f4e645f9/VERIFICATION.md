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

# Reproduction and boundaries

Run `python VERIFY.py` with Python 3.10+ and `mpmath` available (`python -m pip install mpmath` if necessary). The verification script prints `PASS 272 independent exact/numerical checks` when successful; its checks include exact rational equality of the two scalar updates, transformed-density normalization, inverse CDF, finite-difference agreement with the analytic moment derivative, the first/second moment closed forms, and numerical roots with strict order tests.

Exact statements for all real \(p>0\) are proved by the symbolic derivations and limiting arguments in RESULT.md. Numerical root finding at a finite selection of exponents and near asymptotic regimes does not certify the infinite assertions. In particular, the logarithmic-tail expansion uses an analytic uniform-integrability estimate, not an empirical fit.

The older second-moment threshold is a reference consistency check and not a newly claimed priority result. The proof assumes scalar autonomous decay, uniform iid stage fractions, exact implicit stage solutions, and exact arithmetic. No independent scientific assessment has been performed.
