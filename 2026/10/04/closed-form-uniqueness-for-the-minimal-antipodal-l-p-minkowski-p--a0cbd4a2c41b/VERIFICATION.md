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

The proof was replayed algebraically from the formulas in `RESULT.md`. The critical checks are: the box-coordinate reduction under \(y=Ux\); the facet Jacobian \(|\det U|^{-1}\); the equal area of opposite facets; the mass equations \(\alpha_i^\pm=(a_i^\pm)^{1-p}A_i\); and the product identity that gives the unique positive scale with exponent \(n-p\).

The standalone `verify.py` was executed from its packaged path. It checks two nonorthogonal cases, in dimensions \(2\) and \(3\), with unequal opposite masses. It reconstructs the facet areas and reports maximum mass residuals below \(4\times10^{-15}\), ending with `VERIFY_OK`.

The computation is not an exhaustive or symbolic proof of the all-dimensional theorem. The infinite claim is justified by the analytic derivation in `RESULT.md`. No uniqueness is asserted for supports larger than \(n\) antipodal pairs.
