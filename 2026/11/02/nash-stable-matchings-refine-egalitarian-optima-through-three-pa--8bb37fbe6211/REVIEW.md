# Review of Nash–egalitarian stable-marriage boundary

## Correctness (C): PASS
The complete finite-domain theorem is established by direct enumeration of every one of the \(46{,}656\) labeled strict three-pair profiles, every perfect matching within each profile, and every unordered pair of its stable matchings. Stability is checked using two independently written blocking-pair implementations. Every one of the \(8{,}304\) comparisons with unequal rank sums has the strictly correct Nash-product order; the minimum gap in every score stratum is positive. The exact optimizer-set histogram is \(43{,}728\) equality and \(2{,}928\) strict Nash-set containment. The twenty-four perfect matchings of the displayed four-pair witness are checked, with exactly two stable outcomes and opposite strict objective preferences. All arithmetic is integral and reproducible with `verify_nash_egalitarian_boundary.py`. The result makes no larger-market claim.

## Originality (O): PASS, subject to priority risk
The September 2, 2026 Desai–Rasheed–Ghalme–Gujar preprint defines exactly the Nash product used here and presents a polynomial-time optimization algorithm plus empirical comparisons with egalitarian matchings. Inspection of its main text and appendices did not reveal an all-profile three-pair ordering theorem, the complete optimizer-set count, or a sharp four-pair reversal. The published egalitarian-versus-regret result studies rank sums versus worst individual rank, whereas the published rank-maximal-versus-egalitarian census studies a lexicographic rank profile instead of the Nash product. Neither entails the present full pairwise Nash-versus-rank-sum implication. Prior small-market research on Nash versus regret is also not sufficient to imply Nash versus egalitarian when egalitarian optima form a proper subset of regret optima. Several exact-statement and equivalence searches in mathematical research records and public literature located these nearby comparisons but no stronger result covering the present claim. Unindexed sources may still contain an overlapping finite classification, and priority is not mathematically provable from search alone.

## Value (V): PASS
The Nash welfare approach was expressly proposed to balance the egalitarian and other fairness criteria while preserving stability. The result identifies the complete initial market range in which a strong exact relation—agreement on *every strict ranking of stable alternatives*, not merely existence of a compatible optimizer—is forced by structure. It also identifies the precise first size at which the criteria can select disjoint unique stable matchings. The exact \(2{,}928/46{,}656\) tie-refinement incidence quantifies how the Nash objective resolves egalitarian ties, distinguishing practical selection differences from genuine fairness conflicts. The result is restricted and finite, but those bounds are a natural minimal structural threshold rather than an arbitrary parameter slice.

## Closest evidence and limits
- Desai et al., *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1, September 2, 2026, full accessible main text and appendix: https://arxiv.org/abs/2609.02354
- Irving, Leather and Gusfield, JACM 1987, DOI: 10.1145/28869.28871.
- Published comparison of egalitarian and minimum-regret stable matchings: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-coincidence-boundary-for-egalitarian-and-minimum-regret-st--57631882a89b
- Published comparison of rank-maximal and egalitarian stable matchings: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-three-by-three-conflict-layer-for-rank-maximal-and-egalita--c67e0358daf3

The finite computation is not an independent audit, and unindexed sources or supplementary tables are possible residual priority risks. The theorem does not extend to arbitrary larger markets.

Self-review: passed. Independent audit: not yet performed.
