# Self-review of Binary-weight trichotomy for the ternary-step binomial GCD

## Correctness — PASS

For \(N=3n\), the exact identity \(\nu_2\binom Nt=s_2(t)+s_2(N-t)-s_2(N)\) reduces the GCD valuation to a minimum over positive proper multiples of \(3\). A proper binary submask divisible by three exists for every \(s_2(N)\ge4\), by classifying one-bit exponents according to parity. At weights two and three no such submask exists. The proof constructs an admissible binary-weight-two decomposition for each admissible weight-two or weight-three row, attaining valuations two and one respectively. All quantifiers, the adjacent-bit boundary, and the exclusion of \(n=1\) are explicit. The independent binomial integer GCD and carry-formula checks replay over the documented finite ranges; they are not the infinite proof.

## Originality — PASS

McTague (arXiv:1510.06696v5) proves a congruence-restricted binomial-GCD criterion and already records \(\nu_2\binom63=2\), which the present theorem does not claim as new. Wu (arXiv:2606.20940v2) addresses the same GCD family but not the missing \(p=2,m=3\) case for every row. Fairfax-Ball (arXiv:2610.01328v1, Theorem 4.3) proves the global maximum \(2\), while Remark 8.4 acknowledges the first instance; neither gives the exact three-fiber binary-weight classification. Full texts of these three relevant primary papers, six claim/alias searches in a published mathematical-results index, targeted literature searches, and OEIS checks identified no equivalent or stronger statement. The risk of unindexed results is retained.

## Value — PASS

The result closes the first arithmetic residue-class exception explicitly highlighted by McTague and left unclassified by the more recent global-maximum theorem. It determines, for **every** admissible row, all three possible valuation levels via a short intrinsic binary invariant. This is a natural exact structural classification of the local obstruction and not an isolated computation or artificial parameter cutoff.

## Limits

Only the \(2\)-adic component of the selected GCD at step three is determined; odd factors, other steps, and other primes are not classified. The result is self-reviewed, not independently audited.

Self-review: passed. Independent audit: not yet performed.
