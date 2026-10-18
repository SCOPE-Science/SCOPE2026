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

Run `python verify_face_downsets.py` with the Python standard library. Expected output is provided in `verification_output.txt`. Its three finite examples check short-additive encoding, local clamp validity, an exact signed top-cycle boundary, and an integer determinant cocycle; no randomized algorithms, approximate ranks, or unrecorded external data are needed.

The entire universal claim follows from the three exact proof stages: faithfully encoded two-step relations, integral acyclicity of the marked lattice cover, and the resulting free deck-group resolution. The finite output supports those steps but is not a proof for arbitrary parameters. An independent audit and external certification have not been performed.
