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

# Exact reproduction and checks

Run `python3 VERIFY.py` from this directory (Python 3.8+ standard library only). Check that the process completes with `VERIFY_OK`. The saved `VERIFICATION_OUTPUT.txt` is supplied for comparison and is not itself a substitute for running the checker.

The executable reconstructs the entire twelve-vertex icosahedron from a fixed adjacency list. It enumerates all 4,096 subsets using independent parity-coloring and simple-odd-cycle tests, establishes the face vector and the 32 minimal forbidden sets, verifies each of the twelve elementary collapses of the triangle-free supercomplex, tests connectedness and every codimension-one incidence of the hundred-facet pseudomanifold, and replays a six-step signed orientation-obstruction walk.

The executable then forms all 510 acyclic face pairs, checks all 4,212 cover incidences by directed topological sorting, computes the exact integral differential between the two positive-dimensional critical cells as \(+2\), and independently checks the two top boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). These finite calculations support an integral Moore-space homotopy equivalence by standard discrete Morse theory and the degree classification of \(S^4\to S^4\).

The calculation does not classify other graphs; exhaustive finite verification is not a general theorem. No independent external review has been performed. Historical literature comparison is limited by unavailable full book chapters and potential unindexed equivalent work.
