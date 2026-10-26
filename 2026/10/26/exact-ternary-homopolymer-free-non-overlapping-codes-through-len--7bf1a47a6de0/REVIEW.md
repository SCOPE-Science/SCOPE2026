# Scientific review

## Correctness — PASS

For every integer \(2\le n\le9\), the exact predicate is the conjunction of internal adjacent-letter inequality and the absence of every nonempty proper prefix/suffix coincidence across all ordered word pairs, including identical pairs. Removing self-overlapping candidates and building the compatibility graph is bijective with feasible codebooks. The ordered bitset recursion tests every possible maximum clique; the cardinality pruning bound is valid and uses a strict inequality. An independent Bron–Kerbosch pivot search enumerates all maximal cliques and yields precisely the same optimal codebooks at all eight lengths. Its 121728 maximal cliques at length nine contain exactly 12 with size 24. Explicit permutation/reversal transformations independently partition those into two orbits of size six. Each optimum code is checked again using string overlaps. See `RESULT.md`, `check.py`, and `OPTIMA_N9.txt`. No extrapolation from a finite experiment is made.

## Originality — PASS (with residual risk)

Wang and Wang's generating-function paper (arXiv:2108.06934) gives general non-overlapping constructions without enumerating the run-one constrained ternary optima. Stanovnik–Moškon–Mraz (arXiv:2307.12593) give the unconstrained value \(S(3,9)=656\) and the unconstrained maximum-code census, not the constrained result \(H(9)=24\) and its 12 maximizers. Their later paper (DOI:10.1007/s40314-024-03055-0) is particularly close: its structural classification and bounds explicitly encompass run-length-limited maximal codes. The numerical length-two-to-nine optima and symmetry-orbit census were not located in its inspected run-length sections and tables. The general construction makes this question computable, but does not itself report the present exact answers. Relevant published research records and local historical findings were also compared on parameters and implications, not only title keywords. Residual risk: an unindexed exact table or an equivalent computation may exist, and the 2025 framework might yield an alternative derivation.

## Mathematical value — PASS

Cross-bifix separation supplies frame synchronization, while forbidding adjacent equal symbols models a severe homopolymer limit. Their conjunction is not the same as an unconstrained code. For the smallest nine-letter ternary benchmark, the exact maximum is 24 instead of the known unconstrained 656, and the complete maximizing-codebook census consists of exactly two inequivalent types. Exact codebook representatives and orbit sizes provide finite test cases for constrained constructions and optimal encoder design. This is a natural complete finite classification, rather than an arbitrary slice of an unrelated table; it does not claim a general theorem at larger length.

## Closest literature and limitations

The closest direct overlap is the run-length-restricted Construction 5 in Stanovnik–Moškon–Mraz (2025). The precise new contribution is its evaluated ternary length-two-to-nine optimum/census; the established general framework is not claimed new. The finite certificate depends on a replayable exhaustive procedure and covers no length beyond nine. Full independent mathematical auditing has not occurred; complete database uniqueness is not asserted.

Self-review: passed. Independent audit: not yet performed.
