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

# Exact reproducibility

Execute `python3 verify.py` in the extracted file directory (Python 3.10+ standard library only). Compare its terminal output with `verification_output.txt`.

The checker confirms an explicit twelve-vertex graph and orientable spherical rotation system, all \(324\) augmented faces, the \(152\) matching pairs, exactly twenty critical dimension-three faces, all \(984\) directed Hasse incidences, and a topological order of the entire matched Hasse graph. Its independent field-homology ranks are \((11,55,85)\) in degrees one to three. It also exhaustively enumerates all \(120\) automorphisms, verifies graph and orientation preservation/reversal, calculates signed simplicial Lefschetz characters for every group element, isolates the central involution and checks the two rational eigenspace characters.

Expected exact success marker: `ICOSAHEDRAL_TWO_INDEPENDENCE_EXACT_MORSE_AND_SYMMETRY_OK`.

The homotopy classification follows from the complete discrete-Morse certificate; the mod-two chain calculation does not establish integral torsion freedom on its own. The rational representation statement does not assert an integral lattice decomposition. The evidence has not undergone an independent audit or external certification.
