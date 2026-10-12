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

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The delivered `verification_output.txt` records the actual successful execution. The code independently finds exact least values in all residue classes by Dijkstra's algorithm on the standard finite generating range for seven sample parameters, verifies the closed formula and the unique maximum residue, and checks explicit boundary representations and binary-weight identities. The semigroup's infinite family of generators and all admissible coefficients and exponents are handled **mathematically** by the proof in `RESULT.md`, not by finite enumeration. Finite tests cannot independently establish an infinite identity or bibliographic uniqueness.
