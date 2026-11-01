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

# Deterministic verification

The executable `verify_truncated.py` requires Python 3.10+ standard library only. Run `python3 verify_truncated.py > verification_output.json` from the directory containing the files. The recorded output was obtained by actual execution; it was not inferred from a run of a different graph. The complete reconstruction checks 262144 masks by independent membership procedures, 69075 augmented faces, 34533 matching pairs, a full topological sort of 485088 Hasse incidences, nine precise critical masks and the exact integer Morse boundary. The determinant -1 minor is at zero-indexed rows 1 and 4. Full independent simplicial mod-two ranks corroborate the degree-eight rank five. The signed Lefschetz action uses every one of the 24 label permutations and all invariant faces.

The exact method proves the finite, integral, non-equivariant sphere-wedge homotopy type; the symmetry character is over the rationals. No unperformed external audit or infinite certification is implied. A successful run prints `TRUNCATED_TETRAHEDRON_TWO_MATCHING_INTEGRAL_S4_VERIFIED` as a marker in its JSON output.
