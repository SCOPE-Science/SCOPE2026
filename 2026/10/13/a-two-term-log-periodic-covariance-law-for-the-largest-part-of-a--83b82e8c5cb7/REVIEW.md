# Self-review

## Correctness — PASS

For uniformly random unrestricted compositions, the independent fair cut-bit model identifies the number of parts with one plus the count of ones and the largest part with one plus the longest zero-run. Differentiating the product Bernoulli measure establishes the exact covariance/avoidance-probability derivative identity. The rational generating function for runs of fewer than \(r\) zeros is derived from a unique word decomposition. On the central window \(r=\log_2 n+O(\log\log n)\), a simple pole separated from all other singularities and its differentiated residue yield a uniform error of order \(O((\log n)^{11}/n)\); below and above that window, disjoint zero-block and pivotality estimates make the summed derivative errors vanish. Lattice reindexing gives the full two-term \(o(1)\) expansion. Gamma Fourier coefficients show a nonconstant leading phase, and elementary longest-run tail bounds give the correlation rate. The exact-rational independent enumeration of 8,190 fair bitstrings for lengths 1–12 agrees with a separately coded recurrence, and lengths 100, 1,000 and 10,000 corroborate the two-term expansion numerically. The analytical proof, not those computations, supports the infinite claims.

## Originality — PASS, subject to the stated historical limitation

Finch, *Covariance within Random Integer Compositions* (arXiv:2010.06643v2), explicitly studies these very same two statistics, gives exact finite recurrences and conjectures \(\rho(N)\sim C(\ln N)^{-5/2}\) (Section 1); the established new expansion instead gives \(-\Theta((\ln N)/\sqrt N)\) and an explicit periodic two-term covariance. Bender–Canfield's 2005 work treats individual part statistics and largest-part scales rather than this mixed covariance expansion. Lou (1996) studies the exact joint law of longest runs and counts but its complete article was unavailable; an unstated general joint-asymptotic result may imply the finding and must be checked by independent historical review. A prior analysis of this **same** part-count/maximum pair already establishes negative stochastic regression, a coordinate-influence identity and a bound \(O((\log N)^2)\) for the absolute covariance; the present theorem sharpens this to an exact two-term asymptotic with absolute \(o(1)\) error and a nonconstant phase, and proves the distinct correlation scale. Another prior result for number of *distinct part sizes* and number of parts contains a related periodic kernel but does not determine covariance with the *largest part*. The older exact joint identity, stochastic order, rough upper bound, finite run recurrence and marginal asymptotics are excluded from the novelty claim.

## Value — PASS

Finch's explicit open asymptotic question for the dependence of part number and maximum part is mathematically motivated. The new two-term formula proves the correct decay regime and rules out the proposed negative power of \(\ln N\); the nonvanishing logarithmic-lattice variation further precludes a single limiting leading coefficient. The error is absolute \(o(1)\), stronger than an order-of-magnitude estimate, and is informative even at a fixed logarithmic phase.

## Limits

Uniform unrestricted compositions only. The periodic component is minute, and numerical output alone does not resolve it. Earlier publications might imply the expansion implicitly, especially Lou (1996), whose full text could not be examined.

Self-review: passed. Independent audit: not yet performed.
