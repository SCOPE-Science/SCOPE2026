# Scientific review

## Correctness — PASS

All quantified graph cases have at least three nonempty parts, so the cross-part occupied-neighbor denominators \(H_i=N-s_i-1\) are strictly positive. A within-part jump changes neither utility nor part counts; a cross-part jump has a potential increment exactly equal to the moving occupant's utility increment, verified by explicit one-coordinate quadratic differences. For two colors, the sum of the prospective utilities of separate red and blue deviators from a mixed full part exceeds their present utility sum by \(1/H_j\); hence all full parts must be monochromatic. For pure full parts, the two displayed cross-multiplied inequalities are equivalent to non-improvement, yielding an if-and-only-if equilibrium classification. Labeled vacant vertices, red occupancy choices, and monochromatic full-part choices are counted disjointly in the polynomial. The equal-part polynomial and the \(K_{2,2,b}\) integer feasibility example follow algebraically. Direct graph-based rational enumeration checked 35,349 states and 243,582 legal moves, including the corresponding polynomial coefficients; finite enumeration is supporting evidence, not universal proof.

## Originality — PASS, with residual risks

The 2023 arXiv and 2025 journal full texts of Narayanan–Sabbagh–Voudouris analyze the same fractional unlike-neighbor jump model, but their single-vacancy potential theorem applies to regular graphs and spiders, not general unequal-part complete multipartite graphs. Equal-part potential convergence is **covered** and is not presented as a novel consequence. A previously considered complete-bipartite specialization has only two parts, which does not imply the full-part interaction criterion or the size-dependent arithmetic reentrance with three parts. The 2023 Friedrich–Lenzner–Molitor–Seifert full text uses a single-peaked utility, and the 2025 Li–Narayanan–Opatrny–Xu full text uses swap moves and different utility functions. Targeted searches of mathematical research records and public literature found no implication-equivalent description of the full asymmetric multipartite equilibrium polynomial. The absence of a retrieved result is not proof of uniqueness: older congestion-game embeddings or unindexed treatments might imply the potential, and unpublished multipartite equilibrium enumerations remain a risk.

## Mathematical value — PASS

The equilibrium criterion resolves a complete natural infinite family for a strategically meaningful model: it determines every stable binary assignment, including unequal community sizes and prescribed red counts. Exact coefficient formulas provide the entire equilibrium spectrum, not only existence. The mixed-full-part impossibility is structural, whereas the size-sensitive two-sided inequalities expose an integer nonmonotonicity that is absent from the regular and bipartite specializations: mixed full-part colors can be stable for a vacancy community of size three, unstable at size four, and stable again at size five. This reveals how vacancy-induced normalization and indivisible agent counts affect equilibrium; no downstream theorem or independent validation is asserted.

## Closest work and limits

See the detailed source comparisons and residual risks in `AUDIT.json` and the cited primary papers in `RESULT.md`. Only one vacancy, unconstrained jumps, complete multipartite networks and binary colors for classification are covered. Arbitrary-type potentiality is proved but arbitrary-type equilibrium classification is not.

Self-review: passed. Independent audit: not yet performed.
