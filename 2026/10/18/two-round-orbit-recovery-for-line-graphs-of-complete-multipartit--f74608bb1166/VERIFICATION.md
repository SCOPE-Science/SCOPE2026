---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a root edge xy, put d_x=N-a, d_y=N-b and T=sum_z d_z=N^2-Q. The inclusive sum of line-graph degrees over the star at x is d_x(d_x-2)+T-a d_x, since the excluded root vertices are precisely the a in x's part. Adding the y star and subtracting 2D(xy) recovers equation (3), with D=2N-a-b-2. Thus equality of second-round colours forces equality of a+b and a^2+b^2 and hence of the unordered multiset {a,b}. Root automorphisms act transitively on each such type, and full line-graph automorphisms preserve refinement, so the exact orbit conclusion needs no lifting theorem. Counting parts gives the displayed cell sizes and class count, including r=2 or repeated equal parts. Distinct equal-sum types cannot share a part; their four parts have total size at least 2*4, with equality uniquely at (1,2,2,3). Its four type sizes are 4, 3, 4, 12; the two colliding degree-10 types have neighbour-degree sums 100 and 96. This proves the exact depth and minimum, with the infinite sharp family checked by its identical endpoint sums. Read the three checker sources and logs (replay paths in VERIFICATION.md); not rerun. The direct checker tests attainment at the predicted depth and failure to attain before it, not each individual round-one equivalence in depth-two cases; the symbolic argument supplies all partitions. No cross-graph identification is shown.

## originality

PASS

The supported distinct claim is an exact depth classification of within-graph colour refinement on arbitrary complete multipartite line graphs, including endpoint-type recovery in two rounds and the unique least sharp instance. No equivalence or dominating result was established in the strongest checked material; general refinability and the studied alternative reconstructions do not yield the two moments for each individual edge.

## value

PASS

A natural unbounded family has an exact refinement depth, explicit orbits and a unique minimum configuration where the degree partition fails. The second neighbour-degree moment explains the mechanism without orbit enumeration or lifting assumptions. This is a useful sharp classification, not merely a recomputed small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
