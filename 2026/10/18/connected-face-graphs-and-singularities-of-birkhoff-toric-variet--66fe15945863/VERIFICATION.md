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

The standalone program `verify_birkhoff.py` enumerates all coordinate-facet intersections of the \(3\times3\) and \(4\times4\) Birkhoff polytopes, canonicalizes support graphs, and independently checks singular-face inclusion maximality and the ray-excess formula. It additionally checks the all-rank closed component counts and block codimensions for \(3\le n\le7\). The program requires only the Python 3 standard library and prints `VERIFY_OK` when all assertions pass.

Observed results: \(B_3\) had \(49\) nonempty faces and \(9\) maximal disconnected-support faces; \(B_4\) had \(7443\) nonempty faces, \(658\) disconnected-support faces, and \(34\) maximal ones, with component dimensions \(4\) (\(16\) components) and \(2\) (\(18\) components). This program does not certify the infinite theorem or the novelty claim. The infinite theorem is supported by the integral lattice exact-sequence proof in RESULT.md. No independent audit has been performed.
