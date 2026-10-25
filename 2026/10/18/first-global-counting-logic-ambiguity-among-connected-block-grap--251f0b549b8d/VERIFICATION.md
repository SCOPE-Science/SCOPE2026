---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For simple unlabeled graphs with 1<=n<=6, the certificate's 2^(n choose 2)-mask enumeration and adjacent-transposition orbit closure cover every isomorphism class; Tarjan edge-block test correctly recognizes connected block graphs and globally interned 1-WL signatures compare against ALL graphs. Independently recomputing graph-atlas types and global colour refinements yielded all-graph counts (1,2,4,11,34,156), block-graph counts (1,1,2,4,9,22), exactly one ambiguous connected block graph (n=6) and 152 global 1-WL classes at n=6. G (two triangles joined by a bridge) and H (theta with paths 1,3,3) are nonisomorphic (2 versus 0 triangles), yet have the same equitable two-colour partition: two degree-3 nodes each see 1 degree-3 and 2 degree-2 neighbors and four degree-2 nodes each see one of each. Both have 7 edges. These direct checks give the explicit witness AND complete minimality/uniqueness to exactly n=6, without extrapolating to higher orders.

## originality

PASS

Best-of-knowledge original contribution is the precise Sharp global C²/1-WL identification cutoff and unique six-vertex ambiguous connected block graph. Prior coverage of general methods/nearby problems is credited; exact statement/implication comparisons and residual risks are detailed below. The unsuccessful Resultary lookup is not treated as proof of novelty.

## value

PASS

Global C²-identification is a natural and consequential graph-invariant boundary: the comparator includes every simple graph, so even a globally amenable block-graph family can develop its first failure. Exact six-vertex order, uniqueness among 22 connected block-graph types and a non-chordal comparator distinguish restricted-class enumeration from the unrestricted recognition problem. A complete sharp finite cutoff and fully determined mate class are a useful small obstruction benchmark; this is not claimed as a new general amenability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
