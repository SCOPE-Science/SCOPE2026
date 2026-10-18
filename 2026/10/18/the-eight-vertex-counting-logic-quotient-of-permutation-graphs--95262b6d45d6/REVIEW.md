# Review of the permutation-graph counting-logic quotient

## Correctness — PASS

The property is finite and exhaustively enumerated. Every permutation graph is an inversion graph, so traversing all \(n!\) permutations covers the relevant class at each order. Exact globally interned colour refinement classifies \(C^2\) equivalence, and exact graph isomorphism deduplicates representations within each signature. All partitions are identical after \(n\) versus \(2n\) rounds. The authoritative program reproduces 5,699 isomorphism types and 5,654 logical classes at order eight, with 41 nontrivial classes of multiplicities 38, 2, 1 for sizes 2, 3, 4. A separate implementation corroborates the table. The small examples' adjacency masks, edge counts and logical equivalence are independently testable. Nothing beyond order eight is asserted.

## Originality — PASS, with residual risk

Published catalogs and OEIS already give all raw permutation-graph isomorphism totals and are not the claimed contribution. Arvind et al. (2015) establishes the general counting-logic/colour-refinement identification and biregular-switch obstructions, and Guo et al. (2023) gives a dimension-18 upper bound for permutation graphs. These statements do not provide the exact one-dimensional logical quotient, sharp two-pair six-vertex obstruction layer, or full multiplicity distribution through eight vertices. Multiple targeted published-research-record searches did not locate equivalent finite counts. The main priority risk is a previously unindexed specialized enumeration or an explicit consequence of a general classification that was not found; failed search is not proof of novelty.

## Value — PASS

Permutation graphs form a classical graph family whose graph-isomorphism and Weisfeiler–Leman complexity have been extensively studied. Quantifying exactly where one-dimensional refinement first loses isomorphism information, and measuring all collision multiplicities at the first several layers, supplies a natural finite descriptive-complexity invariant. The two distinct six-vertex collisions and the eight-vertex quadrupleton demonstrate that the loss is not a single accidental counterexample. Full enumeration and reproducible data are motivated by the precise logical quotient, not the known graph count alone.

## Limitations

Independent audit has not been performed. The result is confined to orders one through eight, with NetworkX graph-isomorphism testing in the exact certificate and a hashed independent corroboration. Earlier published coverage could exist.

Self-review: passed. Independent audit: not yet performed.
