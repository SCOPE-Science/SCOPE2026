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

For a largest embedded part A and one representative z_i in each other part, A-A contains no connection value, while z_i-A consists entirely of connection values. A collision between z_i-A and z_j-A would give the edge difference z_i-z_j as a nonzero element of A-A by commutativity. The disjoint sets thus have total size |A-A|+(t-1)M>=tM. The cyclic host with an index-t subgroup of order M attains the bound. At equality, |A-A|=M and every translate A-a for a in A must equal H=A-A. Fixing a_0 gives A=a_0+H and H-h=H for all h in H, hence H is a subgroup. The disjoint translates and H exhaust the host, forcing S to equal their union outside H. Cross-part edges and within-part nonedges then force the parts into different cosets, and each part of size M fills its coset. For M=1 the proof gives H={0} and the clique host; multiple largest parts do not change the argument.

## originality

PASS

The bipartite and balanced size formulas, arbitrary-part upper bound and indexed K_{1,1,n} exact subfamily are covered. The lower bound on order alone is also a clique–coclique bound in a vertex-transitive host. The supported distinct content is the forced connection set and coset occupancy in every optimal abelian host, uniformly for arbitrary part sizes, together with the resulting sharp construction. The inspected comparisons do not supply that rigidity; the proof upgrades a packing-size argument by putting all differences of a largest part into its distinguished packing cell.

## value

PASS

The equality case is a structural answer for a natural family in the exact minimization problem: it classifies the host graph and its embedding geometry for all optimal abelian group types, including unbalanced tuples. This is stronger than supplying an optimal cyclic example or reproducing the known order for a special family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
