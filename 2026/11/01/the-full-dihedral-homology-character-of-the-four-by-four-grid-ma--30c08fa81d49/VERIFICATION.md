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

# Reproducing the integral matching-complex symmetry calculation

Run `python3 verify.py` in a directory containing this file and the standalone checker. Python's standard library suffices. The checker fixes the sixteen grid vertices, twenty-four ordered edges, exact signed chain orientation, cyclic/reflection maps, and the complete ordered Morse matching. It constructs all 10,012 faces, verifies all 47,968 oriented incidence edges form a directed acyclic graph, builds integral generators and dual cocycles, and verifies the eight dihedral action matrices and the complete rational irreducible multiplicities.

Expected terminal marker: `ALL_VERIFY_OK`. The intermediate lines print the entire character on the eight elements, the two integral fifth-homology matrices, and the independent Lefschetz traces. The stated integral homology basis is computed by exact unit-pivot elimination and all cycle/cocycle pairings are checked, rather than relying on a numerical rank approximation.

The proof and program address this single finite graph. They do not establish an infinite-family result, a topological equivariant wedge decomposition, or an integral irreducible splitting in degree four. The prior nonequivariant homotopy type is credited in RESULT.md. No independent validation has been performed.
