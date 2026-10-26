# Scientific review

## Correctness
PASS. Every legal inverse is a length-\(2k\) palindromic factor. Consecutive palindrome starts collapse to identical parents, proving the run bound. Period-four witnesses attain it for every \(4\nmid k\), and comparing two adjacent retained symbols proves their candidate parents are distinct. The odd-start-count equality case forces all even palindrome starts, whose reflection symmetry forces the stated periodic words. When \(4\mid k\), the first three-start case cannot have two distinct parents. The included finite checker reproduces all tested instances; the infinite statements are proved analytically.

## Originality
PASS, subject to the stated residual risk. The known general palindrome-run upper bound and the length-two specialization are deliberately excluded from claims of novelty. The contribution is sharp attainment for every \(k\ge3\) not divisible by four, exact rigidity of all odd-start-count extremizers for every alphabet, and the boundary obstruction at multiples of four. The 2026 source treats forward two-error multiplicities and a coarse inverse-list bound; the 2017 source does not contain this length-parameter classification. Related inverse-degree results treat distinct error channels.

## Value
PASS. This determines worst-case list-decoding ambiguity over an infinite parameter family, including the complete extremizer geometry when the available-start count is odd. The modulus-four first-onset obstruction shows a genuine arithmetic boundary rather than a simple substitution in the prior length-two case; the result can inform inverse-list degree estimates for duplication confusability graphs.

## Remaining limitations
The extreme-value law for \(4\mid k\) at longer blocklengths and the full classification for even start counts remain unknown here. Unindexed prior calculations cannot be excluded. The reviewed checker is corroborative and does not replace the proof.

Self-review: passed. Independent audit: not yet performed.
