# Scientific review: Padovan enumeration of alternating-host MAS

## Correctness — PASS
The proof gives an exact and independently checkable greedy subsequence embedding cost \(c(u)=2L-r+s\). The complete classification of one-letter deletion effects yields two disjoint exhaustive families of minimal absent subsequences, with a separate treatment of single-letter candidates. Weighted-run rational generating functions count each admissible word once; exact coefficient extraction proves the recurrence and Padovan shift. The shortest-absent count has a separate exact run-count proof. The attached script exhaustively checks 349,504 binary candidate words for eight hosts, including every deletion and shortest-absent count, plus 100 symbolic recurrence values. Finite checks corroborate rather than prove the infinite statements.

## Originality — PASS with disclosed residual risk
The most relevant first primary source, Kosche et al., arXiv:2108.13968 (2021), characterizes MAS generally and exhibits an exponential-versus-polynomial MAS/SAS gap for alphabets of size at least four, but does not in its inspected results provide this binary alternating-host enumeration. Adamson et al., arXiv:2407.18599 (2024), bound all absent length-specific subsequences, rather than total minimal absent subsequences for a fixed periodic host. Manea et al., arXiv:2504.21471 (2025), give general enumeration algorithms but not the inspected explicit infinite-family generating function. The numerical sequence is pre-existing Padovan (OEIS A000931): no novelty is claimed for the numbers alone. An accessible published-result summary about Fibonacci extremals counts shortest absences over all binary hosts, not all minimal absences in the alternating host; its full text was unavailable. A hidden equivalent specialization remains possible, hence originality is a best-evidence conclusion, not a proof of unique priority.

## Mathematical value — PASS
Prior work explicitly studies the combinatorial gap between minimal and shortest absent subsequences and gave a four-symbol construction. The proof here identifies a particularly simple two-symbol periodic family realizing an exponential-versus-linear gap, with an exact Padovan rational generating function and exponential constant. This is a structural enumeration of a natural object motivated independently of the resulting integer sequence, and it is neither a routine restatement of the general MAS decision procedure nor merely a small numerical census.

## Limitations
No claims about the maximum number of MAS for arbitrary binary words, or independent assessment, are made. A potential implicit result in unindexed literature cannot be ruled out; the most closely relevant public-result summary could not be checked against its full text. Earliest cited public source is the August 31, 2021 version of arXiv:2108.13968.

Self-review: passed. Independent audit: not yet performed.
