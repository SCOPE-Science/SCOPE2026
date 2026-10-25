# Review

## Correctness

**PASS.** The construction defines natural persistence-poset maps, and both persistence objects are finite type. A degree-one map between integral homology 3-spheres induces an isomorphism in every homology degree, so the persistent homology modules are isomorphic. The explicit length-\(m\) interleaving proves the upper bound. For every shorter integer shift, naturality forces a map \(S^3\to\Sigma\) to have a homotopy right inverse; the covering-degree obstruction rules this out. For each principal lower-set fiber, the structure map after a shift of \(2\lceil m/2\rceil\) lands in a contractible lower set, and compatible point choices verify weak contractibility in the persistence sense.

## Originality

**PASS, with residual uncertainty.** The closest source is Guzeev–Tanaka's 2026 persistence Quillen–McCord theorem, which supplies an upper bound and explicitly lists the difference between \(d_{\mathrm I}\) and \(d_{\mathrm{HC}}\) as a future direction. Their paper does not give this delayed homology-sphere-to-sphere family or the exact formula \(d_{\mathrm{HC}}=m\), \(d_{\mathrm I}=0\). The earlier homological theorem addresses persistent homology bounds rather than the homotopy-distance gap. Searches for equivalent formulations and exact examples found related finite-space homotopy/homology distinctions, but not this persistence family. An unindexed or unpublished equivalent remains possible.

## Value

**PASS.** The family establishes that no bound on the homotopy-commutative interleaving distance can depend only on the homology interleaving distance, even within the lower-fiber framework of the persistence Quillen–McCord theorem and with fixed target. This is a concrete calibration example for the paper's stated question about information lost by passing to homology. It is not claimed to improve or sharpen the theorem's general upper bound.

## Closest literature and limitations

- Guzeev–Tanaka, *Quillen-McCord theorem for persistence finite posets*, arXiv:2605.11615: Theorem 3.8 and Corollary 3.10 provide upper bounds; the conclusion explicitly flags the distance gap as future work.
- Guzeev, *Persistent homological Quillen-McCord theorem*, arXiv:2307.00177: a homological interleaving result, without the exact homotopy-distance family here.
- The Poincaré homology sphere is used only through its integral homology, nontrivial fundamental group, and degree-120 universal cover. The construction is existence-theoretic; no minimal triangulation is supplied.

Self-review: passed. Independent audit: not yet performed.
