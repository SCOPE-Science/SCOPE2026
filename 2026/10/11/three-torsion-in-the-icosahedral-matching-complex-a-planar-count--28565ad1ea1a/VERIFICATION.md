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

# Reproducibility and verification limits

Use Python 3 (standard library only). Execute `python3 verify_morse.py` and `python3 verify_modular.py` in a directory with the two included standalone source files. Successful completion ends with `ICOSAHEDRON_MORSE_PASS` and `ICOSAHEDRON_MODULAR_PASS`, respectively. Both checks reconstruct the combinatorial graph and complex without external datasets. They operate only on finite structures.

The first reconstructs all thirty edges, twenty triangular graph faces, 5,887 nonempty matching simplices, 23,130 directed Hasse incidences and the complete acyclic 2,866-pair matching. It constructs the signed integer Morse boundary matrix and checks its rank over two finite fields, together with a specified exact 45-by-45 determinant-three minor. The Smith-factor conclusion follows because rank modulo three is 44, while a maximal minor has determinant exactly three. The graph's planarity is witnessed by its triangular spherical embedding. The homotopy statement further uses the standard discrete-Morse equivalence and the fact that degree matrices classify maps between wedges of three-spheres.

The second uses a separate explicit edge list and tuple-based matching enumeration, and directly computes simplicial boundary ranks over fields of two, three and five elements; these serve as independent cross-checks rather than proofs of integral torsion on their own. Neither verifier invokes formal proof software or an external reviewer. Results for other graphs, uniqueness among all planar graphs and bibliographic uniqueness are not verified here.
