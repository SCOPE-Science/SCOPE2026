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

# Verification record

The analytic argument proves the exact probability law. The standalone `verify.py` reconstructs all hyperplane-cube edge intersections using exact rational arithmetic (no geometry library), determines the number of vertices and all positive-dimensional coordinate facets, and compares with the claimed three profiles for every generic strictly increasing four-tuple chosen from integers 1 through 16. It checks the explicit orthogonal reflection and the fact that the reflected normal belongs to the opposite nondominant chamber. It also checks the elementary Cauchy angular integral numerically and uses 75,000 seeded Gaussian samples as a non-certifying empirical sanity check. Replaying the file directly extracted from the embedded JSONL record printed `ALL_FOURCUBE_THREE_TYPE_CHECKS_PASSED`.

The proof does not infer exact measure from sampling or from the finite enumeration. Instead, it derives the exact dominant probability through the Gaussian/Cauchy edge-crossing probability and derives the exact nondominant probabilities through a measure-preserving involution. Rational enumeration checks representative incidence tables, while the analytic sign-chamber argument extends those tables to all generic directions.

The checker requires Python 3 with standard-library `fractions`, `itertools`, `collections`, `math`, and `random`. Independent assessment remains unperformed. Historical priority remains provisional, particularly for potentially unindexed stereological distributions.
