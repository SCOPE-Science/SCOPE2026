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
The proof was replayed symbolically from the norm definition.

For the lower bound, one active quadratic branch was selected at each unit vector. Equal branches cancel their linear cross terms exactly. In a mixed strip/Euclidean pair the possible negative linear coefficient reduces to a single constrained function of the Euclidean vector's first coordinate. Its unconstrained maximizer is the round-boundary coordinate \(q=\sqrt{1-\lambda^{-2}}\); comparison with the admissible cap \(1/\lambda\) gives the exact transition \(\lambda=\sqrt2\). The quadratic remainder in this lower estimate is nonnegative.

For the upper bound, the comparison pairs are chosen strictly inside the flat and round pieces of the unit sphere, so the active branches persist for sufficiently small positive \(\tau\). Sending those points to the appropriate boundary recovers the lower coefficient. Thus no nonsmooth directional-derivative identity at a corner is assumed.

Limits: the result proves only the right derivative and the corresponding \(o(\tau)\) expansion. It does not certify the full function for small positive \(\tau\), classify its minimizers, or provide an independent audit.
