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

# Reproducibility and limits
Run `python3 VERIFY.py` (Python 3.8+, standard library). A successful run ends with `RADIUS_THRESHOLD_CERTIFICATE_OK` and checks every one of the finite-state edges in the claimed radius-one, radius-two and radius-three transfer graphs. The critical radius-three target has one 17-vertex, 18-edge cyclic strongly connected component, phase-zero vertex identifiers 41 and 49, and ten-step core return matrix `[[1,1],[1,1]]`. The ring-level simulation covers the explicit lengths listed in `RESULT.md`; infinite-family proofs additionally require the transfer-graph correspondence and the trace argument stated there. `VERIFY_OUTPUT.txt` is a record of the actual run, not a substitute for the code and finite-state proof.

The source-specific published claims were compared at statement and implication level. The experiment does not establish claims about arbitrary initial configurations outside the specified one-step inverse images. Independent audit has not been performed.
