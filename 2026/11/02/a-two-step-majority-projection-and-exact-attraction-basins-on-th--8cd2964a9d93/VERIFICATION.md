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

The ten Fano subset cases partition 128 point subsets: Psi Phi is an idempotent projection onto 58 subsets (empty, full, 28 noncollinear triples and 28 complements). With the dual, F^2=P×Q, F^4=F^2; recurrent states are a swap of two 58-symbol factors, yielding 58 fixed configurations and C(58,2)=1653 two-cycles. Fibers 36,36 and 56 ones yield fixed basin classes 1(56),1296(2), two-cycle 2(1540),72(112),2592(1). Independently rebuilt the Fano graph and exhaustively checked all 16384 state orbits and first-entry table against source check_fano.py and check_heawood.cpp; direct incidence proof independently covers all states. F^3!=F via the two-point witness.

## originality

PASS

The 1980 Goles–Olivos theorem implies eventual periods at most 2 in finite symmetric-threshold systems, but does not give the sharp Heawood-specific entry time, 58-symbol swap, all basins, or Fano subset projection. Existing Heawood graph geometry is not the dynamical census. No equivalent same-graph rule statement located in the primary comparisons.

## value

PASS

The Heawood graph is a canonical small cubic bipartite graph; complete finite nonlinear dynamics on all states, a two-step projection and exact attraction basins provide a motivated natural classification, not an unmotivated lookup table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
