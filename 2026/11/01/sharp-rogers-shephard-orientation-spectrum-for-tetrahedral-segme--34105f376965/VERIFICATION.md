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

The proof uses exact simplex-orthant volumes, all nonempty-subset facets of the two-sided simplex, Cauchy's projection identity, and a complete sign classification of four zero-sum barycentric derivatives. The standalone `verify.py` checked the derived volume formula independently by numerical convex hulls of explicit vertices/differences, together with rational algebra and sharp-orientation witnesses. The checked invocation `python verify.py` printed: `PASS: 486 independent polytope-volume / exact-rational / equality checks`.

The computations have finite coverage and do not certify the analytic claims for every extrusion. In particular, equality and completeness of the interval rely on the sign argument in `RESULT.md`. Historical priority remains subject to unindexed and inaccessible literature. Independent audit has not been performed.
