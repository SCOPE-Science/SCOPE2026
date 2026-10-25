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

# Verification of the finite certificate

Execute `python3 verifier.py` with `certificate.json` alongside. The actual embedded code recomputes the original graph, its all-pairs shortest-path metric, and every candidate simplex from the 14-vertex universe. The certificate contains precisely 68 ordered codimension-one free-face pairs, all checked against the current complex rather than an earlier face list. The output confirms 245 initial faces, the final f-vector (14,51,44), eight five-/six-cycle fundamental loops of an actual spanning tree, and mod-two ranks 13 and 38. These checks were executed on the actual packaged code and certificate. The finite-field ranks are supplementary: the integral homotopy classification relies on the proof of simple connectivity and explicit collapses. No Lean proof, independent audit or external certification is claimed.
