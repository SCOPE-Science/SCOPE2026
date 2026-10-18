# Self-review

## Correctness — PASS

Every zero cell has open-neighborhood sum equal to its row weight plus its column weight. Partitioning feasible labelings according to whether a row is empty, has weight one, or all rows have weight at least two yields a sharp lower bound. Its equality cases exhaust the two claimed families. Surjection counting and the precise overlap at the transition give the closed labelled-optimum count, including singleton boundaries. The standalone independent exhaustive tests passed on fourteen entire labelling spaces (1,152,264 labelings) and four larger at-or-below-optimum spaces (696,634 labelings). These finite checks supplement the universal proof rather than certify it.

## Originality — PASS, subject to residual bibliography risks

Shao and Zhao, arXiv:2610.00108, discuss counting Italian functions on paths, trees and cycles; they do not treat rook graphs. Varghese and Lakshmanan, arXiv:1910.12260, Theorem 2.4 concerns **perfect** Italian functions on complete-graph Cartesian products, where at a zero the neighbour sum must equal two. Its minimum formula differs on \(m<n<2m\), and it does not enumerate ordinary minimizers. Kazemi, Pahlavsay and Stones, arXiv:1509.08208, treat binary \(k\)-tuple total domination, a different constraint. Mathematical-record searches tested aliases, stronger coverage and exact tables, and found no directly covering formula, but absence from searches is not a priority certificate. Other indexed or unindexed publications remain a residual risk.

## Value — PASS

The classification solves a complete family of natural equality cases and gives a sharp structural phase transition from surjection-controlled placements to rowwise independent weights, including an exact intersection correction. The resulting Stirling and polynomial counts distinguish minimum functions at a recently studied enumerative invariant and quantify the gap from the previously published perfect variant. The result does not cover the full weight polynomial or general product graphs.

Self-review: passed. Independent audit: not yet performed.
