# Review: maximal independent sets of two-token complete bipartite graphs

## Correctness — PASS
The independent-versus-pure bipartition of the token graph is verified from its symmetric-difference adjacency. For any maximal independent set, its pure-pair coverage determines uniquely two uncovered subsets; maximality forces their complete mixed rectangle and all pure pairs on the complements. Complement sizes one cannot occur. This is a bijection, proving the polynomial. The integer quadratic identity \(\binom{m-u}{2}+\binom b2+u(n-b)=\binom m2+u(n-m)+(b-u)(b-u-1)/2\) proves minimum cardinalities and counts, with all boundary cases considered. An independent construction enumerated 6,947 maximal independent sets across 15 small instances with full coefficient agreement. Finite enumeration is supporting evidence only.

## Originality — PASS, qualified
The initiating 2025 token-domination paper handles stars and complete graphs, not the exact maximal-independent-set profile here. Earlier independence-number and well-covered-token-graph papers supply only extremal values and general constructions, not the complete formula or minimum-count classification. The two October 2026 papers treat ordinary domination on exactly the same host. In particular the October 22 paper gives a **full domination feasibility criterion**, from which an independence specialization is possible; this substantive overlap is acknowledged, and no discovery priority is claimed for their lemma or ordinary-domination values. The labelled-set polynomial, minimum independent domination number and exact multiplicity were not found explicitly stated in the inspected literature. Residual risk: the result may exist under maximal stable sets, minimal vertex covers of the token graph, or symmetric-square terminology, or be viewed as a relatively direct corollary of the newer lemma.

## Mathematical value — PASS
The result classifies *all* inclusionwise maximal independent sets across an infinite two-parameter graph family, with exact cardinality distribution, sharp independent domination and minimizer counts. The quadratic-versus-linear separation of independent and ordinary domination on balanced hosts is a motivated structural consequence. These invariant and counting questions are mathematically natural for a family whose ordinary domination was only recently determined, rather than a parameter rename or numerical instance.

## Limits and status
The theorem concerns labelled two-token complete-bipartite graphs only; finite tests are not infinite proofs. External historical-priority review and independent proof validation are outstanding. Self-review does not constitute an independent audit.

Self-review: passed. Independent audit: not yet performed.
