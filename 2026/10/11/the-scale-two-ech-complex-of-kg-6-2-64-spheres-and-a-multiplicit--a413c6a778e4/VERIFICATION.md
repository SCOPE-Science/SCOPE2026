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
# Exact finite verification

Run `python3 verify.py` using a Python 3 standard library. `VERIFY_OK` is emitted only if all assertions succeed. The program reconstructs all fifteen closed-neighborhood facets, the complete seven-entry face vector, 735 matched pairs, the remaining 65 critical faces, and all 5,985 codimension-one incidences. A topological sort of the oriented matching Hasse graph visits all 1,535 faces. Independently it calculates mod-two boundary ranks and confirms the Betti vector. It obtains the full eleven-class rational character by signed fixed-simplex enumeration and verifies its irreducible Specht decomposition by the Murnaghan–Nakayama rule.

The integral wedge claim uses finite discrete Morse theory and the absence of critical one-cells, not a mod-two-to-integral inference. The representation result is over the rationals; no integral representation decomposition is claimed. This is an exact enumeration of this graph, not a sampled or extrapolated assertion. Independent audit has not been performed.
