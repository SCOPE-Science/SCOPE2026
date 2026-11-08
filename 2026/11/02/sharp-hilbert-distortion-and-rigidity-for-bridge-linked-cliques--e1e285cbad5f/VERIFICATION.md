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

For two leaf-clique centroids, the within-clique variance lower bounds are a=(m−1)/(2m), b=(n−1)/(2n); upper own-hub/bridge lengths and lower cross-leaf distances force 9≤(sqrt(c²−a)+c+sqrt(c²−b))²+a+b. Strict decrease in variances and increase in c yield the unique optimal root. Orthogonal regular simplices on a collinear hub bridge achieve all pair bounds, including cross-hub lower distance two. Equality propagates to every leaf-edge length and cross-leaf distance; centering forces orthogonal simplex spans and an affine dimension m+n−1, hence congruence rigidity. Independent numerical root and pair-orbit checks covered unbalanced sizes and large examples, not infinite sizes.

## originality

PASS

Robertson (2023) proves general negative-type/distortion characterizations and examples for bicliques and cubes, not the exact bridge-linked two-clique point metric. Linial–Magen develops Euclidean distortion machinery for cycle products; Duda–Wong studies bridge barbell quantum walks, a different invariant. Neither material comparison yields this root/rigidity result.

## value

PASS

A classic barbell graph gives a natural exact c2 invariant with complete rigidity of every optimizer and sharp size supremum. The result solves all clique cardinalities, not a one-off small numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
