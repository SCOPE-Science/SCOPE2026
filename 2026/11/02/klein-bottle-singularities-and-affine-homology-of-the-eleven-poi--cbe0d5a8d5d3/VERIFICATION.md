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
# Verification of the finite topological and equivariant calculation

Run the included `paley11_checker.py` with Python 3. It requires no packages outside the standard library. The checker tests every subset of size one through five, determines all maximal faces, and confirms the full codimension-one incidences. For each of eleven links it tests edge degrees, local six-cycle links, connected triangle dual graph and failure of a coherent orientation. It also tests that the global tetrahedron adjacency graph is connected.

The checker forms complete simplicial boundary matrices over \(\mathbb F_3\); it verifies ranks \((10,45,55)\). The proof in `RESULT.md` derives rational ranks from these finite field lower bounds and the exact chain-complex upper bounds. All fifty-five affine maps are checked directly to preserve tournament arcs and give characters \((10,-1,0)\) by simplicial fixed-point counts. The three invariant dimensions \((0,0,2)\), for the full affine group, translations and dilations, are verified exactly.

Expected first output line: `PALEY11_LINK_AND_AFFINE_CHARACTER_EXACT_OK`.

Limits: The checker does not calculate integral homology or an integral homology representation, and does not substitute a numerical sample for a universal theorem; the stated result is finite. The nonequivariant homotopy type and torsion were previously established by Govc. No independent audit has been performed.
