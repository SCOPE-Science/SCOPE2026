---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

A geometric H-fixed barycentric point has constant coefficients on full translation cosets; their uniform barycenters span the fixed complex iff the union of cosets is a Rips clique. A coset is allowable precisely when max_{h in H} wt(h)<=3, and two cosets are adjacent iff max_h wt(x+y+h)<=3. Counting each active coordinate in 2^(r-1) codewords bounds support and eliminates ranks >=4 by explicit rank-4 hyperplane weight-4 contradiction. At rank3 support size five would yield six pairwise-intersecting edges in K5, impossible (max four), leaving support three or four. Rank2 XOR weights classify exactly four forms; direct quotient Cayley generators give cube graphs for the first three and 4-cycles for the fourth. Rank3 quotient Cayley graphs are discrete; no triangles remain in the admissible orbit graphs, so graph models are exact PL homeomorphism types. Independently enumerated every rank>=2 subgroup of n<=5, checked coset adjacency and graph isomorphism for 155 admissible groups, and confirmed no extra rank>=4 cases; the unbounded result rests on the subgroup classification, not finite tests.

## originality

PASS

Best-of-knowledge: the submitted full statement was compared by actual implication to the specific prior primary statements and published mathematical index. AMBIENT_NOT_FIXED: Does not assert rank2/3 simultaneous geometric fixed spaces. ; AMBIENT_NOT_FIXED: Ambient homology/collapsibility is different invariant. ; DIFFERENT_INVARIANT: Sphere-wedge type of ambient Rips does not determine subgroup geometric fixed PL homeomorphisms.. An inaccessible plausible source alone was not treated as failure; meaningful risks remain listed below.

## value

PASS

Simultaneous subgroup geometric fixed sets encode genuine equivariant information not contained in ambient homology or its representation character. The exhaustive sharp code-weight threshold and transition between connected cubes, many circular components and isolated points is a natural structural PL classification with explicit boundary cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
