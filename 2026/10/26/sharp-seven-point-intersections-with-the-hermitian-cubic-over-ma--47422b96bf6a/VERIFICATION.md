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

## Exact arithmetic checks

Two standalone scripts reconstruct the same 180 sharp companions using different exhaustive search spaces. `verify_exhaustive.cpp` checks all 349525 ternary cubic coefficient classes, rational-point incidence and linear divisors. `verify_linear_algebra.py` checks the 36 rank-three nullspaces for seven-point constraints, the 16 candidate forms per omitted pair, the five non-line-factor companions, rational-point distributions and common tangent counts. Both were executed to successful terminal assertions and output markers.

## Mathematical checks and limits

The complete-intersection identities give the nine-point Cayley–Bacharach obstruction, and the factorization of every non-Hermitian pencil member excludes nine-point integral cubics. A direct all-characteristic singularity calculation proves smoothness of the displayed witness. The elementary classification of geometric cubic factor patterns and singular cubic normalization proves that the five companions found in each pair are smooth. Bézout and the absence of degree-two points on the maximal Hermitian elliptic curve reduce the seven-point contact divisor to two possible patterns; the tangent-gradient checker distinguishes them. Arithmetic checks alone do not replace the geometric arguments, and no independent external audit or validation is asserted.
