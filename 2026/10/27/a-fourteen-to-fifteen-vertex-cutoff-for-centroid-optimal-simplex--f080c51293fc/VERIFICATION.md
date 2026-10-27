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

# Verification notes

The checker `verify_barycentric.py` uses only `fractions.Fraction`. It embeds explicit positive rational weights for every face rank for each integer from three to fourteen original vertices. It checks normalization, nonnegativity, and every possible nonidentical pair orbit indexed by subset sizes and intersection cardinality. The canonical KR formula on equilateral vertices and exact Euclidean squared-distance identity reduce the operator bound to a rational inequality. All 1,489 cases passed, including exactly 12 forced vertex–centroid equalities. There are no randomly sampled cases, numerical inequalities, or unverified solver optimizations in the final certificate.

The all-integer obstruction for at least fifteen original vertices is an analytical argument: permutation averaging plus explicit vertex–seven-face and seven-face–centroid test functions, followed by the exact equivalence of strict dominance to `n > 672/47`. The checker independently confirms the two bracketing rational comparisons at 14 and 15.

Not checked: an exact formula for the unrestricted optimum when at least fifteen original vertices are present; all optimizers, other metrics, or Banach-valued target data. These are not asserted.
