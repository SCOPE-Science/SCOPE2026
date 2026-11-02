# Scientific review

## Correctness — PASS

The exact result concerns binary cyclic words with length-seven windows and Hamming radius one. Every word of length at most 22 is represented once by an integer bitmask in the exhaustive census, with cyclic windows defined by modular indexing. The 128-bit OR of eight-member Hamming-ball masks is equivalent to full target coverage. The C and Python implementations independently test every candidate and agree on zero solutions at lengths 1–21 and exactly 132 at length 22. The Python implementation reconstructs both full group orbits, weights, distinct-window counts, and target-coverage multiplicities for every accepted cycle; the C implementation computes the same count, weight histogram and canonical representatives. No infinite or probabilistic inference is made. The claim is supported by the actual enclosed source files, not by a log alone.

## Originality — PASS, with residual historical risk

Chung and Cooper (arXiv:math/0310385, 2003) tabulated length 22 for the same covering parameter; the full preprint's definitions, construction arguments, numerical table, and remarks were inspected. The prior numerical optimum **covers the shortest-length statement**, so shortest length alone is not claimed novel. However, that article does not enumerate all 132 indexed minimum cycles, derive the 44/88 symmetry split or prove forced balance and target multiplicity profile. Chee, Etzion, Ta, and Vu (2025, doi:10.1007/s10623-025-01726-5) exhibit an order-seven radius-one length-22 sequence in Example 26 to construct two-dimensional covering arrays; their open full text was inspected around constructions, examples and appendix, without finding the full optimal-cycle enumeration. The 2026 near-optimal asymptotic study and ordinary Hamming covering-code classification results concern different questions and do not logically imply the new count. Relevant title, alias, numerical, and statement-level research-record searches produced no stronger known result. An unindexed exact census or inaccessible source may still have appeared elsewhere: historical priority is not independently certified.

## Value — PASS

This is the complete solution set for a natural smallest optimal cyclic Hamming covering design of window order seven, rather than a marginal improvement in length. The result distinguishes six rotation classes and two complement/reversal/rotation classes, shows every optimum is balanced, and determines the exact overlap of all radius-one neighborhoods. The parameter is independently motivated: a length-22 order-seven radius-one sequence is used explicitly to build a two-dimensional covering design in Chee et al. (2025, Example 26). The classification identifies every replacement optimal seed and the redundancy distribution available to such constructions. The scope is finite and does not claim that this classification yields a new asymptotic bound.

## Limitations and closest literature

The shortest length 22 is known in the 2003 baseline; the new count and all-optimizer structure are the asserted contribution. The direct exhaustive proof needs at most \(8{,}388{,}606\) candidate-word checks. The 2025 construction does not claim that every alternative seed improves that construction. Literature searches are not a uniqueness or priority certificate, and independent scientific audit is pending.

Self-review: passed. Independent audit: not yet performed.
