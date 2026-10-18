# Scientific review

## Correctness — PASS

The Manhattan-distance betweenness criterion is established in the proof. The strict-coordinate antichain argument excludes corner-rooted four-sets; a complete case split constructs an extension of each nonmaximal pair; each legal corner triple is proven maximal. Builder-first two follows from adjacent bipartite vertices; Blocker-first upper three follows from the corner cap; its lower three follows from an explicit isometric \(2\times3\) subgrid whose six vertices are partitioned into two feasible triples. The four-cycle boundary has no feasible triple. Exact minimax and rooted-set counting checks cover 18 graph instances with 20,504 visited minimax states. These finite computations corroborate but do not replace the unrestricted proof.

## Originality — PASS, with residual risk

The closest antecedent [1] defines the same game, gives the already-known Builder-first value two on bipartite graphs and a structural characterization of Blocker-first value two; it does not determine the Blocker-first value for rectangular path grids. Its Problem 5.7 explicitly asks for classes with Blocker-first value three. The grid general-position polynomial [2] counts feasible sets but has no adversarial minimax or fixed-corner maximal classification. The survey [3] distinguishes last-move achievement/avoidance games from the size-optimization game. The mutual-visibility game [4] has a different legality rule on grids. Searches for grid, Cartesian-product, equivalent corner-rooted, and game-value formulations across accessible literature and mathematical research records found no covering result. Searches alone do not prove absence; an unindexed equivalent or independently deducible stronger result is the residual risk.

## Value — PASS

This is a natural all-parameter solution to the Blocker-first side of a game family singled out in [1, Problem 5.7]. It proves a sharp opening-order gap \((2,3)\) for all rectangular grids other than the four-cycle and explains the precise three-move upper mechanism by a complete corner-rooted facet census. The problem is adversarial and is not determined by the known unrooted counting polynomial. The size-three rooted configurations are enumerated with a closed formula, not obtained by an arbitrary finite search.

## Closest sources and scientific limitations

[1] Klavžar–Tian–Tuite, arXiv:2310.19949, especially Sections 2–5, Corollary 2.4 and Problem 5.7. [2] Iršič–Klavžar–Rus–Tuite, arXiv:2401.05696, Section 3, Corollary 3.4 and Theorem 3.5. [3] Chandran–Klavžar–Tuite, arXiv:2501.19385, games discussion. [4] Chenoweth et al., DOI 10.1007/s40840-026-02083-9, Sections 2 and 5. Scope excludes higher-dimensional or wrapped grids and other game variants. Independent review and exhaustive literature coverage are not available.

Self-review: passed. Independent audit: not yet performed.
