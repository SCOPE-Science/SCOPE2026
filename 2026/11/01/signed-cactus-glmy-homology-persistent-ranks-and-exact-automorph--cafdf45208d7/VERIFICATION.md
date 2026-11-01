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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3.10+ and no third-party packages. It reconstructs low-degree signed GLMY regular-path chain ranks using the signed double cover, independently computes the balanced-short-cycle quotient, enumerates cactus edge-filter stages, and tests symmetry characters. Expected terminal markers: `VERIFY_OK`, `SYMMETRY_OK`, `ALL_GRAPH_SHORT_CYCLE_OK`, `CACTUS_FILTRATION_OK`, and `FRIENDSHIP_SYMMETRY_OK`.

The computations cover 272 signed high-girth cases, 320 unrestricted signed-graph cases, 544 cactus filtration instances (480 adjacent stages), and 14 exact signed character comparisons. Ranks are computed modulo 1009; this tests the finite examples but does not establish the unrestricted real result. The proof in RESULT.md provides the unrestricted deduction. The automorphism-character comparisons involve exact integer traces, in conjunction with a prime-field nullspace calculation on tested examples. Independent audit has not been performed.
