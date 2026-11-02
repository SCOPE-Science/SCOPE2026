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

Run `python verify.py` with `numpy` and `scipy` (versions described in `requirements.txt`). The checker performs an independent shoelace reconstruction of convex polygons from intersections of adjacent tangent lines, verifies the finite beta probability and the beta-edge density coefficient, and performs Monte Carlo checks for the finite-threshold tail in multiple parameter regimes. Its successful completion emits `ALL_CIRCUMSCRIBED_DIRICHLET_TAIL_CHECKS_PASSED`.

The numerical tests neither prove the \(t\to\infty\) asymptotic nor establish priority. Those require, respectively, the explicit corner-density integration and one-big-gap squeeze in `RESULT.md`, and comparison with earlier complete literature. The 2015 predecessor's full text was not available and remains a historical priority risk. No independent audit was performed.
