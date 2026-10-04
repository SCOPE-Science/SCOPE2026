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
The symbolic proof is the primary correctness argument. The packaged checker reconstructs finite weak orders directly from level sizes, exhaustively enumerates all order-preserving maps in six representative unequal-height cases, checks the image-level dichotomy used in the proof for every map, and computes connected components in the pointwise-comparability graph of each finite function space.

The replayed cases include target levels of unequal sizes. Every tested map either has a singleton occupied target level or has exactly one distinct two-point image level for each binary source level with an unused target level when the source height is smaller. Each tested mapping space has one comparability component.

The finite computations are sanity checks only. They do not replace the all-heights proof, and no claim is made for source levels larger than two or for equal source and target heights.
