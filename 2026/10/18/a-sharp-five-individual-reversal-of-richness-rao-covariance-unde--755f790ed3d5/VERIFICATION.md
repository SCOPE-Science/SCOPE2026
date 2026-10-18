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

The finite-population theorem is proved by complete abundance-profile case analysis through four individuals, an exact omission-count identity for every integer \(r\ge2\), and algebraic specialization to ultrametric distances. The computation independently corroborates these claims without asserting that finite trials prove infinite statements.

Run `python check.py > reproduced.json`, then compare `reproduced.json` byte-for-byte with `certificate.json`. All routines use Python's standard-library `fractions.Fraction`, `itertools`, and `math.comb`, and enumerate equally likely labeled-individual subsets. The certificate documents 65 nonnegative small-population dissimilarity-basis tests, 40 general distance comparisons, and 150 ultrametric comparisons. The precise five-individual covariance sequence is also reproduced.

The conventional empirical Rao statistic weights ordered pairs with replacement and differs from the pairwise-unbiased statistic by the positive constant \((m-1)/m\) at each fixed \(m\); this preserves covariance signs but not numerical magnitudes. The closed-form criterion is restricted to the specified abundance profile and the next-to-census sample. Bibliographic completeness and independent validation remain outside the present verification evidence.
