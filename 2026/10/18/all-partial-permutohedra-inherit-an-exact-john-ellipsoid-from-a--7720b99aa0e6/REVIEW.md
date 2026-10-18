# Self-review

## Correctness — PASS

The primary polytope description is taken from the full facet theorem of Behrend and coauthors. The proof reduces every subset support to an exact scalar depending on cardinality, establishes the strict screen for all intermediate subsets in both parameter ranges, and supplies positive John moment decompositions for each containing-envelope ellipsoid. These moment identities establish unrestricted optimality rather than optimization only over a symmetric subfamily. Endpoints \(m=n\) and \(n=m+\sqrt m\), diagonal/offdiagonal normalization, and positive definiteness are covered algebraically. The embedded rational checker independently tests 9,900 parameter profiles and 69,394 explicit subset masks. The code is finite corroboration, not the universal proof. No independent audit has been performed.

## Originality — PASS, qualified

The exact ellipsoid of a capped hypercube and its three phases were previously derived in *Three-phase John ellipsoid of a capped hypercube*. An inscribed Euclidean ball, outer Löwner ellipsoids, the partial-permutohedron facet theorem, and standard simplex ellipsoids are also prior results. These stronger/related statements do **not** directly yield the exact John ellipsoid of the strictly smaller partial permutohedron: the missing necessary implication is feasibility with respect to every intermediate proper subset inequality. The new proof establishes that implication uniformly and identifies all contact facets in the smaller polytope. Targeted mathematical searches and direct inspection of the closest full results did not identify a covering statement. Residual risk: an earlier general symmetric-polymatroid or optimization theorem might subsume the facet-screening lemma.

## Mathematical value — PASS

The theorem determines a canonical maximum-volume ellipsoid of an infinite, natural family of polytopes whose subset-facet description can be exponentially large. The nontrivial fact that all intermediate facets are irrelevant gives an exact reduction to a simplex or capped cube, an abrupt coordinate-contact transition, an anisotropic intermediate regime, and a sharp roundness transition. It is a complete structural classification for the two-parameter family, rather than routine numerical specialization of the capped-cube theorem: its decisive additional mathematical claim is a uniform new subset-containment proof.

## Closest literature and limitations

Heuer–Striker (arXiv:2012.09901v1) and Behrend and coauthors (arXiv:2207.14253v1) provide the starting facet/vertex formulas. The full published *Three-phase John ellipsoid of a capped hypercube* supplies the enclosing family's established formulas. Published partial-permutohedron inball and enclosing-ellipsoid theorems concern other optimization targets. All available comparison claims were checked by hypotheses and implication, not title similarity. The stated originality conclusion is qualified by remaining literature-access and nomenclature risk, not independently validated.

Self-review: passed. Independent audit: not yet performed.
