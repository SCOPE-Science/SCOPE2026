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

# Reproducible verification

Run `python3 verify_cut.py` with Python 3 standard libraries. It enumerates the graph, all 560 induced triples, 400 maximal cut faces, every one of 65,199 augmented simplices, all 32,591 matched pairs, and every one of 519,792 face incidences. It independently topologically sorts the directed graph to establish acyclicity. It then performs exact oriented integral gradient-path reduction to obtain the 16-entry boundary vector and confirms greatest common divisor two.

Run `python3 verify_dual_smith.py` with Python 3 and SymPy (tested with 1.14.0). This separate implementation constructs all connected triples without using the cut-complex matching, forms the exact 105-by-160 integral triangle-boundary matrix in a spanning-tree cycle basis of the complete graph and obtains Smith diagonal entries 104 copies of one and one copy of two. The computer output is preserved verbatim in `verification_output.txt`.

The signed Morse vector determines the attaching map because the Morse CW model has no cells in intermediate dimensions and the eleven-skeleton is a wedge of eleven-spheres. The fact that a primitive change of cellular basis is realized by a self-equivalence of the wedge uses standard Hurewicz and cellular arguments. Mere agreement of finite-field Betti numbers, a failed search or software execution without these topological steps would not establish the claimed integral homotopy equivalence. Only this finite sixteen-vertex graph and one cut parameter have been checked.
