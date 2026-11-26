---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Independently reconstructed both directions of Theorem 1 for noncomplete n>=3: an (n-1)-set omits just x, so each internal nonedge must have a two-edge geodesic through x. This holds exactly when every complement neighbor of x has no other complement neighbor; connectivity of the induced set is the remaining condition. The full set is visible only for a complete graph. The complement component at x is a star; a leaf of a nontrivial star is universal in G-x, while for an isolated x connectivity requires the complement of the remainder to be connected. If both graphs are connected a spanning complement star would disconnect G, proving the corollary. For n>=5 complete/edgeless pairs do not attain either upper bound. Otherwise both parameters are at most n-1 and the prior sum bound excludes two n-1 values; attaining either bound is exactly (n-1,n-2) in some order. Take the star component as above in the complement of the (n-1) graph. A star contributes at most 2 (a connected set containing two leaves must include their center, blocking their geodesic), so some remaining component must support n-2>=3 vertices; the star has at most two vertices. For a two-vertex star the remainder must be a clique K_{n-2}, giving K_{2,n-2}. For an isolated x the remainder Q has mu_c(Q)=|Q|-1 and connected complement. Applying the criterion inside Q forces its complement to be a spanning star; this yields K_2 joined to an independent set. Both examples give n-1 by the criterion and n-2 by the component rule in the complement. This verifies the theorem precisely for n>=5 without inferring anything about order-four equality.

## originality

PASS

Credit the complete equality classification for n>=5, not the inequalities, the examples attaining them, or the omitted-vertex implication as independently novel. The structural test is a useful reformulation of the source's proof idea. The checked papers and closest catalog results do not supply the necessity proof excluding all other extremizers. This is a bounded best-of-knowledge comparison.

## value

PASS

The result converts two known sharp inequalities into a complete structural classification of extremizers for all n>=5. The distinction between producing examples and proving there are no others matters to the extremal question. The complement-component reduction makes the necessity proof short and transparent; the small-order limitation is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
