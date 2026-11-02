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

Run `python3 verify.py` from the directory containing this package. The code has no third-party dependency. Observed outputs: `EXACT_ROWS_OK 200`, `BETA_MOMENTS_OK 18`, `LOG_ROW_SCALE_OK 9`, and `ALL_CHECKS_OK`.

The 200 finite \(s=2\) row identities and harmonic-sum identities use exact `Fraction` arithmetic. The 18 beta moment checks and nine normalized row tests use midpoint quadrature with prescribed tolerances, and do not replace the analytic large-index or continuous-parameter arguments. The underlying proof is the coefficient-level calculation, regular-variation limit and uniform error bound, and classical Cesàro block estimates in `RESULT.md`.

Normalization example: the 0th output row of \(T_{2,0}\) contains the scalar \(1/2\), while its \(n\)-th row has square norm \((2n+3)/(6(n+1)(n+2))\). The normalized constant \(1/(2s-1)\) equals \(1/3\) in this case. Tests and stated bounds have not undergone independent review.
