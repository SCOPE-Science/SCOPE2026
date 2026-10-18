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

The degree partition immediately separates clique interiors, distinguished bridge vertices and connecting path for m>=4; symmetric distance-from-end refinement separates one reflected path layer per round, ending when the middle has at most two vertices. For m=3, degree-two clique interiors can merge with path vertices, explaining k=1 splitting at round 2, k=2 stable erroneous six-cell at round 1, and the k>=3 delayed split at round 3. Direct independent 1-WL code built B(m,k) and checked all 506 combinations 3<=m<=13,0<=k<=45, plus the six-cell at B(3,2). All-m,k correctness rests on the round-by-round wave argument rather than this finite enumeration.

## originality

PASS

The exact five-branch depth and unique equitable-versus-orbit anomaly are not a mere parameter renaming of the universal-cover formulation. Krebs--Verbitsky supplies correspondence with truncated neighborhood-unfoldings and general bounds, but the barbell-specific path symmetry and triangle collision require a separate analysis. Bounded family-specific searches and Resultary did not uncover an identical exact formula; residual priority risk retained.

## value

PASS

A common parameterized graph family admits a complete and structurally interpretable 1-WL depth classification, with a sharp exceptional failure of orbit recovery. The exact k,m boundary is motivated by local-information propagation, not a gratuitous small-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
