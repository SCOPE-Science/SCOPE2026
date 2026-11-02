# Scientific review: excluding the ten-tacnode basket

## Correctness — PASS

The quantifiers are unrestricted over complex projective arrangements of three *distinct smooth* conics and three *distinct* lines with only ordinary nodes, ordinary tacnodes and transverse ordinary triples. The 18 conic--line Bézout units force an even number of conic--line nodes; the basket has just one node, so this number is zero. There are only two projective three-line incidence types: concurrent and triangular. The proof enumerates every permissible assignment of \(CCC\), \(CCL\), \(CLL\), and \(LLL\) triples and excludes each with exact tangency budgets and the two-tacnode common-tangent obstruction. The two near-free vectors arise independently from the published degree-nine syzygy bound, Tjurina identity, Bézout identity and orbifold inequality.

The standalone Python verifier performs an exhaustive over-approximation of these incidence constraints and returns `EXACT_THREE_CONIC_THREE_LINE_INCIDENCE_INFEASIBLE_OK`. This finite check corroborates rather than replaces the unrestricted proof. The verifier deliberately allows some formally consistent non-realizable placements; zero survivors therefore still establish the necessary incidence constraints are unsatisfiable.

## Originality — PASS with residual priority risk

Dimca--Pokora [1, Lemma 5.1] prove the prerequisite common-tangent statement, and their Theorem 5.2 classifies *free* conic--line arrangements. The free classification does not imply the present **unconditional** basket exclusion. Gałecka [2, Sections 4–5] supplies the necessary near-free conditions and leaves degree nine unresolved. Her numerical bounds alone allow both \((1,10,4)\) and \((0,9,5)\). Searches of indexed mathematical records, equivalent singularity-basket formulations, and deduplication against recoverable earlier claims located no identical or dominating assertion. A specialized unindexed earlier incidence argument remains possible, so no uniqueness or independent novelty certification is asserted.

## Mathematical value — PASS

The exclusion settles one natural degree-nine near-free numerical candidate left by general bounds. The new geometric obstruction hinges on projective triangle/concurrency cases and the interaction of line-side tangencies with doubly tangent conic pairs. It is not merely a numerical rewrite, a small arbitrary parameter slice, or an example whose answer was already forced by the cited inequalities.

## Scope and limitations

The remaining basket \((0,9,5)\) is only necessary and may be realizable or impossible. Additional singularity types, singular conics, repeated components, and non-complex fields fall outside the theorem. No external independent audit or validation has been performed.

## Source comparisons

[1] A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349, Lemma 5.1 and Theorem 5.2.

[2] A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969, Propositions 4.1 and 4.4, Section 5.

Self-review: passed. Independent audit: not yet performed.
