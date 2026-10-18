# Self-review

## Correctness (PASS)

The statement fixes open-neighborhood signatures and open-independence, counts labeled vertex subsets and restricts both factors to sizes at least two. Every selected vertex must have exactly one selected neighbor; the resulting induced components use disjoint row and column footprints. Collision with the mate of a selected vertex forbids empty rows in the presence of horizontal components and empty columns in the presence of vertical components. The proof then verifies full signature injectivity by horizontal/vertical support profiles, rather than incorrectly treating the general two-neighbor necessary condition as sufficient. The labeled allocation denominator accounts for both endpoint swaps and interchange of same-type components. Finite exhaustive and construction checks are independently reproducible; they support but do not establish the infinite assertion.

## Originality (PASS, residual bibliographic risk)

The 2017 introduction by Seo and Slater and the 2021 preprint/2022 article of Cappelle et al. do not classify Cartesian rook graphs. The second paper's necessary two-neighbor lemma is applicable but expressly not sufficient for graphs of arbitrary girth. Junnila et al. (2018) address ordinary locating and other closed-neighborhood codes on rook graphs, and their later work on direct products/Hamming graphs is likewise about distinct constraints. Published record comparisons concern generic identifying-open-code constructions, codes of chain/threshold graphs, or unrelated rook-neighborhood homology; none implies the exact \(OLD_{oind}\) incidence classification. The comparison is evidence-based, not an assertion that absence from searches proves uniqueness. An undiscovered or unindexed equivalent theorem remains possible.

## Value (PASS)

Existence of open-independent open-locating-dominating codes is hard on unrestricted graphs. Here the full natural two-parameter Cartesian clique family admits a sharply arithmetic existence criterion and a complete set census. In particular, square boards are feasible exactly at side lengths divisible by three. The result combines sensor distinguishability with a rigid induced-edge constraint, is not a mere computation of one arbitrary small instance, and provides both obstruction and construction across infinitely many parameter values.

## Closest literature and limits

Seo–Slater (2017), DOI:10.5614/ejgta.2017.5.2.2; Cappelle–Coelho–Foulds–Longo (2021/2022), arXiv:2103.07972; Junnila–Laihonen–Lehtilä (2018), DOI:10.1016/j.dam.2018.03.050; Junnila–Laihonen–Lehtilä (2023), arXiv:2306.07862. The argument does not cover higher Cartesian dimensions or factor size one, and independent validation is unperformed.

Self-review: passed. Independent audit: not yet performed.
