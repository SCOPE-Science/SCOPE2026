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

The finite verifier `verify_character.py` constructs the dodecahedral graph directly from its generalized Petersen coordinates and exhaustively enumerates its 5,828 independent sets and 120 graph automorphisms. It computes the reduced mod-two homology from exact bitset boundary ranks, and computes signed fixed-simplex Lefschetz traces for every automorphism. The recorded output `verification_output.txt` ends in `VERIFY_OK` and reproduces the complete character table.

The mathematical proof converts mod-two Betti bounds and the Euler characteristic into rational homology concentration, then uses the Hopf trace formula and equality of rational characters to establish the claimed module. The finite calculation does not identify the integral homology lattice or certify literature-wide originality; no independent audit has been performed.
