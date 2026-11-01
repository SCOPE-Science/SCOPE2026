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

# Reproduction and scope

Run `python3 verify.py` with Python 3.9 or newer; no third-party modules, network access, or external data files are required. A successful run exits with code zero and begins with `CUT4_GIRTH_FIVE_ELEMENTARY_COLLAPSE_OK`.

The checker constructs each tested graph from a precisely specified edge list. For every case, it exhaustively enumerates induced connected four-vertex sets, all five-vertex sets with every four-subset connected, and every six-set that could violate the dual's asserted dimension. It checks the independent degree formula. It performs a legal elementary collapse pairing for each five-cycle four-cell and a legal free-triangle collapse for every remaining tetrahedron, checking uniqueness in the current complex after each move. The number of collapses is exactly the number predicted by the proof.

Full mod-two simplicial boundary ranks of the Alexander dual are calculated independently for all ten named graphs. For named examples on nine or ten vertices, the program separately reconstructs the ordinary four-cut complex from disconnected quadruples and computes its complete reduced mod-two homology directly. Both calculations agree with the formula; in particular, the Petersen four-cut complex has twenty-six degree-five classes. The dodecahedral graph has 140 connected induced quadruples, twelve pentagons, and predicted rank 841 in degree fifteen.

A fixed random seed generates 300 additional girth-at-least-five graphs on nine through fourteen vertices, checked for face characterization and the full elementary collapse schedule. The named cycles and Möbius–Kantor graph have girth at least six and serve as boundary-control tests; they are not added to the claimed girth-exactly-five theorem. All other named girth-five cases supply targeted five-cycle tests. See `verification_output.txt` for actual output.

**Limitations.** These are finite reproducibility tests, not an exhaustive census of all graphs of any order, and mod-two computations alone do not establish integer torsion-freeness. The proof in `RESULT.md`, especially the free-face classification, Alexander duality, and Hurewicz–Whitehead deductions, supplies the infinite-family and integral assertions. Independent audit has not been performed.
