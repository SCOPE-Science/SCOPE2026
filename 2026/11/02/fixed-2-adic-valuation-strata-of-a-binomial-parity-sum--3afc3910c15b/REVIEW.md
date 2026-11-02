# Scientific review: fixed valuations of a binomial-parity sum

## Correctness — PASS

The exact sum and its positive run-length-transform representation agree with Theorem 13 of Rampersad and Wiebe (arXiv:2309.04012v1). The recurrence has an invertible four-state companion shift modulo each power of two. Its checked length-five and length-ten residue blocks establish the entire classification of the run weights with valuation zero and one. Binary-word factorization proves the multivariate renewal identity. Extracting the constant and first-degree terms gives the two rational enumerators exactly; modular periodicity and a finite coefficient extraction give rationality for all fixed valuation levels.

The smallest positive root of the pentanacci denominator is the unique root on its modulus circle. The pole of the fixed-valuation enumerator has exact order one plus the valuation, since its highest-order coefficient is a nonzero positive power of the one-valuation run series. This supplies positive explicit asymptotic constants. Checking 2,000 defining binomial sums, all words at binary lengths up to 17, and the modular states supports but does not substitute for the symbolic proof. Limits: the published run-length identity is a cited prior theorem; no assertion is made about valuations growing with binary length.

## Originality — PASS within inspected evidence

**Nearest source:** Rampersad and Wiebe, Theorem 13, provides the transform itself, not its 2-adic valuation strata. The new component is the exact one-valuation generating function and the rationality and sharp \(r^v\lambda^r\) law for every fixed valuation, rather than the already available transform identity.

**Known zero-layer coverage:** OEIS A124312 already enumerates binary words avoiding maximal runs of zeros of lengths congruent to four modulo five, which becomes the same zero-valuation enumeration under bit complementation. The zero-layer rational formula is included as a necessary baseline and explicitly not claimed as new. **Related different table:** OEIS A118898 counts exactly one occurrence of four consecutive zeros. Although initial counts coincide, its count at length ten is 136, whereas the one-valuation count here is 138, so it does not cover the new formula. Wu (2022) developed run-length transforms of earlier binomial sums; its inspected abstract and relevant page describe other base sequences. Targeted scholarly and mathematical-record searches did not reveal an equivalent higher-valuation enumeration.

Residual priority risk: a stronger, unlocated digital-word enumeration theorem could imply the exact one-layer formula or all fixed-valuation asymptotics. Search absence cannot prove worldwide novelty. An independent audit of prior literature has not occurred.

## Mathematical value — PASS

The source introduces a natural count of odd binomial products, whose divisibility by powers of two is not classified by merely knowing the original run-length identity. The distinction between zero and one factors of two yields a nontrivial rational function with a squared pentanacci denominator, and the complete hierarchy shows that each fixed extra factor of two introduces an additional power of the logarithmic scale in natural counting. These are exact quantitative statements for infinitely many indices, not a single small numerical instance or a relabeling of the known zero-valuation table.

The result is limited to 2-adic valuations fixed in advance and makes no claim about typical valuation limits, odd primes, or absolute bibliographic priority.

Self-review: passed. Independent audit: not yet performed.
