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
# Verification of the two-particle metric-star barcode

The mathematical proof in `RESULT.md` is the basis of the arbitrary-length conclusion. This file reports finite arithmetic cross-checks without claiming exhaustive coverage of real parameters or external validation.

Run `python3 verify_polyhedra.py`. The script builds each polygon \(Q_{ij}\) and same-arm triangle \(T_i\) using exact fractions, glues actual shared vertices, constructs simplicial chain groups, checks mod-two boundary ranks, and compares with the model. Expected stdout begins `VERIFY_OK 7065 polygonal-mod-two-chain comparisons, k=3..8`.

Run `python3 verify_barcodes.py`. The second script builds the inclusion-filtered incidence graph, processes vertices and edges in decreasing separation order, records zero-dimensional merges and one-dimensional edge-cycle births, and compares both lists to the claimed interval endpoints for 10,000 rational arm vectors. Expected stdout: `BARCODES_OK 10000 exact filtered-graph barcode tests, k=3..12`.

The programs require Python 3 and only its standard library. The first code tests homology over \(\mathbb F_2\), the second exact graph barcodes. They do not certify the infinite-domain claim or integral homology; those rely on the explicit strong deformation retract and graph argument. Inclusion maps on graph homology are accounted for analytically, and tie events are tested with exact arithmetic.
