# Scientific self-review

## Correctness — PASS

The theorem classifies the entire MUS set, not only a selected family of unique factors. The decisive proof steps are (i) the pairwise disjoint phase-four-factor sets for the two length-three image blocks; (ii) exact transfer of occurrence multiplicities from any output factor of length at least four to its covering parent factor; (iii) a bijective lift of all parent MUS intervals of length at least three; (iv) direct classification of the nine-symbol base word and the absence of unique factors of length at most three in later iterates; and (v) induction on all lengths and intervals. Every boundary is treated with zero-based half-open intervals. The standalone verifier checks the exact formula through iteration eight, independently checks the smaller words via all-factor counting, and exhaustively tests 3402 parent-occurrence identities. Finite computation is corroboration only; the induction proves the infinite statement.

## Originality — PASS, subject to residual priority risk

The closest 2026 source [1] explicitly identifies the substitution as strongly interference-free and proves general occurrence-preservation implications. It classifies MUSs of Fibonacci and Thue–Morse iterates, not the five intervals for this substitution. A generic factor-count preservation criterion does not itself identify the minimal unique factors: the four-symbol synchronization and boundary-lift coverage are additional arguments. The 2025 MUS crossing-count paper [2] and the 2019 sliding-window paper [3] address general bounds and algorithms rather than the exact family. The standard Mephisto–Waltz sequence descriptions [4,5] contain the morphism but not this classification. The prior related finite-iterate MUS classification for a different binary morphism uses a different substitution, four rather than five intervals, and different scaling. Targeted scientific-record and web searches found no covering claim, but such negative searches cannot establish absolute priority.

## Value — PASS

The primary 2026 morphism study names fixed points of strongly interference-free morphisms as a natural direction and gives exact MUS classifications for two other classic morphic families. The present theorem completes the corresponding natural finite-iterate invariant for the named Mephisto–Waltz example. The constant number of MUSs, their length scaling, their exact positions, and the phase-synchronizing explanation give a structural answer applicable at arbitrarily large word lengths; it is not a routine finite table or a renaming of the known Thue–Morse and Fibonacci results.

## Literature limits

Sources [1] and [2] were inspected in accessible full-text HTML in their relevant mathematical sections. Source [3] was inspected in accessible parsed text for its definitions, algorithms, and scope. The reference listings [4,5] were checked for the morphism and known properties. Unindexed work or an unpublished equivalent derivation could change the priority assessment. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Kishi et al., *On Occurrence-Preserving Morphisms*, arXiv:2605.18034v1 (2026), https://arxiv.org/html/2605.18034v1.

[2] Fujimaru et al., *On the number of MUSs crossing a position*, arXiv:2508.16092v1 (2025), https://arxiv.org/html/2508.16092v1.

[3] Mieno et al., *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804, https://arxiv.org/abs/1909.02804.

[4] Wolfram MathWorld, *Mephisto Waltz Sequence*, https://mathworld.wolfram.com/MephistoWaltzSequence.html.

[5] OEIS, A064990, https://oeis.org/A064990.
