# Scientific review: palindromes of Kimberling's binary word

## Correctness — PASS

The claim is precisely for the infinite binary word \(B=0\pi(T)\), with \(\pi(0)=100,\pi(1)=101,\pi(2)=10\) and the Tribonacci fixed point \(T\). The primary paper proves this morphic representation. Since all \(\pi(\varphi^3(a))\) blocks have length at least \(11\) and the adjacent pairs of \(T\) are exactly \(00,01,02,10,20\), all factors of length at most \(11\) are exhausted by six explicit finite words. The palindrome census has \(P_B(10)=P_B(11)=0\), excluding every longer palindrome by its center. Distinct palindromes total \(15\); the last first appears at the 25th position, giving the sharp defect formula. The finite cover and independent palindromic-tree checker ran successfully; only the cover is used for the infinite proof.

## Originality — PASS within examined sources

The primary paper (arXiv:2510.11318) proves the morphic identity, ordinary factor complexity and critical exponent, but does not give this palindromic classification. OEIS A288462 states the sequence rather than its complete palindrome census. General theorems on complement-symmetric Rote words and reversal-closed low-complexity words do not imply this theorem: the target word's factor language is neither complement-symmetric nor reversal-closed. Published mathematical-record and sequence searches found no equivalent or stronger covering statement. Residual risk: unindexed or unpublished overlapping analysis and historical-priority uncertainty.

## Mathematical value — PASS

For a recently studied binary word of minimum linear ordinary factor complexity among non-Sturmian examples, an exact palindromic spectrum is a natural intrinsic invariant that is not fixed by its ordinary complexity. The complete finite spectrum and its sharp defect-stabilization threshold distinguish this word sharply from complement-symmetric Rote sequences with palindromes at every length. The finite-window structural proof is transferable as a technique, but no general-family theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
