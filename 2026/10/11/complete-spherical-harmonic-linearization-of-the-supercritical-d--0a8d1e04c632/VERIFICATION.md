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

The proof is analytic. The standalone script `artifacts/verify.py` checks exact combinatorial identities used in the derivative of the curvature quotient and the degree-zero/degree-one spectral reductions over a finite parameter grid.

Critical checks reconstructed from the stated equations:

1. At \(u\equiv R_*\), stationarity is exactly \(f_0R_*^{\alpha-k-1}=1\).
2. At the isotropic curvature-radius tensor, \(DG[\eta]=-(k\beta/n)R_*^{-k-1}\operatorname{tr}\eta\).
3. Therefore \(D\mathcal F=(k\beta/n)\bar\Delta-\beta(\alpha-k-1)\).
4. Degree zero gives the source's homothetic exponent \(\beta(\alpha-k-1)\); degree one gives \(\beta(\alpha-1)\), hence the exact gap \(\beta k\).

The finite script checks do not certify the infinite-dimensional spectral statement; that statement follows from the symbolic linearization and the standard spherical-harmonic spectrum.
