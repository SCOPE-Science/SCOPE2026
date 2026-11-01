---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

A uniform tree of Theta(a,b,c) deletes exactly two edges on distinct paths, giving W=ab+ac+bc equally likely deletion pairs. Each pair of distinct deletion indicators has strictly negative covariance. Vertex degree equals host degree minus incident deletions, so nonadjacent vertices have strictly negative covariance. Shared-edge diagonal terms produce the two displayed positive rational forms, and elementary expansions show equality only for all edges of (2,2,2) and the middle length-three edge of (2,2,3). Independently implemented brute-force connectivity enumeration checked all 216 ordered triples a,b,c∈{2,...,7}; all vertex-pair exact rational covariances satisfy edge iff covariance≥0. All-length result follows from algebra, not finite enumeration.

## originality

PASS

General reduced-Laplacian formulas already compute covariances for arbitrary weighted graphs, and real-stability theory describes a different property. The uniform all-length theta sign separation, exact equality cases and adjacency-reconstruction corollary require nontrivial special inequalities not stated in inspected prior results; priority remains qualified by possible earlier theta specialization. Actual named comparisons and inaccessible-source limitations are recorded below.

## value

PASS

Recovering labeled edges of a natural bicyclic graph family solely from exact random-spanning-tree degree covariance is a structurally motivated inverse-statistics theorem, including sharp zero exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
