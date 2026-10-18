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

# Verification record

The proof is the five-step analytical argument in `RESULT.md`, not a numerical extrapolation. Run `python3 schwarzian_check.py` with `mpmath` installed to reproduce the five high-precision comparisons. Its most delicate identity, the exact negative-Schwarzian formula, was independently checked at five positive parameter/state configurations by 50-digit numerical differentiation, with relative residual below \(10^{-44}\). The strict analytical estimate uses \(0<R_\gamma(t)<1/2\), so it holds for every permitted parameter, not just the sampled values.

Running `python3 opacity_map_verify.py` using only the Python 3 standard library returned:

`PASS 306 diagnostics; gamma=3,p2=30: critical p2=28.343173521868, p1-window=(1.149551999920,4.045507637619)`

The verifier checks the map derivative at a range of parameters and states, computes the unique slope maximum, checks the fixed-point parametrization, locates both critical \(p_1\) values, and compares direct iteration with the predicted fixed-point/cycle phase. The example values are floating-point diagnostics, not certified enclosing intervals. The proof covers uncountably many parameter values and all nonnegative initial states through the exact calculus and interval arguments, not enumeration. No independent external audit has been performed.
