# Scientific review: period-doubling net occurrences

## Correctness
PASS. The five-piece maximal repeated-prefix profile is proved for every \(n\ge3\) by an explicit eight-block match and a parity-based induction. A general lemma then equates net occurrences with nondecreasing adjacent profile entries, giving exactly five starts and lengths. Boundary conventions, overlap of occurrences, arbitrary suffix comparison positions, and the final suffix-length truncation are handled explicitly. Independent finite suffix-array and direct-brute-force checks corroborate the theorem.

## Originality
PASS within the examined literature. Guo and Kishi's complete 2025 article proves three and nine net occurrences in Fibonacci and Thue–Morse iterates, not period-doubling. Kishi et al.'s 2026 occurrence-preserving-morphism paper likewise concerns those two applications. Banbara et al.'s full 2026 paper determines smallest attractor pairs for period-doubling iterates, not their net occurrences or all-position longest repeated-prefix profile. A related shortest unique factor characterization addresses only extremal unique-factor lengths and positions, which do not imply the complete longest-repeat profile. Searches for equivalent net-frequency, minimal unique substring, maximal repeated prefix and period-doubling formulations did not find a covering statement. There remains historical-priority risk from unindexed or differently phrased literature.

## Mathematical value
PASS. The finite period-doubling family is a standard automatic-word test case for substring algorithms. The result closes the natural net-occurrence census for this family with an order-independent exact constant and explicit dyadic positions. The strictly stronger exact profile describes a useful all-position repetitiveness statistic, not merely the final count. The comparison with the known constants for Fibonacci and Thue–Morse words exposes family-dependent behavior of the same invariant. The scope does not include arbitrary prefixes.

## Closest literature and limitations
The closest net-occurrence paper is Guo–Kishi, CPM 2025, DOI 10.4230/LIPIcs.CPM.2025.16. Other pertinent work includes Kishi–Guo–Urbina–Bannai, CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.24, and Banbara et al., arXiv:2602.16152. No independent scientific audit has been performed; finite computations are not infinite proofs. The originality determination is based on inspected accessible materials, not a guarantee of global priority.

Self-review: passed. Independent audit: not yet performed.
