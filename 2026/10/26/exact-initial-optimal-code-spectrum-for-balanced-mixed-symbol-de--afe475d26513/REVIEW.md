# Scientific review

## Correctness
PASS. The balanced-output shadow exactly describes one-zero/one-one deletion, because a balanced word losing two symbols and remaining balanced must have lost one of each. The channel-compatibility graph has a direct pairwise-output definition. The standalone checker builds it from all deletion pairs, uses a provably valid greedy-coloring clique upper bound, and exhaustively establishes both the optimum code sizes and all optimum-codebook counts for five specified lengths. It directly rechecks all enumerated codebooks against channel outputs and checks all symmetry images. A separate exact integer-program calculation recovers the maximum sizes, but is not needed for replay.

## Originality
PASS under examined coverage, with residual risk. Cullina–Kulkarni–Kiyavash (2012) use full two-deletion confusability on constant-weight source layers and list aggregate constructions, not the exact different-symbol-only codebook counts. Guruswami–Håstad (2020), §§1 and 5, construct efficient codes correcting unrestricted pairs and distinguish the mixed-symbol case in their decoding analysis, without computing the present finite optimality/multiplicity profile. Targeted published-record searches found no equivalent or stronger claim and no relevant tabulation. The possibility of an unindexed small-parameter enumeration remains.

## Mathematical value
PASS. This is a natural finite benchmark for composition-constrained synchronization coding with a restricted corruption type. The exact size and complete multiplicity/symmetry census reveal sharp small-length behavior; notably the length-ten optimum of ten has 666 distinct codebooks in 174 symmetry classes, instead of merely a feasible code or asymptotic bound. The contrast with unrestricted two deletions in the same balanced source class demonstrates the significance of knowing the deleted-symbol composition. The finite cutoff is explicit, with no unsupported extension.

## Closest literature and limitations
The foundational graph model is known. The new content is the precise mixed-symbol channel optimum and labeled optimum-codebook census for the specified sizes. Related unrestricted-channel work does not imply the results. Full independent mathematical validation has not been performed, and matching results in unindexed literature cannot be completely ruled out.

Self-review: passed. Independent audit: not yet performed.
