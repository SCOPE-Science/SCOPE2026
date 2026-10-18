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
# Reproducible checks and limits

The stand-alone `CHECK.py` uses only the Python standard library. Execute `python CHECK.py` in a directory containing the checker: it enumerates all allowable sign vertices for eleven disjoint-check profiles, including mixed block lengths, and verifies all coordinate first and second moments, vertex count, direct linear-objective maxima and the opposite-direction width-loss law for 176 integer test directions. It numerically integrates the half-normal minimum-tail function by Simpson quadrature and tests strict discrete curvature, the exact nine-dimensional balancing example, and rescaled first and second moment limits for block lengths up to 1000.

Successful output: `PASS: 176 exact support and directional-width tests; 11 vertex covariance profiles; convexity, extremal width and asymptotic moments`.

The normal limits, strict balancing for every partition, and the optimal-ball argument are proven in RESULT.md. Enumeration does not purport to exhaust all block lengths, prove asymptotics, or establish bibliographic uniqueness. The numerical first/second moment checks have only numerical precision; the mathematical derivation uses the tail integral and uniform exponential envelope. All constructions concern disjoint parity-check blocks of lengths at least three.
