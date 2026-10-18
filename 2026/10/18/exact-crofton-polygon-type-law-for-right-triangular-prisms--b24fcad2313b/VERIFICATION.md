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

# Reproducibility

Run `python3 verify.py` from the directory containing the extracted files. The program is self-contained and needs only the Python 3 standard library.

It reconstructs the finite six-direction support-order decomposition and its elementary antiderivatives for multiple equilateral and scalene triangles. It compares them with independent numerical integrations on 32 geometry/height pairs. It then independently partitions cutting offsets at the six vertex heights and evaluates all nine edge-crossing signs, verifying the proposed pentagon offset interval for 3,600 directional cases. Finally it samples 180,000 motion-invariant random affine planes using a uniform spherical normal and an **unconditional** uniform offset in a constant encompassing interval, retaining only intersections; that sampling step is essential to avoid a biased distribution. The deterministic seed yields 78,827 intersections, and all checks pass.

Finite tests are not a substitute for the exact full-domain proof in `RESULT.md`. The complete mathematical proof uses only edge-crossing identities, projection intervals, the planar Cauchy width formula, and a verified elementary antiderivative. There has been no independent expert audit, and inaccessible historic sources impose a priority limitation.
