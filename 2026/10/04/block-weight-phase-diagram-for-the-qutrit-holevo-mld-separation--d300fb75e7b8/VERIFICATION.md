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

The result is proved symbolically in `RESULT.md`. The key universal checks are:

1. For \(W>0\) and a real symmetric slack \(X\), the Hermitian \(2\times2\) constraint at parameter \(\beta\) is equivalent to \(X\ge0\) and \(\det X\ge\beta^2r^2\).
2. The sharp inequality \(\operatorname{Tr}(WX)\ge2\sqrt{\det W\det X}\) is attained by \(X_\beta=\beta r\sqrt{\det W}\,W^{-1}\).
3. The resulting fixed-family cost is the concave quadratic \(a+b+h+2\beta r\sqrt D-h\beta^2r^2\), whose exact supremum has the two stated regimes.
4. The joint minimizer \(X_*=r\sqrt D\,W^{-1}\), together with \(\kappa V_{33}=1\) and zero cross-block entries, satisfies every family constraint because the first-block determinant is \(r^2(1-\beta^2)\) and the third slack is \(\beta^2r^2\).

`verify.py` checks these identities numerically on deterministic positive-definite weights, including both optimizer regimes and nonzero within-block coupling. Its dense grid is a regression check only; the universal proof is the analytic argument above.

Unproved limits: no formula is claimed for weights coupling the third parameter to the first two, and finite-copy attainability is not established here.
