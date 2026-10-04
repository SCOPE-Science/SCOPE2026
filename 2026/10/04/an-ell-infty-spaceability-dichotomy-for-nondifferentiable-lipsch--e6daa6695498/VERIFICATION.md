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

The proof was checked symbolically from the stated quasi-norm inequality and the focal differentiability characterization.

For the explicit embedding \(T\), the same-support calculation gives the exact block Lipschitz constant \(|a_n|L\). For different supports, zero boundary values reduce the difference to two within-block increments, and one quasi-triangle estimate yields the global upper bound \(\kappa L\|a\|_\infty\). Hence
\[
L\|a\|_\infty\le\operatorname{Lip}(T(a))\le\kappa L\|a\|_\infty.
\]
This verifies injectivity, continuity, bounded inverse on the range, and closedness of the range.

For any nonzero coefficient sequence, one coefficient is nonzero. On that support interval, differentiability of the image curve is equivalent after affine rescaling and multiplication by a nonzero scalar to differentiability of the seed curve. The seed has no differentiability point, so the image curve fails differentiability throughout that interval.

The argument does not rely on finite sampling, numerical approximation, or an unverified exhaustive search. Literature searches support noncoverage but do not constitute a proof of absolute novelty; the remaining terminology risk is recorded in the review.
