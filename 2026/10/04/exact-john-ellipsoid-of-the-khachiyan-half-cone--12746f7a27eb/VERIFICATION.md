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

The claim is verified by an exact reduction rather than numerical optimization.

1. Uniqueness of the John ellipsoid and \(O(n-1)\) symmetry force an optimizer of the form \(ce_1+\operatorname{diag}(a,b,\ldots,b)B_2^n\).
2. The axial constraints are exactly \(a\le s\) and \(a\le1-s\), where \(s=-c\).
3. The conic boundary is the intersection of the linear halfspaces \(t+\sqrt{n^2-1}\,z\mathbin{\cdot}y\le n\), so exact support-function evaluation gives
\[
b^2\le\frac{(n+s)^2-a^2}{n^2-1}.
\]
4. The logarithmic derivative in \(a\) is strictly positive throughout the feasible interval. After setting \(a=\min\{s,1-s\}\), the logarithmic volume derivative is strictly positive for \(s<1/2\) and strictly negative for \(s>1/2\).
5. Therefore the unique maximum is \(s=1/2\), \(a=1/2\), \(b=\sqrt{n/(n-1)}\). This reproduces the source's \(E_n\) and yields the stated determinant ratio.

The inspected recent source independently verifies \(J(K_n)=B_2^n\). No finite experiment is used as a substitute for an infinite-dimensional or all-\(n\) argument.

Limit: originality against every historical source is not mechanically certifiable. The original 1988 Russian paper was not independently inspected line by line; the recent source's detailed attribution describes it as containing the cone limit rather than the exact half-cone maximality proved here.
