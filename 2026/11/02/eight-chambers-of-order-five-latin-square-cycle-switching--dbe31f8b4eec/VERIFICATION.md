---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The finite graph is on all 161280 fully labelled order-five Latin squares; 1344 squares with first row fixed times 5! gives all vertices exactly once. For two rows or columns, a relative derangement is either a five-cycle or disjoint (2,3) cycles, and one legal switch exchanges exactly a single minimal cycle. A distinct independent exhaustive C++ reconstruction enumerated 1344 normalized squares, expanded all 161280, counted 288000/576000/1036800 unique undirected edges at lengths 2/3/5, and computed DSU components (17280 singles plus eight of 18000 for 2; 17280 singles plus two of 72000 for 2,3; six of 2880 plus two of 72000 for 2,3,5); all 17280 cyclic-class squares have zero intercalates and the other 144000 have four. This is exhaustive over a finite, fixed domain, not an extrapolation to higher orders. Independently checked the complete source RESULT.md, both supplied verifier implementations, and actual frozen Git tree/blobs.

## originality

PASS

Wanless 2004 analyzes isotopy/main-class switch graphs, while the inspected submitted result counts connected components among 161280 labelled vertices with exact single-cycle restrictions; the known intercalate-only census is prior baseline and explicitly not claimed. Aryapoor–Mahmoodian permits improper squares, which can connect through states forbidden here. No matching label-level {2,3}/{2,3,5} component histograms located in the checked primary text or Resultary search; best-of-knowledge rather than an absolute novelty claim.

## value

PASS

Switching connectivity for proper Latin squares is a natural finite reconfiguration problem: the addition of length-three moves merges eight previously known 18000-vertex components into two 72000-vertex components, while length-five moves liberate all 17280 isolated cyclic-class squares but retain six small components. Full exact chamber and edge counts are mathematically meaningful beyond the already known two isotopy classes and intercalate-only baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
