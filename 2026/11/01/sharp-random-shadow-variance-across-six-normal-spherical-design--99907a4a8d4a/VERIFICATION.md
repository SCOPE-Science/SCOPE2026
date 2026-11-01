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

# Reproducibility

Execute `python3 verify_brightness.py` from the extracted files. The Python 3 standard library is the only dependency. The program independently computes normal balance and second moments for five twists, numerically integrates brightness and squared brightness over the viewing sphere, compares their difference with the analytic closed formula, and evaluates both exact endpoints. It also tests the dot-product ordering at 299 interior parameter values. The checker output on 2026-10-25 included the literal word `PASS` and a computed range of `0.030694143418` to `0.101940050221`.

The numerical integral has finite resolution (240 latitude bands by 720 longitude points). Its tolerance is stated in the code and is intended as a finite consistency test, not a mathematical certificate. The universal classification, strict monotonicity and equality characterizations are proved analytically in RESULT.md via a rank-two projection, a self-inversive polynomial, the two-point spherical absolute-value integral, and strict majorization.

# Scope and external checks

The initiating mathematical paper is arXiv:2608.11570, first submitted August 12, 2026. A later directional-kernel paper arXiv:2609.05869 and published comparisons about variance of shadows of Platonic solids are described in REVIEW.md and AUDIT.json. These comparisons do not constitute an exhaustive world-literature novelty certificate. Independent audit has not been performed.
