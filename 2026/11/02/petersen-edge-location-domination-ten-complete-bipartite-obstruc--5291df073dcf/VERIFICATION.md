---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

A selected edge set is qualifying iff every outside edge has a nonempty, pairwise distinct intersection signature with selected incident edges. I independently generated KG(5,2), its 15 line-graph vertices, exhaustively checked every 0..5 subset (4944 total), obtaining no solution below five and exactly 246 minima. Enumerating every 30,135 unordered pair and BFS from each of 246 vertices gave 1470 exchange edges, all eccentricities five, defect 90 and the prescribed histogram. A separately built S5 action reproduced all four orbit sizes, degrees and distance profiles; the 90-pair defect graph decomposed into ten components of size six with all nonisolates degree three. The finite theorem is exhaustive, not extrapolated.

## originality

PASS

Foucaud et al. establish the stronger selected-vertex identifying-code size five, and Foucaud–Henning prove general bounds for ordinary location-domination on line graphs; neither inspected primary result determines all weaker Petersen minima, 246-state exchange metric and K3,3 defect geometry. An older data table/reconfiguration calculation remains possible.

## value

PASS

The Petersen graph is a canonical natural small strongly regular graph; its complete optimum-code reconfiguration space and sharp geodesic defect classify a mathematically motivated discrete optimization invariant, not an arbitrary handful of samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
