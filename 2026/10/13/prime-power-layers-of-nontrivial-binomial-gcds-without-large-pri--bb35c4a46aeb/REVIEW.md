# Self-review: prime-power layers of nontrivial binomial GCDs

## Correctness

**PASS.** The published binomial-GCD criterion is invoked with \(n=k+1\), and its nontriviality condition is exactly the existence of an exact prime-power component \(p^a\ge\sqrt n\). For integers whose largest prime factor does not exceed \(\sqrt n\), this dominant component has exponent at least \(2\) and is unique. Writing \(n=p^a b\) produces an exact coprimality count, not a heuristic one. Partial summation using the prime number theorem produces the two constants \(2a/(a+1)\) and \(2a/(a-1)\), while the uniform sum over exponents at least \(3\) is smaller by a power of \(X\). The packaged verifier checks the source criterion directly in finite cases and reproduces the exact count independently by factoring each integer; those computations are not used as the infinite proof.

## Originality

**PASS.** Guo–Qiu–Cao–Feng–Gao prove the decisive membership criterion, and OEIS A080170 records the complementary zero-GCD sequence. The primary full text was searched for counting, density, distribution, and asymptotics; it gives no such layer theorem. Claim-specific searches by the source title, exact parameter, \(16/3\) constant, \(3/4\) exponent, equivalent formulations, and mathematical-literature searches found no statement of the same hierarchy. The result expressly depends on the published criterion and classical PNT; it is not described as a new proof of the criterion or a new prime-counting method.

An unindexed equivalent counting formulation remains a residual literature risk. No claim of exhaustive global literature coverage or independent certification is made.

## Value

**PASS.** The square-root threshold is distinguished by the published positivity criterion, not chosen ad hoc. Restricting to integers with no prime factor above the same threshold isolates the complementary *prime-power* mechanism. Its distribution is extremely sparse but has a precise \(X^{3/4}/\log X\) scale, and every fixed prime-power exponent belongs to a coherent hierarchy of different scales and exact rational constants. This addresses a natural quantitative question left untreated by the source's membership theorem; it is not merely a single computed value or arbitrary subfamily.

## Literature and limits

The closest reference is arXiv:2606.22997v1, especially Theorem 1 and Lemma 9; OEIS A080170 is the original database entry. The new results require that classification as an input. They provide fixed-exponent asymptotics, not a uniform growing-exponent estimate or a formula for the actual positive GCD values.

Self-review: passed. Independent audit: not yet performed.
