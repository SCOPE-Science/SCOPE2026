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
# Verification notes
The analytic proof uses the exact sector-pair visibility and sample bounds of arXiv:2610.03657v1. The key checks are: (i) the local scaled photon-number law for squeezed vacuum, (ii) endpoint control in the sector-pair Riemann sum, (iii) positivity of the limiting integral for fixed \(c>0\), (iv) the source validity condition for fixed \(c<1\), and (v) Stirling reduction of the classical bound to the rate \(I(c)=c-1-\ln c\).

The standalone checker evaluates finite instances for several fixed values of \(c\) and confirms convergence toward the integral and the classical exponent. Those computations are corroborative only; no finite enumeration is used to prove an infinite asymptotic statement.
