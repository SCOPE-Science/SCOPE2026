# Scientific review: reverse BWT block transport and order-five joint spectrum

## Correctness — PASS

The unrestricted theorem is proved from an explicit one-cycle binary feedback permutation. The rotation-sorting order equals lexicographic order of its distinct \(n\)-bit prefixes. Computing the predecessor of the forward rotation and the successor of the corresponding reversed rotation gives the two complementary block products, with the second indexed by exact fixed-width bit reversal. Counting unequal adjacencies proves the displayed run-count identities, including the linear/noncircular boundary convention.

The order-five finite statement is exhaustive, not a sampling inference: all \(65536\) feedback masks are tested and the unique 32-state cycles are selected. An independent Euler-tour enumerator reproduces the same \(2048\) necklaces. For each cycle, direct rotation-sorted BWTs of the word and reverse agree with the symbolic products; the two independent enumerators agree on the whole 36-cell distribution. The supplied standalone checker is replayable, prints `VERIFY_OK`, and records an extremal witness. Counts and quantifiers apply only to the stated cases.

## Originality — PASS, with historical uncertainty

The original 1994 Burrows–Wheeler report defines the cyclic-rotation transform. Higgins's 2012 de Bruijn analysis characterizes the complementary blocks but does not identify their **forward-to-reverse bit-reversal permutation**. Giuliani and collaborators (2020) establish large BWT reversal sensitivity using Fibonacci-plus and standard-plus strings, not de Bruijn cycles. Lipták and Parmigiani's 2024 BWT de Bruijn slides describe generation from complementary block orientations, without an explicit reversal law; the full conference paper was not accessible. Fici and collaborators' 2025 survey presents de Bruijn BWT structure and reversal sensitivity in separate sections and no joint de Bruijn reversal census.

An earlier forward-only exact order-five BWT-run census provides the marginal counts but does not specify the matching between a cycle and its reversed cycle, and therefore does not determine the 36-cell joint table or sharp individual reversal gaps. Searches for bit-reversal block transport and order-five reversed-run joint tables found no equivalent source. The earlier marginal is explicitly *not* presented as novel.

**Residual priority risk:** the inaccessible full 2024 construction paper or another unindexed source could contain the bit-reversal transport rule. No inference of uniqueness is made from a negative search alone; the positive comparison is at the level of the mathematical statements, including distinctions between BWT, its inverse, and reversal of the source string.

## Value — PASS

BWT run count directly controls run-length indexing and serves as a standard compressed-structure complexity measure. Reversal is a natural operation in sequence processing, while binary de Bruijn words have identical circular factor coverage, making them a clean benchmark for the variability of that measure. The unrestricted structural law converts a difficult lexicographic reranking question into fixed-width bit reversal of a finite feedback table; it is reusable at every order. The exact order-five joint classification identifies the first substantial reversal gap, eight sharp extremizers and 648 equal-run cases, facts that cannot be inferred from an isolated one-sided distribution. The result is more than a cosmetic reparameterization or a recomputation of a known one-variable table.

## Limits and status

The all-order result is binary and sentinel-free and concerns cyclic rotations. Only the \(n=5\) joint table is exhaustively classified. No closed-form higher-order reversal-gap extremum is claimed. No independent mathematical audit or complete historical-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
