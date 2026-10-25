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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library. This checks gamma-normalized circular integrals and the two extrema of the candidate angular profile for a range of subquadratic exponents, random perturbations of positive weights and direction differences, and the necessary quantitative weight/angle rigidity implications. Numerical angular grids resolve only a finite sample; every infinite statement is proved symbolically in RESULT.md. The limiting sharpness over convex bodies follows from weak convergence of normalized surface-area measures of thin rectangles, not a numerical polygon sample.

The correctness, originality and mathematical value reviews were performed together with the derivation; these do not constitute an independent audit. The classical \(p=1\) result is previously published and is credited. An exact priority determination for all equivalent language in global literature is not certified.
