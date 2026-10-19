# Scientific review

## Correctness — PASS

The complete 27-trigram property and tight counting force every nine-position candidate to be the single set \(E=\{3,6,\ldots,27\}\). The explicitly tabulated residue obstruction excludes it for each possible cut. Adding one mark hits the sole previously uncovered bigram, while length-three uniqueness propagates coverage to all longer factors. The standalone checker reruns direct coverage of every substring for all 27 cuts. The finite case is fully covered; there is no inference about untested lengths or cycles.

## Originality — PASS, with limits

Whittington (2024, §5, Theorem 29) asks the all-de-Bruijn-cycles unfolding question but only proves existence for selected Lyndon-generated cycles at prime orders. His example of an unfavorable single cut has a favorable alternative cut and therefore is not the present all-cuts counterexample. The 2019 Mantaci et al. general attractor bounds and the 2023 Fuchs–Whittington decision-complexity result do not imply the exact instance. The accessible indexed research and historical claims searched by literal word, unfolding synonyms, and implication yielded no matching example. Equivalence in unindexed literature remains a live originality risk.

## Mathematical value — PASS

This answers the explicit universal-versus-existential question about de Bruijn unfoldings in the negative. It supplies a concrete small word, a proof that every standard unfolding misses the tight nine-mark threshold, and the sharp optimum ten. It does not classify maximal attractors among all de Bruijn cycles.

## Closest literature and limits

Primary: P. Whittington, *Online String Attractors*, arXiv:2407.15599v1, §5 (2024); S. Mantaci et al., *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (2019). The finding addresses one explicit finite counterexample, not the separate conjecture that some favorable cycle exists for every order/alphabet. Indexed searches and self-review are not an independent external validation.

Self-review: passed. Independent audit: not yet performed.
