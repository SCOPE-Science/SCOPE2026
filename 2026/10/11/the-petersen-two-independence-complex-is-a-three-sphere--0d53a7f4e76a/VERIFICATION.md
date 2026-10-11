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

# Exact finite reproducibility

The standalone `verify.py` uses only Python 3 standard libraries. Run it as `python3 verify.py` in a directory containing that file. It enumerates all \(1024\) masks from a Petersen adjacency list and also all \(30\) forbidden three-vertex paths, confirms that the two tests define the same face set, counts the facets, builds the deterministic matching, and checks every oriented edge of its Hasse diagram by complete topological sorting. There are \(260\) nonempty faces, \(129\) pairs, \(860\) Hasse arcs, and precisely two critical masks: \(1\) and \(402\).

The independent mod-two boundary-matrix elimination gives reduced Betti ranks \((0,0,0,1,0,0)\) and boundary ranks \((9,36,54,25,5)\). This is corroboration only; the acyclic matching proves an integral homotopy equivalence. There are no random seeds, external packages, tabulated data imports, distributed computations, or unverified large-parameter extrapolations.

The proof assumes the standard discrete-Morse theorem converting finite acyclic face-poset matchings into a CW model. The exact finite checks establish acyclicity for this specified simplicial complex only. Independence of the mathematical review from the presented proof is not claimed.
