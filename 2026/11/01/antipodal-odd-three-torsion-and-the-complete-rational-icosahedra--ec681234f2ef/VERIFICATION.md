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
# Finite exact verification

Execute `python3 verify_equivariant_icosahedron.py` after installing the dependencies named in `requirements.txt` (`networkx`, `sympy`). The script is standalone: it constructs the icosahedral graph and all matching faces, plus the complete graph automorphism group, without precomputed input tables or internet access. The included `verification_output.txt` records the actual execution result and its final marker `ICOSAHEDRAL_MATCHING_EQUIVARIANT_EXACT_OK`.

A complete augmented face-poset traversal checks 5,888 faces, 23,160 incidences, 2,889 matching pairs and full acyclicity. It constructs the 87-by-23 integral Morse boundary, verifies the exact Smith factors of 22 units and one factor 3, and exhibits a 23-by-23 determinant -3. For rational representations it directly computes the signed fixed-face Lefschetz sums for all 120 graph automorphisms and compares the resulting integer class character with A5 representation rows. For torsion it constructs an explicit nonzero mod-three 4-cycle supported on 1,009 four-simplices, checks its entire mod-three boundary, verifies the cellular projection chain-map identity for each of 1,482 four-simplices, and evaluates its image under every graph symmetry. The 60 rotations act by +1 and the 60 orientation-reversing symmetries by -1 on the one-dimensional fourth mod-three homology. The natural universal coefficient theorem transfers this action to the characteristic integral order-three torsion subgroup of third homology.

Limits: The script checks a finite combinatorial object, not an infinite graph family. It uses discrete Morse theory, standard cellular/simplicial chain maps and naturality of UCT as mathematical theorems, not as executable external proof certification. The free integral lattice module is not classified. No independent audit has been performed.
