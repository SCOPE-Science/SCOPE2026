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

The theorem is proved analytically in `RESULT.md`. The included `verify.py` is a consistency replay only. It checks representative subcritical parameters, unit norms, the positive dependence, the determinant factor, all six spike-coverage inequalities, and the endpoint square-sum obstruction. Finite numerical checks are not used as evidence for the universal quantifier over \(r\).

Critical analytic checks are:

1. For \(1<r<\sqrt2\), \(c_r=\sqrt{1-r^{-2}}<1/\sqrt2\), so the required \(x\) exists.
2. The determinant equals \(s(3x^2-1)\), and the excluded value \(x=1/\sqrt3\) is exactly the only internal singular value.
3. The positive relation \(u_1+u_2+u_3+\sqrt3\,s\,u_4=0\) has strictly positive coefficients because \(s>0\).
4. At \(r=\sqrt2\), illuminating two distinct axial spikes would require two distinct coordinate squares to sum to more than one, contradicting unit norm.

No statement beyond the displayed family and parameter range has been verified. Independent audit has not been performed.
