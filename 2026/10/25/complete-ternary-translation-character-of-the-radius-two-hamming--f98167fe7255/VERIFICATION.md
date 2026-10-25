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

# Finite verification certificate

Run `python3 verify.py` from the extracted package directory with Python 3 (standard library only). It generates the 27 Hamming triples, all allowed-pair adjacencies, all 5,949 faces, 2,951 staged Morse pairs, and the complete 27,189-arrow matching-orientation graph, then checks the graph is acyclic by topological sorting all 5,949 vertices. Its 47 unmatched nonempty cells are exactly one vertex and 46 tetrahedra. It separately constructs each simplicial boundary map over \(\mathbb F_2\) and computes nonzero ranks \((26,217,728,954,666,279,72,9)\), giving Betti vector \((1,0,0,46,0,0,0,0,0)\). The acyclic matching, rather than finite-field ranks alone, supplies the integral homotopy input.

It then checks signed Lefschetz contributions face by face for each of the 27 translations, reproducing rational degree-three traces \((46,4,-2,1)\) by translation weight. Independently it reconstructs the nine translation-orbit complexes of three representatives and verifies face vectors \((9,18,6)\), \((9,9,3)\), and \((0,0,0)\). Integer polynomial arithmetic proves that the Fourier multiplicities are \((2,2,2,1)\) by character weight. The exact replay output is included in `verification_output.txt`.

This is a complete exact finite certificate for this fixed 27-point space. It does not verify other alphabets or dimensions, the integral group-ring module, or originality outside the inspected literature. Independent validation has not been performed.
