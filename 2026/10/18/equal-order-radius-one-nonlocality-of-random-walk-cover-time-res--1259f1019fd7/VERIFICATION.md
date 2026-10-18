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

# Reproducible verification

Run `python3 verify_cover.py` in the directory containing this file. The script requires only the Python standard library and checks both eleven-vertex tree edge lists, the three marked pairwise distances, rooted ambient-degree radius-one balls, and the exact pre/post insertion expected cover times.

It calculates each value twice: by decreasing visited-subset size and solving first-step equations over `fractions.Fraction`, and independently by target-set inclusion-exclusion of exact first hitting times. Its success terminal message is `VERIFY_OK: two independent exact rational cover-time methods agree`.

The complete exact signed changes are \(-1162717427/813580152\) and \(3127/83076\). The verification is exhaustive for these four finite graphs, not for all eleven-vertex trees or all graph orders. It does not establish minimality or extend to neighborhood radius two or greater.
