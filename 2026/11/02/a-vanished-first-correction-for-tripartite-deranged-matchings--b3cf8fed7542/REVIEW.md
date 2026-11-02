# Assessment of the tripartite deranged-matching correction

## Correctness

PASS. The known finite inclusion–exclusion formula is reproduced from the exact matching count, normalized, and expanded using explicitly derived falling-factorial logarithms. A cutoff at \(m^{1/10}\), absolute factorial tail bounds, and uniform polynomial remainder estimates justify the exchange of asymptotic expansion and summation up to an \(O(m^{-3})\) error. Rational polynomial moments give the vanishing first correction and the nonzero coefficient \(3/128\). Independent vertex-mask counts for three sizes and exact symbolic coefficient checks from `verify.py` passed. The finite computations corroborate, rather than substitute for, the infinite argument.

## Originality

PASS under available evidence, with residual publication-priority uncertainty. Johnston–Kayll–Palmer, arXiv:2209.11319, equation (7), already supplies the exact triple sum and the leading limit. Spiro–Surya, arXiv:2211.01872, and Granet–Joos, arXiv:2301.10131, prove general Poisson limits, not the second-order zero-overlap coefficient. Deng, arXiv:2505.13799, considers multivariate Poisson limits and explicitly identifies convergence rates as a further problem. Record and publication searches for the same graph, coefficient, aliases and rate did not identify the \(3/128\) term. A stronger unindexed error expansion cannot be ruled out by search alone; the new proof is essential to the claim.

## Value

PASS. Quantifying the convergence of tripartite deranged matchings is motivated by the classical matching derangement problem and subsequent Poisson approximations. The cancellation of the naturally expected \(m^{-1}\) contribution reveals a second-order effect; its exact nonzero coefficient distinguishes this zero-overlap probability from a generic first-order Poisson approximation. This is not asserted to solve the general multivariate rate problem or to imply an unspecified downstream theorem.

## Scope and risks

The result covers one zero-overlap probability in the balanced three-part family and gives an asymptotic, not an explicit finite error bound. The exact finite sum and leading limit are credited as prior results. Priority against unindexed works is not certified. No external mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
