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

The proof was checked symbolically from the stated definitions. For a general positive-definite quadratic form, the four coordinate-sign conjugates preserve the same lower and upper norm-comparison constants, and their average is diagonal. For a diagonal form the unit-sphere substitution \(t=|x|^p\) is exact and yields \(F_{a,b}(t)=a t^{2/p}+b(1-t)^{2/q}\). Because \(2/p\) and \(2/q\) lie strictly between \(0\) and \(1\), the endpoint minimum and unique interior maximum are global, not numerical approximations.

After normalizing the endpoint minimum to \(1\), both diagonal coefficients are at least \(1\), so every diagonal profile dominates the identity profile pointwise. At the identity profile’s interior maximizer, the domination is strict unless both coefficients equal \(1\), which proves uniqueness among diagonal forms as well as the global lower bound. For uniqueness, once sign averaging forces the diagonal part of any optimal quadratic form to be scalar, a nonzero cross term produces opposite perturbations at the same interior absolute-value pair; the larger sign exceeds the claimed optimum while axis values keep the minimum at most \(1\).

A numerical check for \(p=4\), \(q=6\) gives \(t_*\approx0.61978\) and squared distortion approximately \(1.51171647\), consistent with the formula. The numerical check is not used in the proof. The literature comparison is limited by possible terminology differences for mixed-power convex bodies, and no claim is made for exponent regimes outside \(2<p<q<\infty\).
