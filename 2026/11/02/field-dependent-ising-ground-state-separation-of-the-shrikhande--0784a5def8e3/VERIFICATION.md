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

For negative-spin r-set in either degree-six graph, cut B=6r-2e; the strongly regular identity A²=4I+2J yields min-eigenvalue lower bound e>=r²/4-r. Independent-set witnesses attain r<=4 and explicit binary masks attain the sharp integrality bounds for r=5..8 except rook r=6; there the row-column pair count forces e>=4 versus the Shrikhande e=3 witness. Independently rebuilt each coordinate graph, enumerated ALL 65,536 labelled spin assignments each and reproduced every sector B,C entry for r=0..8 (and complement symmetry for 9..16), including Shrikhande C6=32 vs rook C6=1224. Convex envelopes of sector points give exact field breaks 1,3,6 vs 2,6 and all coexisting labelled degeneracies. Finite exhaustive census is a complete proof of finite multiplicities because the entire 2^16 domain is visited, not sample extrapolation.

## originality

PASS

Vinci et al introduce longitudinal-field Ising polynomial and test small vertex-transitive graphs up to 15 sites; their full article does not contain this 16-site Shrikhande/rook pair or its exact sector counts. Earlier strong-regular parameter tables give spectra but not Ising cut populations. Rook comparator is known from line-graph classification; new aspect is the Shrikhande r6 extremum and separation of the two exact field-response envelopes.

## value

PASS

The minimal famous cospectral 16-vertex strongly-regular pair is a canonical test of graph invariants beyond adjacency spectrum; exact zero-temperature field transitions, magnetization plateau, and degeneracies supply a reproducible, physically motivated separating invariant and sharp finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
