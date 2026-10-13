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

## Verification record

The standalone `verify.py` enumerates all ordered pairs of elements of the specified square-zero quiver algebras over the prime fields of orders two and three, computes every target coefficient using direct multiplication, and compares the resulting fibers with both the independently evaluated coloring sum and the complete subset expansion. It confirms the exact width jump for complete-graph quivers on four, five, and nine vertices over the binary field; the general width theorem is symbolic, not inferred from these examples.

Running `python verify.py` from the package directory ends in `VERIFY_OK`. The tests include a two-arrow Kronecker quiver, a three-vertex path, a three-vertex oriented cycle, and a single-arrow algebra. They do not test extension-field arithmetic directly, large arbitrary quivers, or the general infinite family; those claims are established by the proof in `RESULT.md`.

The scientific premises are the explicit arrow-basis multiplication and the independence of arrow radical variables when the arrow ideal squares to zero. The absolute value of the graph-polynomial sum is not used to infer existence: existence follows instead from the nonnegative coloring expression. No independent audit has been performed.
