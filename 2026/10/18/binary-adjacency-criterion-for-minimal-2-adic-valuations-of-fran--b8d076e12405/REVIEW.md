# Scientific review

## Correctness — PASS

The stated bound and its equality cases follow for every nonnegative index from Strehl's positive-summand identity and Legendre's exact factorial-valuation formula. The valuation of each nonzero summand is the binary digit sum of the index plus two nonnegative carry counts. The zero-carry choices are in bijection with subsets of adjacent-one positions. Their number is a power of two, making the normalized sum odd precisely when the original index has no consecutive binary ones. This establishes an infinite proof, not a computational extrapolation. The separate Fibonacci census is an ordinary two-state enumeration. The standard-library checker reproduces the identity, valuations, and consequences for explicitly bounded inputs.

## Originality — PASS, subject to independent literature assessment

Sun's 2011 preprint proves primarily odd-prime aggregate congruences and does not state this exact binary valuation boundary. Schulte, VanSchalkwyk, and Yang (2014) supply the Strehl identity and explore the Franel valuation tree, including conjectural recurrences and finite observations, without asserting an all-index adjacent-one sharpness theorem. Malik and Straub (2015) establish digitwise Lucas congruences for Apéry-like sequences including Franel numbers; these are congruences modulo primes, not exact valuations or a classification of equality at the digit-sum lower bound. OEIS A000172 records the Strehl identity but not the binary-adjacency criterion. A more general unindexed theorem of binomial-sum valuations may nevertheless imply the result.

## Value — PASS

The 2014 Franel valuation study expressly motivates a deeper understanding of binary valuation patterns. The finding classifies exactly when a canonical digit-sum lower bound is attained, produces an exact count of minimum-valuation terms for every index, and explains the Fibonacci enumeration of sharp indices. This distinguishes a whole infinite, natural subfamily rather than an arbitrary numeric cutoff, while not asserting the still-unknown exact valuation in every nonsharp case.

## Limitations and closest literature

The theorem is restricted to the prime two and to the lower-bound equality frontier. It is not a complete valuation formula; a broader later valuation result or unpublished equivalent remains a possible originality risk. The main comparisons are Sun (2011), the 2014 MSRI-UP report, Malik–Straub (2015), and OEIS A000172. Finite tests alone are not treated as proof of the infinite statement.

Self-review: passed. Independent audit: not yet performed.
