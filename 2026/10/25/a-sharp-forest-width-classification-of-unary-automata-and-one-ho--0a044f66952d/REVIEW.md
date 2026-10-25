# Research assessment

## Correctness — PASS
Every non-simple accepting walk in a forest contains a two-step directed reversal; duplication gives every larger accepted length of the same parity. Conversely an eventual parity tail is realized by a directed path with a terminal 2-cycle. A regular language has a finite eventual period and is represented by a path into an even simple cycle. For the one-hole family, an accepting walk of length \(m+2\) must be simple, because removing any immediate reversal would wrongly accept \(m\); the path construction attains the resulting \(m+3\)-state lower bound. All boundary conditions and orientations were considered.

The proof is analytic and applies to all finite automata meeting the stated assumptions. A finite four-state exhaustive forest enumeration independently corroborates the parity property but is not used as an infinite proof.

## Originality — PASS, with residual risks
The 2026 bipartite-cactus upper bound is broader in the represented regular-language class but does not imply a forest characterization; the 2021 symmetric-edge model is narrower in allowed arc orientations. Accessible own claims about modular residues and modular rays in bipartite cactus automata do not imply the present classification or the one-hole cofinite state bound. Six actual published-finding corpus semantic searches located no equivalent claim, although a negative search cannot establish originality.

The 2026 full text was inaccessible; a corresponding appendix result or an unindexed oriented-tree-automata theorem is the main originality risk. Closest papers: Grobler–Koziel–Siebertz (2026), arXiv:2610.11717; Kutrib–Malcher–Schneider (2021), DOI 10.1007/s00236-021-00402-0.

## Value — PASS
The newly established general bipartite-cactus representation makes the exact threshold for lowering undirected support treewidth from two to one a natural structural question. The complete unary-language classification answers it, while the one-hole cofinite family measures an exact and unbounded state cost within the forest class. These statements capture the topology-versus-state-number tradeoff rather than a renamed textbook deduction; the finite enumeration is only supplementary.

## Limitations
The exact state minimum is for a single missing **positive** length. No general tight state-complexity bound is claimed for all eventual parity languages. The bibliographic comparison with the 2026 paper is limited to accessible metadata and abstract; the 2021 paper's text was inspected.

Self-review: passed. Independent audit: not yet performed.
