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
# Reproducibility and verification

Run `python3 verify.py` from the extracted directory with Python 3 standard library. The script independently brute-force checks *cyclic periodic* antisquares for all binary words of displayed lengths 1 through 15. It also checks the bivariate rational generating function against the cyclic-gap binomial sum through length 19, enumerates the extremal one-third minority configurations for periods divisible by six through 114, and certifies rational bounds for the dominant root and positive Gaussian variance. Expected terminal line: `ALL CHECKS PASSED`.

The computational experiments do not establish the infinite theorem on their own. Its critical proof steps are the published minimal-antisquare and bi-infinite-word reduction, two-to-one difference coding, gap bijection, cyclic transfer-matrix log determinant and dominant-root quasi-powers argument. The primary article is available as arXiv:2209.09223; the cited definitions and nonstandard lemmas must be evaluated there.

There is no independently performed mathematical audit or independent validation in this package.
