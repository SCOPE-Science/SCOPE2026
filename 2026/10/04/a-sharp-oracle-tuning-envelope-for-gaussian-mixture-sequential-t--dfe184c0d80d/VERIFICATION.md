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

The source martingale formula was checked directly against Wang--Ramdas, Theorem 4.9 and equation (41). The proof then uses exact algebra and one-variable calculus. The decisive derivative identity is
\[
\frac{d}{dx}\log (G_n^{(\sqrt{x})})^2
=-\frac{n(n-1)(x(T_{n-1}^2-1)-n)}{x(n+x)(n(n-1)+(n-1+T_{n-1}^2)x)}.
\]
Its denominator is positive for \(n\ge2\) and \(x>0\), so all optimizer and boundary claims follow from the numerator sign.

`verify.py` checks the equivalent closed form against the source expression at multiple parameter values, checks the predicted sign change around the optimizer for \(T_{n-1}^2>1\), checks monotonicity toward one when \(T_{n-1}^2\le1\), and recomputes the \(5\%\) finite and limiting barriers. It uses no external packages.

The computation is supportive rather than an exhaustive proof over real parameters; the infinite-domain statement is established by the displayed symbolic factorization and monotonicity argument. No validity claim is made for selecting the maximizing precision from the same data.
