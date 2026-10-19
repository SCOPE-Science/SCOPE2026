# Scientific review: repeated-permutation scattered-palindrome spectrum

## Correctness — PASS

The claim concerns the full \(q\ge3\), \(k\ge1\) family, not a finite table. Every subsequence of \((a_1\cdots a_q)^k\) requires one block plus the number of non-increasing adjacent rank changes. This is both a necessary condition (ranks inside one block strictly increase) and sufficient by an explicit left-to-right greedy embedding. For palindromes, reversal pairs each non-equal adjacency with exactly one weak descent and each equal adjacency with two weak descents; the even central equality gives the remaining descent. This proves the minimum-block test \(1+m+e(h)\le k\). Counting adjacent equalities in the determining halfword proves both length formulas and hence the rational generating function. The maximal length, number of maximal palindromes, contiguous-factor comparison, and exponential growth all follow without extrapolating examples.

The standalone checker enumerates all distinct subsequence values in 21 small cases, checks 150 alphabet permutations, and uses a second independent embedding method in bounded ranges. These tests corroborate the proof but are not treated as an infinite certificate.

## Originality — PASS, with residual uncertainty

The first public motivating source is Pandoh’s June 21, 2021 seminar slides; the closest longer primary source is Mahalingam–Pandoh (arXiv:2108.02729), studies general scattered-palindrome bounds, some length-three cases, and extremal counts when the alphabet size is at least half the host-word length. Its statements do not determine the complete by-length spectrum of an arbitrary number of repeated copies of one alphabet permutation. Müllner–Ryzhikov (arXiv:1901.07502) treats lengths of longest palindromic subsequences and circular-word extremal constructions, not this enumerator. Published-record searches under repeated permutation, cyclic alphabet word, palindromic subsequence, and rational generating function formulations did not reveal an implication covering the theorem. The separately known alternating binary case is excluded from the new scope.

The general ability to count distinct palindromic subsequences algorithmically at each individual input is not a symbolic closed formula uniformly in both parameters. A prior unindexed formula or an implicit equivalent in another source remains a residual risk; no claim of exhaustive bibliographic uniqueness is made.

## Mathematical value — PASS

The classical question of how many different palindromic subsequences a word has is distinct from merely finding its longest one, and the canonical word consisting of repeated complete alphabet sweeps is a natural structured test family. A single uniform theorem resolves **every length coefficient** for an infinite two-parameter family, reveals a second-order generalized-Fibonacci recurrence, and establishes exponential scattered complexity despite constant contiguous palindromic complexity. Its membership criterion explains the phenomenon rather than just tabulating outputs. It makes no unsupported claim of optimality over arbitrary words.

## Closest literature and limitations

The June 2021 seminar slides and subsequent scattered-palindrome paper provide the motivating global counting context and two-copy example; the 2019 paper studies different longest-subsequence questions. The result does not cover arbitrary concatenations of different permutations, near-palindromes, counts of embeddings, or global maximum/minimum complexity among all words of a fixed length. External bibliographic indexing is incomplete and independent mathematical validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
