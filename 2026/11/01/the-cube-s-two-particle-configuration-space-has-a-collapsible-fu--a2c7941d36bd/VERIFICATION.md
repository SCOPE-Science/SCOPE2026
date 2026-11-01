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

# Verification record

Run `python3 verify.py` with `certificate.json` in the same directory, using Python 3 standard library only. The checker regenerates the cube graph, the full 48-element signed-coordinate-permutation group, the cubical two-particle model, all barycentric flags, their group orbits, the entire quotient incidence table and every proposed elementary collapse. This run succeeded with `CUBE_CONFIG_QUOTIENT_VERIFY_OK`, and the recorded stdout is `verification_output.txt`.

The checker establishes exact finite incidence arithmetic, not the continuous configuration-space retraction. The latter is proved separately in the `RESULT.md` proof by a continuous, particle-swap- and graph-automorphism-equivariant barycentric homotopy. Its coefficient identity rules out collisions for every homotopy parameter. All claimed results are self-reviewed; no independent audit was conducted.
