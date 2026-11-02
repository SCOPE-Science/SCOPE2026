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

# Reproducibility and verification

The analytical proof is given in `RESULT.md`. The optional independent numerical diagnostics in `verify.py` use only Python's standard library and a deterministic random seed. Run `python3 verify.py` to check the exactly normalized unit-rate position density and variance, the inward-propulsion quadrature, and three direct simulations of the renewal representation. All twelve programmed numerical checks passed when executed from the packaged code.

The numerical values have rounding and Monte Carlo tolerance; they do not certify global originality, the local central limit theorem, or the small/large parameter limits. Those conclusions follow from the separately displayed analytic steps and explicitly stated assumptions. Independent audit is not performed.
