# Mathematical review

## Correctness — PASS

The binomial formula for the central Delannoy sequence follows from the bivariate lattice-path generating function. Two applications of Vandermonde's identity split the dyadic shift into terms with one and two positive indices. The elementary bound \(\nu_2\binom hi\ge\nu_2(h)-\nu_2(i)\) leaves two single-positive contributions and, only when \(\nu_2(h)=2\), two double-positive contributions of the lowest possible valuation. The latter cancel modulo \(32\), a critical exceptional check. The resulting first-order phase holds for all \(n\ge0\) and all positive \(4\mid h\). The minimal-period argument rules out all smaller periods through the gcd-of-periods property, not merely half the chosen period. The standalone integer-recurrence verifier passed all documented tests; it is corroboration rather than an infinite certificate.

## Originality — PASS with residual historical risk

Sun, arXiv:1008.3887 (2010), identifies the generalized trinomial specialization and analyzes summatory congruences; Sun, arXiv:1009.2486 (2010), considers primarily odd-prime sums. Guo, arXiv:1412.7724 (2014), proves weighted Delannoy-polynomial power-sum congruences. Kauers–Krattenthaler–Müller, arXiv:1107.2015 (2011), develop general methods for powers-of-two congruences in other recurrent families. OEIS A001850 tabulates standard central Delannoy formulas, not an explicit all-moduli least-period theorem in the inspected entry. The precise uniform dyadic index-shift phase and resulting least-period law were not located in the inspected material. These sources may imply weaker modular congruences, while a general recurrence algorithm might in principle derive special cases after computation; no directly covering statement or reduction was identified. Prior-work searches do not establish absolute uniqueness. Specialized literature on Legendre-polynomial values at three or on modular recurrences may contain equivalent results; this requires independent historical scrutiny.

## Mathematical value — PASS

Global least periods modulo every power of two are canonical invariants of the central Delannoy sequence. The result supplies their complete classification and a uniform leading dyadic shift term, with a sharp parity dichotomy in the index and a nontrivial cancellation at the first exceptional valuation. It is more informative than finite period tables or a generic existence-of-period result and identifies exact arithmetic behavior across an infinite family of moduli.

## Verification and limits

The verifier uses the three-term integer recurrence to compute the sequence independently of the binomial and shift formulas, then checks the latter and the least periods. The proof, not a bounded enumeration, supports the unbounded claim. No assertion is made for odd-prime periods, arbitrary generalized coefficients, or the higher valuation layers of indices congruent to zero or three modulo four. Historical priority remains subject to further source access and an independent review.

Self-review: passed. Independent audit: not yet performed.
