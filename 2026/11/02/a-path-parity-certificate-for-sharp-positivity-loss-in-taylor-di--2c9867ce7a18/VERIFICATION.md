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

The linear-algebra proof uses the binomial identity for the degree-\(s\) exponential Taylor polynomial and the nonnegativity of alternating exponential partial sums on \([0,1]\). The walk-gap hypothesis eliminates every polynomial power except the \((s-1)\)-st, whose coefficient is \(1-dh\).

`python verify.py` was run on the actual package code using the Python standard library. The result was `VERIFY_OK cases=29 exact_assertion_groups=698`. All numerical matrix calculations use rational arithmetic, and assertions check the exact witness identity, row sums, and signs. This finite replay does not independently certify the arbitrary-order mathematical argument, prove bibliographic uniqueness, or test every possible graph.
