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

# Verification details

The standalone `verify.py` enumerates the Alexander dual and each alleged free-face pair, independently of the closed-form count. It checks graph hypotheses and edge/triangle/tetrahedron incidences, simulates elementary collapses, and verifies the connected one-dimensional remnant. Its finite tests include Möbius ladders from eight through twenty-four vertices, five open ladders and a disconnected graph. The first two Möbius instances receive an independent mod-two cut-complex boundary calculation. Output: `VERIFY_OK`.

The infinite theorem is established by the explicit collapses and Alexander duality in `RESULT.md`, not by these finite computations. Published-source comparison cannot guarantee universal priority, and no independent audit has occurred.
