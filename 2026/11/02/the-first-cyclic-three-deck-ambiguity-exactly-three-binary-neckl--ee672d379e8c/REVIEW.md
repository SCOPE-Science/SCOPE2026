# Scientific review

## Correctness — PASS

The statement concerns only finite lengths \(1\le n\le8\), so complete enumeration is logically exhaustive rather than empirical extrapolation. The direct binomial-coefficient definition is implemented by combinations of positions, covering all \(2^n\) binary words at each length and all cyclic cuts of every canonical representative. The recurrence provides a second implementation of the same invariant. Every canonical necklace is checked for genuinely different rotations, not merely different root indices. The complete exceptional lists and overall distribution are verified with exact integer assertions. A separate two-binomial cut identity supplies a transparent structural consistency check. Replay of the standalone code returned `VERIFY_OK`. No unproved infinite claim is made.

## Originality — PASS, qualified

The 2013 work of Rigo and Salimov defines and develops the same binomial equivalence relation, but its material results concern infinite-word factor complexity rather than identification among rotations of an arbitrary circular source. Chrisnata and coauthors compute global numbers of binary three-decks, notably \(D_3(7)=126\) and \(D_3(8)=247\); those totals alone do not determine the intra-necklace equivalence classes or the sharp cyclic cutoff. Prior results for complete finite Thue–Morse iterates already include the necklace `00101101`; that instance is acknowledged and excluded from the claimed distinctive novelty. The new component is the **complete three-necklace universal classification** and the sharp no-earlier-ambiguity assertion. Comparison with published sources and accessible prior scientific claims found no implication establishing that complete assertion. The 2019/2023 global-deck source could only be inspected through its accessible publisher abstract and table; a finer unindexed calculation remains a residual historical-priority risk.

## Value — PASS

This resolves a natural minimum-length question for a standard short-subsequence reconstruction channel when the receiver must distinguish different starting cuts of the same circular word. It demonstrates that global three-deck nonuniqueness at length seven need not imply any circular-root ambiguity and gives a complete first-obstruction census at length eight, not an arbitrary finite slice. The precise list of five pairs makes the boundary reproducible and available as a benchmark for algorithms handling cyclic source ambiguity. The conclusion is finite and self-contained; it is not claimed to solve general sequence reconstruction.

## Sources and remaining limits

Rigo–Salimov (2013 open manuscript) establishes the relevant equivalence; Chrisnata et al. (2019 conference version, 2021 online/2023 volume) gives global-deck enumeration; the previously established Thue–Morse rotational case covers a proper subfamily. Historical priority beyond indexed and accessible literature is not independently established. All completeness assertions concern the stated finite domain only.

Self-review: passed. Independent audit: not yet performed.
