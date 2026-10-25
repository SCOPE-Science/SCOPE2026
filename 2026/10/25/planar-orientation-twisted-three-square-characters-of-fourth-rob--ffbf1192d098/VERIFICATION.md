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
# Reproducibility

Run `python3 verify_robust4_symmetry.py`. It uses only the standard library and **recomputes**, rather than reads a precomputed fixture for, the complete fourth robust clique face posets, forbidden independent four-sets, row-major Morse matchings and orientation of every face incidence. It topologically sorts all directed Hasse graphs (checking acyclicity) and verifies every point-group automorphism, signed Lefschetz character and determinant-twisted fixed-square-triple trace.

The four graph sizes, face counts, matched-pair counts, critical zero/five-cell counts and oriented incidence counts are described in `RESULT.md`. All exact character values are also stated there. A separate `certificate_summary.json` records expected totals; the executable has these totals independently encoded and raises an assertion upon any discrepancy.

**Limits:** This is exhaustive only for the four named grids with at most sixteen vertices. The verified discrete-Morse reductions prove the nonequivariant homotopy concentrations used by the rational Lefschetz calculation, but do not construct an explicit intertwining homology basis, an integral equivariant isomorphism, or an equivariant homotopy equivalence. No independent external scientific audit was performed.
