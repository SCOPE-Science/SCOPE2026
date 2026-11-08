# Independent mathematical audit

## correctness

PASS

Alternating host length 4k−1 covers every balanced binary target via greedy embedding and repeated-adjacent-pair bound. For k<=8, an exact prefix-completion DP tracks for each target the longest greedily embeddable prefix, branches over both appended bits and prunes only when current progress plus remaining host positions is below 2k. This necessary condition cannot remove a solution. Independent C implementation performed exhaustive full prefix-state enumeration at lengths 4k−2 and 4k−1 for k<=7, matching counts [2,10,44,190,800,3266,13018], palindromes and arch-index histograms; for k=8 length30 it searched 30,965,979 prefix nodes and found no host. Reversal/complement Burnside with odd host length gives orbit counts. Thus proof is a justified finite exhaustive computation, not extrapolation beyond k8.

## originality

PASS

Baranwal et al study contiguous antisquares as factors, whereas these are subsequence covers. Adamson covers hosts universal for ALL length-k words and gives the arch characterization; it does not count hosts for only complement-paired targets. Resultary contains broader binary subsequence-universality findings but no matching antisquare-restricted table in examined hits.

## value

PASS

The finite complete spectrum solves a natural restricted-language supersequence problem where the target family has 2^k structured words; the k8 sharp cutoff and k1..7 symmetry/arch census are useful exact algorithmic-combinatorial benchmarks rather than arbitrary single instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
