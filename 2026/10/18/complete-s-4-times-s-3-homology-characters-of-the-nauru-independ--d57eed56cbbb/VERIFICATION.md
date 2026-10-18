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

The self-contained `verify_nauru_symmetry.py` constructs the graph twice, confirms the explicit graph isomorphism, exhaustively enumerates 35,219 augmented independent faces, and reconstructs 17,607 acyclic matching pairs. The directed face-poset graph has 205,680 incidences and its complete topological sort establishes acyclicity. The exact signed integer critical \(4\times1\) degree-six Morse boundary is zero. These checks prove the stated integral reduced homology groups, not just rational ranks.

The same program enumerates 144 distinct group automorphisms, bounds the full graph automorphism group to at most 144 using individualized neighbor-color refinement, and evaluates signed fixed-face Lefschetz numbers for all 144 automorphisms. It independently recomputes class-representative traces directly from every fixed simplex and checks the 15-class table, the possible top-degree sign characters, and exact character inner products. No random experiment is used for the final proof and no external packages are needed.

Run: `python3 verify_nauru_symmetry.py`. Expected final status line begins `NAURU_EQUIVARIANT_VERIFY_OK`.

Scientific boundary: the rational degree-five representation is identified, but no integral degree-five automorphism-lattice classification or general family formula is claimed. Independent scientific validation remains unperformed.
