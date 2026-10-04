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

The accompanying `verify.py` uses high-precision arithmetic to replay the saved formulas without relying on any external package. It checks:

- the exact radical formula for \(t_*\) satisfies \((3\sqrt3-2)t^2-2t+\sqrt3-2=0\);
- \(t_*\) lies in \((2-\sqrt3,1)\), and the derivative numerator changes sign across it;
- \(\lambda_*=L(t_*)\) agrees with the stated decimal;
- a strictly interior point near the optimized isosceles apex gives negative defect at \(\lambda=0.58<\lambda_*\);
- a strictly interior point in a slender right triangle gives negative defect at \(\lambda=2.01>2\);
- the scaled right-triangle boundary defect approaches \((2-\lambda)(1-q)\) numerically.

The computational checks are not an exhaustive search and do not certify validity anywhere inside \([\lambda_*,2]\). The analytic proof in `RESULT.md` supplies the quantifiers for every \(\lambda<\lambda_*\) and every \(\lambda>2\).
