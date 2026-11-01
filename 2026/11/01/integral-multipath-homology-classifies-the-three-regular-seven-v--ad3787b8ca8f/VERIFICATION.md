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

# Finite verification and limits

Execute `python verify_regular7.py` from this directory with SymPy available. The executable reconstructs all \(2640\) labeled regular tournament orientations, checks the three representative permutation orbits cover them disjointly, and independently enumerates the multipath faces via edge choices and successor assignments.

For each representative, its matching is verified against every nonempty face-poset Hasse incidence and certified acyclic using a topological sort. The code reconstructs the exact signed integral Morse boundary matrices, compares every entry and critical face index to `morse_certificate.json`, checks successive boundaries compose to zero, obtains integer Smith forms and checks the expected rank triples. A separate mod-two elimination on the original simplicial chain complex supplies independent boundary ranks; enumeration of all directed Hamiltonian cycles separately checks the top ranks. The saved execution output is in `verification_output.txt`.

The representative masks, ordered arcs, complete critical face lists, and all nontrivial Morse boundary matrices are embedded in `morse_certificate.json`. The input is finite and all selected paths are exhaustively checked, not extrapolated. The exact homology calculation does **not** establish integral homotopy equivalences, other tournament orders, or external independent audit.
