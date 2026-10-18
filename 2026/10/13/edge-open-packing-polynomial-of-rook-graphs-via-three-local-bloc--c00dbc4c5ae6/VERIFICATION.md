---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For R_{m,n}=K_m □ K_n each edge-open packing induces a disjoint union of stars with no graph edge between distinct stars, since any bridging third edge conflicts two selected edges. The rook neighborhood splits into a row clique and a column clique, so each star has one edge or a right-angle two-edge L; no induced 3-leaf star exists. Distinct selected blocks must use disjoint row labels and disjoint column labels. Counting labelled horizontal (1,2), vertical (2,1), and L (2,2) blocks with 4 centers gives EGF exp(u+v+uv²z/2+u²vz/2+u²v²z²). Its coefficient extraction yields the proposed triple sum and distinguished-row recurrence. Rows and columns consumed are each at least the number of selected edges; equality on an odd square would require only 2-edge blocks, impossible by parity, and explicit disjoint L-block constructions attain the bound otherwise. Independent literal third-edge conflict checks enumerate all edge subsets for boards 1x2,2x2,2x3,3x3 and get [1,1], [1,4,4], [1,9,12], [1,18,45], matching the factorial coefficient formula exactly.

## originality

PASS

The general induced-star description is already established by Chelladurai–Kalimuthu–Soundararajan (2022), so it cannot be claimed as new. Brešar–Samadi (2024) analyze complexity, extremal bounds and trees; Brešar–Dravec–Hedžet–Samadi (2024) supply general Cartesian-product lower bounds but not all rook packings. The exact two-sort resource decomposition, bivariate exponential formula, every coefficient and odd-square maximum are not in inspected sources. Resultary query for rook EOP polynomial returned rook homology and other invariants, not an EOP enumerator.

## value

PASS

The rook graph is a natural two-parameter graph family and the edge-open-packing polynomial is a canonical exact statistic counting every feasible edge subset, not merely the maximum. The complete labelled three-block decomposition supplies a useful two-sort generating function, recurrence and sharp parity optimum. Such an exact full enumerator is a motivated invariant for extremal and injective edge-coloring questions; it is not a random finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
