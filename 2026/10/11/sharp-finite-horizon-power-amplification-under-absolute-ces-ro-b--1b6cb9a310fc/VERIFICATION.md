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
# Verification and limitations

The universal inequality follows by applying the \(p\)-absolute Cesàro bound to every trailing finite orbit window and multiplying the exact consecutive-tail ratios. The extremizer is a bounded nonincreasing positive weighted backward shift on standard \(\ell^p\), whose coordinate orbit sums equal \(K(j+1)\) for all \(j\ge1\), and whose power norm is the first \(n\)-weight product. The Gamma expression is a direct product identity; the asymptotic uses the classical Gamma quotient limit. All arguments are valid for real and complex \(\ell^p\) and every real \(K\ge1\).

`verify_finite.py` uses exact rational arithmetic, and tests \(K=1,5/4,3/2,2,7/2,17/3\) at sizes and horizons through eleven. The check explicitly verifies the coordinate means for longer and shorter horizons, weight monotonicity, and the power-product equality. The expected terminal output is `EXACT_FINITE_CHECK_OK for rational K and sizes 1..11`. These finite checks are supplementary, not evidence of an exhaustive infinite proof or novelty.

Scientific limitations: no uniqueness of maximizing operators, no quantitative stability statement, and no claim that all possible equivalent literature has been searched. Independent validation has not been performed.
