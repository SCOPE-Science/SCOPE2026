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

Run `python3 verify_six_obstructions.py` in a Python 3 installation with no additional packages. The program prints `VERIFY_OK` upon success and raises an assertion on any disagreement. It enumerates every one of the 65,536 labeled bipartite edge sets on four left and four right vertices, checks whether a mixed two-vertex cover exists, checks containment of one of six specified forbidden patterns, and enumerates all inclusion-minimal failures. It also verifies both formula counts on complete rectangles with one through four vertices per side. Expected minimal failures on four by four: 96 with three edges, 396 with four.

The computer enumeration is finite and does not certify all graph sizes. The direct mixed-cover and matching proof in RESULT.md supplies the general theorem. No independent audit or formal proof-assistant certification has been performed.
