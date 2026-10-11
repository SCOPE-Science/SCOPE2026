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
# Verification

The proof was replayed from the definitions of decreasing rearrangement and the finite weak-Lorentz quasi-norm. For a unit vector in the source quasi-norm, the ordered coordinate bounds are \(x_k^*\le k^{-1/p}\). The exact appended-functional gauge is attained by ordering coordinates against the coefficient moduli and choosing matching phases.

For sufficiency, at each threshold \(k^{-1/p}\|x\|\) with \(1\le k\le n\), the appended coordinate is below threshold and at most \(k-1\) original coordinates can lie above it; at the last threshold \((n+1)^{-1/p}\|x\|\), the appended coordinate itself supplies one coordinate below threshold. Adding a coordinate cannot decrease the first \(n\) order statistics, so equality of quasi-norms follows.

For necessity, the phase-aligned extremizer has every original coordinate strictly above \((n+1)^{-1/p}\). Therefore an appended value above that threshold would make all \(n+1\) target coordinates too large. This proves the coefficient inequality without numerical enumeration.

The verification does not extend the statement beyond one appended functional, and it does not assert a classification of all nonsurjective isometries.
