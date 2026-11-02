# Scientific review

## Correctness — PASS

The claim is stated for every ternary circular word length, with alphabet labels fixed and equivalence only under cyclic rotations. A balanced profile has a circular realization precisely when its active directed support is connected. The exact number of indexed words in each profile comes from the directed matrix-tree/BEST formula after quotienting equal arcs; consequently the number of necklaces is bounded below by its normalized expression. The proof separates periodic directed simple-cycle exceptions from primitive one-necklace profiles. Flow conservation yields a unique off-diagonal normal form. Its tree factor, factorial ratios and loop-binomial factors are computed explicitly, and a nonnegative-polynomial comparison rules out every remaining core configuration. The eleven disjoint families of one-necklace profiles sum to the asserted six-residue formula. The two delivered checkers passed: exact BEST/Burnside versus the classification through length 25 and direct-word versus the result through length 12. These finite checks are corroboration, not a substitute for the symbolic all-length argument.

## Originality — PASS, qualified

Jacquet, Knessl and Szpankowski, *Counting Markov Types* (2010), evaluate the ternary balanced-matrix generating function. Their fuller paper, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs* (2012), distinguishes connected realized profiles from disconnected balance solutions, supplies asymptotic type counts, and cites a general exact type-class formula. The present claim does not merely count balanced matrices: it counts profiles whose **fiber modulo cyclic rotation has cardinality exactly one** and gives a complete all-length classification and degree-two quasipolynomial. These results are not asserted in the inspected articles, and their general identities do not give the evaluated single-necklace count without the additional factorial-rigidity classification.

Grisales, Labelle, Posada and Dimitrov (2022) enumerate loopless digraphs with one edge-distinguished Euler tour as vertex count varies; Obscura Acosta and Tomescu (2023 preprint, 2024 journal article) characterize uniqueness of edge-distinguished Eulerian circuits. Neither directly counts cyclic ternary bigram profiles with repeated **indistinguishable** transitions and self-loops as edge count varies. Relevant indexed research results on binary linear adjacent-pair spectra and ternary strict ranking feasibility were compared by their claims, not only titles. None implies this statement. Residual risk: unindexed historical work on circular word reconstruction or specialized Markov-type fiber enumerators may have the same sequence.

## Value — PASS

An exact adjacent-pair spectrum is a classical and practically motivated finite-resolution observation of circular words. Distinguishing a uniquely reconstructible profile from one with multiple necklaces is a substantive reconstruction invariant, not the mere number of admissible profiles. The exact answer in every length, structural characterization, and explicit period-six correction identify a sparse quadratic set within a larger degree-six class of realizable ternary Markov types. The proof also handles nonprimitive repeated cycles, for which an indexed-word singleton count would be misleading.

## Limits and closest literature

The claim is for a three-symbol alphabet and complete cyclic ordered-pair counts. It does not provide class-size distributions for nonunique profiles, a general alphabet formula, or independent priority certification. Named source inspections and reproducible computations provide same-author methodological checks but cannot replace independent scientific review.

Self-review: passed. Independent audit: not yet performed.
