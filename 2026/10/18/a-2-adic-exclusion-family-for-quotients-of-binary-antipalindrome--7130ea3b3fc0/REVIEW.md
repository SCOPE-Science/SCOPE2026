# Self-review

## Correctness — PASS
The length-difference inequality fixes the exponent jump from the numerator and denominator's even binary lengths. For \(h=\nu_2(N-1)\), the factor of two in an antipalindromic denominator extends the congruence \(A\equiv B\) by one binary place, while complement reversal propagates trailing equality to leading equality. The shorter-than-prefix case is treated separately and gives an immediate contradiction; the longer case gives the exact ratio lower bound \(2^h/(2^h+1)\) times the forced power of four. The density count partitions every integer by exact valuation, applies precise periodic residue-class counts, and uses concavity to locate the global liminf. No finite computation substitutes for any infinite step. The statement concerns a subset and not the full unrepresentable set.

## Originality — PASS within investigated sources
Bai–Meleshko–Riasat–Shallit (2022), Theorem 18 and Corollary 19, provide the closest method: a fixed three-bit prefix obstruction and the bound \(1/60\). The present assertion is not obtained merely by renaming that theorem: it proves a fresh uniform arbitrarily-long-prefix obstruction involving \(\nu_2(N-1)\), handles the short denominator case, and computes the lower density of its entire valuation-indexed union to give \(0.0881665934\ldots\). Direct reading of the originating full-text sections and searches of related mathematical findings identified no stronger implication. The previously published digit comparison is conceptually antecedent but does not establish this improved constant. Residual risk: equivalent unindexed work, and incomplete coverage of all contemporary literature.

## Value — PASS
The density of the unrepresentable part of an arithmetic ratio set is a central natural question for these numbers, and the cited paper explicitly investigates it and proposes the stronger zero-density conjecture for representables. A quantified more-than-fivefold improvement of the known bound with a closed-form convergent series, relying on all valuations rather than a selected finite digit pattern, contributes a meaningful analytic obstruction. It does not claim to settle the conjecture.

## Sources and limits
Source: Bai et al., arXiv:2202.13694v1, Section 3.4, Theorem 18 and Corollary 19; compare also Theorem 14 and the zero-density conjecture. Finite OEIS A351172/A351173 data serve only as a crosscheck and do not imply an asymptotic density result. Verification is reproducible with the included script; separate external mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
