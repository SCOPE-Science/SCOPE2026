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
# Reproducibility and limits

Two standalone standard-library Python programs provide independent checks. Run `python3 check/finite_types.py` and compare its complete stdout byte-for-byte with `check/finite_types.out`. It builds adjacency from coordinate tuples and iterates the noncounting \(k\)-variable tuple-type refinement until stable on ten specified pairs at widths three, four, and five; every asserted equivalence or non-equivalence matched its prediction.

Run `python3 check/edge_spectrum.py` and compare its stdout with `check/edge_spectrum.out`. This independently enumerates maximal cliques, determines the largest clique containing each edge from graph adjacency alone, extracts truncated color classes and computes all finite connected-component diameters. It passed 39 checks using thirteen factor sequences and widths three, four, and five. No search heuristic, timeout, approximate statistic, or imported enumeration table underlies those checks.

These finite calculations do **not** establish claims for arbitrary dimensions, alphabet sizes, or quantifier depths. The universal proof consists of the edge-capacity lemma, finite-variable colored-path definability, colored-component diameter formula, and permanent coordinatewise pebble strategy in `RESULT.md`. The reported verification is neither independent mathematical audit nor external certification.
