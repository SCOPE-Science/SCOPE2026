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

For H_n=K_n square K_2, exact distance-two signatures at (0,i),(1,i) are B\{i}, A\{i}. Nonempty signatures in opposite layers cannot coincide. In-layer collisions require |A union B|>=n-1, while missing witnesses force the three boundary patterns for empty and singleton layers. Multiplying (2z+z^2)^n and allowing one empty column then subtracting the three disjoint forbidden patterns yields the stated P_n, including the explicit n=3 double-count correction. Deletion minimality reduces for n>=5 to disjoint A,B partitioning n-1 columns with layer cardinalities>=2, plus the empty/full and singleton boundary classes; n=3,4 are handled individually. Independently enumerated every subset of the actual adjacency graph for n=3..7, testing exact distance-two signatures and all single-deletion minimality. Counts n=3..7: all (36,149,588,2103,7178), minimal by cardinality (14 at 3;56 at4;30 at4+42 at5;120 at5+62 at6;350 at6+86 at7), matching P,Q. Source script and verification note were read but not accepted as proof of n>7.

## originality

PASS

The original definition and operations theorems predate this result; the exact complete-prism/crown all-set and minimal enumerators do not follow from their theorems on joins or coronas. A fresh primary full-text comparison and semantic finding search support best-of-knowledge originality, with explicit risk of differently named crown-graph classification.

## value

PASS

The complete prism/crown is a canonical symmetric graph family; not merely a new notation. The complete labeled-cardinality and inclusion-minimal enumerators refine its locating-hop domination number and exhibit the structurally meaningful five-column change, which can be used in graph-identification and locating-domination polynomial work. Both enumerators require a nontrivial boundary case and minimal-deletion classification, not a generic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
