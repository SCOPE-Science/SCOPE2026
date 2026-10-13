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

The proof is exact and analytic. The model reduces to one common first-failure waiting time plus one mutually exclusive survivor residual. From that representation, the covariance is the variance of the common waiting time minus the product of the two mutually exclusive add-on means. The two marginal variances follow from exponential second moments.

The Pearson denominator was re-expanded in the heterogeneity variable \(s=r+r^{-1}\), giving
\[
1+c^2(s^2+2s-2)+c^4(5+2s),
\]
whose derivative is \(2c^2(s+1+c^2)>0\) for \(c>0\) and \(s\ge2\). The published Kendall formula has denominator \(c(c+1)s+2c^2+2c+1\), also strictly increasing in \(s\).

Checks against established cases: at equal rates the Pearson formula is exactly \((1-c^2)/(1+3c^2)\), matching Li and Li's Proposition 4.2; both dependence coefficients tend to zero as \(c\uparrow1\) and to one as \(c\downarrow0\) for fixed positive rates. The proof does not rely on these boundary checks.

Unproved limits: no claim is made for nonexponential component lifetimes, unequal decelerating factors, more than two components, or dependence measures other than Pearson correlation and the displayed Kendall coefficient.
