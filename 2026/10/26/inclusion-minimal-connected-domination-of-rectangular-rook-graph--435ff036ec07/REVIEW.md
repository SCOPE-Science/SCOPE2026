# Self-review

## Correctness — PASS

The selected rook squares form an edge set in a complete bipartite row–column graph. Directly, domination is equivalent to occupying every row or every column, and induced connectivity is equivalent to connectivity of the edge-support graph. The proof rules out simultaneous full coverage and cycles, then forces every leaf onto the fully covered side. The sufficiency argument checks each edge-removal case. Bipartite Prüfer coding enumerates the resulting trees with a surjective column-word or row-word, giving the Stirling factors. An independent graph-definition enumerator checked all coefficient dictionaries and all structural forms for seven small boards, including the boundary square and the \(4\)-by-\(4\) board. The argument, not finite extrapolation, establishes the infinite-family statement.

## Originality — PASS with residual priority uncertainty

Mertens's complete primary paper, arXiv:2401.00716 and the 2024 published version, counts all dominating sets via row–column incidence and an edge-cover polynomial; it does not classify the connected, inclusion-minimal subfamily. Abu-Khzam et al., ESA 2022, focus on exact algorithms, lower-bound constructions and complexity for enumerating minimal connected dominating sets in general graphs, without the rook-family Stirling formula. The software documentation listing a minimal-connected-domination polynomial defines an invariant rather than supplying this closed rook family formula. Searches of indexed research records, ordinary and equivalent terminology, and accessible previous claims disclosed no claim implying the stated polynomial. Since exhaustive novelty verification is impossible, unindexed or differently titled work remains a documented risk.

## Mathematical value — PASS

The result counts every inclusion-minimal connected dominating configuration rather than only minimum solutions or all dominating solutions. The one-sided-leaf-tree classification is a structural reason for a nontrivial Stirling enumerator. The exact size spectrum shows a natural family with arbitrarily long gaps between irredundant feasible sizes, already for two-row boards; this gap phenomenon cannot be inferred from the known connected-domination minimum or ordinary domination polynomial.

## Scope and limitations

Finite simple labeled rook graphs of dimensions at least two. An elementary proof and standalone reproducible checks are given; exhaustive computational tests only cover the seven stated small boards. Prior published sources were inspected in the indicated relevant sections, not a claim of having inspected every possible text. Literature-priority risk remains, and no independent audit has taken place.

Self-review: passed. Independent audit: not yet performed.
