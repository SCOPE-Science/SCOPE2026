# Scientific review

## Correctness
PASS. The position-parity interleaving identity follows directly from the Zimin recursion. Its strict alphabet separation proves the suffix-array recurrence, and the all-\(a_1\) odd-position structure proves that proper-prefix comparisons are unchanged when suffixes are replaced by cyclic rotations. Exact predecessor letters yield the transform and the exceptional run count at rank two. The independent Python checker verified every suffix order through rank 11 and full rotation order through rank 9. Finite tests do not replace the proof of all ranks.

## Originality
PASS, qualified. Actual semantic searches for Zimin/ruler BWT blocks, suffix-array recurrences, and the exact \(2n-1\) run law found no dominating result. Prior examples of \(abacaba\) already give the rank-three transform, including the Tribonacci example in Brlek et al. (2019), which is expressly excluded from a claim of low-rank novelty. Simpson–Puglisi (2008) analyzes completely clustered transforms on arbitrary alphabets rather than the alternating Zimin block structure. Prior prior on Zimin factor automata concerns languages and transitions, not lexicographic suffix order; prior binary Cantor BWT results involve another family. The full text of Restivo–Rosone (2009) was not accessible; the available abstract addresses one-block-per-letter transforms and remains a historical-priority risk, rather than a proved source of the present formula. Searches do not prove uniqueness or absolute priority.

## Value
PASS. The theorem characterizes a canonical compression and indexing transform of a classical recursive word family at every rank, including all block lengths and the original row, without expanding its exponential-length input. The \(O(\log |Z_n|)\) run-size law and exact suffix-array permutation are useful structural test cases for BWT and succinct indexing. The value is the complete symbol-resolved classification, not merely an easy alphabet-size lower bound. There is no claim of optimum among words with the same alphabet.

## Closest literature and limits
See Burrows–Wheeler (1994); Simpson–Puglisi (2008); Restivo–Rosone (2009, abstract available); Fici et al. (2014); and Brlek et al. (2019, full text inspected). The claim concerns sentinel-free cyclic BWT of literal finite Zimin words with increasing alphabet order; it excludes appended-terminator variants and arbitrary alphabet relabelings. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
