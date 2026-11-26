---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

After a common sign change and permutation the centered vector is (a,b,-c), c=a+b>0 and a≥b≥0. Convolving the two positive exponentials with the negative one yields the displayed positive-side divided difference and the negative-side exponential with coefficient c/((a+c)(b+c)). Differentiating u exp(-t/u)/(u+c) at fixed c converts the divided difference into a positive integral; integrating t^s gives the two powers of u with precisely the coefficients in (1) after division by Γ(s+1). The b=0 endpoint is integrable (the term u^{s+1} stays integrable with up to two logarithmic derivatives), and a=b uses the single derivative at a. Gamma duplication gives the claimed ratio. The two kernel curvatures are bounded below by 1/(2(s+2)) and 1/(2(s+2))−1/(s+1)^2, respectively, both positive at every s≥2. Differentiation of the positive mixture gives an average curvature plus the variance of its log-derivatives, so strictness holds on the full interval. For variance-normalized Y, Theorem 1 of arXiv:2602.03058v1, equation (6), applies at all real orders ≥2 and gives h(s)≥h(2)=0. Thus s h′(s)−h(s) starts nonnegative and strictly increases for s>2, giving strict growth of the norm ratio including comparisons with p=2. Replay: see RESULT.md, Steps 1–4, and the inspected verification/check_moments.py for optional finite diagnostics; its logged count is not an independent run or a continuum certificate.

## originality

PASS

Pass for the arbitrary centered three-coefficient statement, particularly genuinely asymmetric vectors, and the strict all-real-order curvature/ratio conclusion. The moment formula, one-order inequality, and paired-coefficient comparison are not new. No inspected relevant result already proves the unrestricted three-coefficient cross-order claim.

## value

PASS

This resolves the first genuinely asymmetric three-term class of a published two-order comparison problem, at all real orders in its proposed range, and proves the stronger curvature property. The positive density decomposition explains why the asymmetric case works without assuming the paired Gaussian-scale mixture; the finite number of terms does not make this just a finite order check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
