---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For monotone f between h-level ordinal sums of antichains, successive source level image intervals cannot be inverted. A boundary overlap forces the shared target-level image to be a singleton; if every occupied target level had >=2 images, h strictly separated nonempty intervals must occupy exactly h target levels, so f(A_i)⊂B_i and each restriction has >=2 distinct values. If some occupied target-level singleton b exists, the entire image is pointwise-homotopic to constant b via collapse maps, making f null. A level-preserving nonconstant f has no distinct map pointwise above or below it, by backward and forward induction using >=2 target images on adjacent levels. Thus special maps are isolated, with count ∏(q_i^{p_i}-q_i); remaining maps form the constant class since Q connected. Order complexes are joins of levels and induced top homology rank is ∏(|f(A_i)|−1). Independent exhaustive mapping-comparability enumeration P=(2,2,2) to Q=(2,2,3) verified 755 maps, 25 components and 24 special isolated maps.

## originality

PASS

No independent published covering implication was located under the checked exact and equivalent formulations.

## value

PASS

Provides a genuine infinite parametric off-diagonal classification not included in self-map or height-two results, and simultaneously computes component count and top-homology ranks. These are structural invariants natural to homotopy theory of finite weak orders, not merely a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
