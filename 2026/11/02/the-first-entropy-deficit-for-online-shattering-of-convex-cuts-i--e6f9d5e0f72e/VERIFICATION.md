---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two constants plus two orientations of every edge cut give exactly 2n distinct halfspaces: two crossing edges between connected sides would form a cycle. A shattered tree of depth d uses at least 2^d concepts. At n=2 the class is the power set, and at n=3 an endpoint query leaves two three-concept chains. The four-vertex path has depth three by endpoint/threshold queries; in the four-vertex star two leaf queries give four two-concept cells, each splittable. Every larger tree restricts to the full halfspace class on any connected four-vertex induced subtree, giving the lower bound three. At n=8, depth four forces equality at every split. After a positive query at v, exactly d(v,w) of the eight remaining concepts exclude w, so a balanced second query has d(v,w)=4. Of the four concepts containing both vertices, exactly d(x,P[v,w]) exclude x; hence a balanced third query forces distance two to the path. Conversely, query v and w in both branches. The same x bisects the equal-answer cells by complementation; the midpoint bisects the opposite-answer cells. Each remaining pair differs on a vertex, giving the fourth query. On paths of any order the first endpoint split gives two chains of size n and threshold queries achieve the matching count bound. Independent Prüfer enumeration and exact version-space rank gave 11/12 unlabelled and 218400/43744 labelled trees at ranks four/three out of 23 and 262144 respectively, with motif and rank agreeing in every shape. All orders 2 through 7 and paths through 14 matched the formulas in the replay.

## originality

PASS

The distinct supported result is the first order at which tree halfspaces miss their hypothesis-count bound, the exact order-eight geometry for attaining it, and its shape/labelling totals. Basic cut structure and path threshold search are not separately novel. The strongest readable comparisons concern the same halfspaces under other learning measures, or the same online invariant for a different class of concepts.

## value

PASS

The order-eight cutoff is the first opportunity for any tree shape to fail a tight small-order count bound, not an arbitrary census cutoff. Detecting exact maximal rank by one path and one off-path distance gives an immediately usable local structural test and clarifies why hypothesis cardinality does not determine adaptive shattering in this family. The two censuses quantify that split; the routine path formula gives a contrasting benchmark, not the main contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
