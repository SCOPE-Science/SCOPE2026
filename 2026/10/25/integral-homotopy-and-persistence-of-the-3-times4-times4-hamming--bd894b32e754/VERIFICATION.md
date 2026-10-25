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
# Exact verification and scope

The standalone `CHECK.py` is the complete finite checker. With standard Python 3, run `python3 CHECK.py`. It builds the adjacency predicate directly from Hamming words, generates all independent simplices including the empty simplex exactly once by ordered recursion, and checks the complete face histogram. At each ordered vertex it pairs all then-available faces by toggling that vertex; the verifier checks all remaining critical faces are three-dimensional and that the match is disjoint.

Every cover relation is oriented according to the matching; a topological sort of the entire resulting directed Hasse graph, not a sample, visits all 243270 vertices. Critical-face dimensions then yield the integral wedge decomposition by discrete Morse theory. The scale-one homotopy argument is given in `RESULT.md` and its line/vertex incidence counts are checked in the same program. The other scales follow from the exactly three possible positive Hamming distances.

Observed exact outputs: 243270 augmented faces, 1843680 Hasse covers, 121536 matched pairs, 198 unmatched dimension-three faces, 243270 sorted directed vertices, and first Betti number 57 at scale one. Terminal marker: `COMPLETE_HAMMING_3_4_4_FILTRATION_VERIFIED`.

The proof is finite and algorithmic, with no inference beyond the fixed 48-point space. No independent audit has been performed. A computation log by itself would not establish acyclicity; here the executable performs the complete directed-graph verification.
