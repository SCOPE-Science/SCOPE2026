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
# Verification

The standalone script `verification/check.py` derives all finite-household expected final sizes using the exact binomial transition recursion rather than evaluating the asserted polynomials as an input. It symbolically verifies six \(E_k\) formulae, the two comparisons at equal local probability, the strict derivative-ratio identity, the upper calibration bracket, and the precise binomial-mixture formula.

Positivity over a **continuum** of parameters is certified analytically using explicit Bernstein-basis coefficients of three polynomials on \([0,1]\). All coefficients are exact strictly positive rationals and are independently reconstructed by the checker. No finite grid enumeration is substituted for this argument.

The script also brackets the unique calibrated \(g\) for \(p=1/2\) in the interval
\[
\frac{525741}{1000000}<g<\frac{525742}{1000000}
\]
using exact rational evaluations, and checks the strict response gaps at both bracket endpoints. This isolated numerical witness is a reproducibility aid, not the basis of the universal theorem.

To run from a directory containing this package, install the declared dependency and execute `python verification/check.py`; successful replay prints `VERIFY_OK`.
