# Scientific review: Fibonacci minimal absent-subsequence antichains

## Correctness — PASS

The definitions concern distinct words absent as scattered subsequences, with every one-position deletion present. The proof invokes the original Theorem 3.1 of Kosche et al. for greedy minimal-absence; its four conditions are checked against the transition rule. A complete classification of reachable greedy pair states shows exactly two first-position incoming groups for runs 3 onward, with Fibonacci multiplicities, and one uniform multiplicity for all interior positions. Termination is possible only at the last positions of the two final runs or the first position of the last run. These cases yield exact terminal counts \(\(F_r\)\) and \(F_{r+1}\). The two-run base is checked separately. Each choice of letters determines a unique greedy path, so the proof does not overcount embeddings. Independent brute-subsequence enumeration and path dynamic programming agree in 124 finite cases. No finite experiment is substituted for the induction.

## Originality — PASS, with residual risk

The closest general criterion is Kosche et al., arXiv:2108.13968, Theorem 3.1; the supplied example for \(0011\) is the first member of this family, not the infinite formula. Adamson et al., arXiv:2407.18599, study numbers of all absent subsequences at fixed lengths and universality indices, a different statistic. The subsequent arXiv:2504.21471 studies output-sensitive MAS enumeration, not this Fibonacci run invariant. A related published count for \((01)^k\) concerns undoubled runs, and does not imply the result for arbitrary lengths at least two. Searches for Fibonacci MAS, alternating run dilations, absent subsequence antichains, and exact boundary counts did not identify equivalent statements. Since indexing is incomplete, an equivalent historical theorem remains possible; this is self-review, not independent validation.

## Mathematical value — PASS

The theorem completely evaluates a natural combinatorial invariant on an infinite family with unbounded run count and *arbitrary* run lengths, proving non-obvious invariance under run dilation and an exact split by terminal symbol. It exposes a Fibonacci state-transition mechanism in the boundary of the scattered-subsequence downset, a useful structural comparison point for the effect of isolated runs and alphabet extension. No claim of wider algorithmic improvement is made. The result is not merely a finite census or substitution into a pre-existing explicit run formula.

## Scientific limits

Requires a binary alphabet, at least two runs, and minimum run length two. Does not evaluate the entire MAS length spectrum, nor extend to one-letter runs. The literature comparisons are fallible, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
