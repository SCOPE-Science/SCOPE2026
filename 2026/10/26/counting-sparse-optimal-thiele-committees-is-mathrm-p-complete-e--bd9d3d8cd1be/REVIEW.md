# Scientific review: sparse counting of optimal Thiele committees

## Correctness — PASS
For every selected size-\(n\) edge set, there are exactly \(2n\) incident approvals. The pointwise strict bounds \(u(d)\le c d\) with equality only at voter degrees zero or one show that total score \(2nc\) occurs precisely when all \(2n\) voters are covered once, equivalently when the edges form a perfect matching. Hall's theorem supplies at least one perfect matching in every cubic bipartite input. The graph-to-committee mapping is one-to-one, and the sparse-family optimality predicate is polynomial-time checkable. The invoked independent theorem that counting perfect matchings on simple cubic bipartite graphs is \(\#\mathrm{P}\)-complete is supported by published literature; its original proof is not reproduced. Exact-rational finite verification passed for \(87,837\) committees and four score rules.

## Originality — PASS with residual priority risk
Ai's 2026 counting theorem establishes unrestricted \(\#\cdot\mathrm{OptP}\)-completeness, not the degree-bounded parsimonious subcase. Lassota–Sornat establish winner-determination tractability, not counting tractability. Janeczko–Faliszewski use the edge-candidate construction for the **greedy** version, so their theorem cannot be substituted for the assertion about every exact global maximizer. Previously established matching complexity is used rather than reclaimed. The closest risk is that this simple correspondence may occur elsewhere as an unstated or previously stated corollary; searches alone cannot certify historical uniqueness. The original Dagum–Luby PDF was not accessible, although the theorem was independently corroborated in published work.

## Value — PASS
This closes a natural algorithmic distinction singled out by the 2026 PAV and structured-Thiele literature: optimal committees can be constructed efficiently with just two supporters per candidate, and in this particular balanced setting even the optimal score is fixed in advance, but the number of tied exact optima remains \(\#\mathrm{P}\)-complete. The conclusion applies uniformly to a nontrivial family of Thiele objectives under a sharp pointwise score-separation condition; it is not an arbitrary fixed-size census. The counting complexity is relevant to measuring unresolved choice and downstream exact tie enumeration.

## Closest literature and limitations
Ai (arXiv:2609.08884, Sec. 5–6), Lassota–Sornat (AAAI 2026, Sec. 5.1 and conclusion), Janeczko–Faliszewski (arXiv:2305.01769, Sec. 4), and Dagum–Luby (TCS 1992) were compared by mathematical statement and implication. The result concerns the rigid degree-bounded graph-induced election family; it does not extend the counting hardness to planar source graphs or fixed committee size. Independent checking of historical priority remains open.

Self-review: passed. Independent audit: not yet performed.
