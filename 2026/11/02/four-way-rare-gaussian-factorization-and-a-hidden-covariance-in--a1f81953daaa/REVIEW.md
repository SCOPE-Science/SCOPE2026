# Scientific review: joint rare and Gaussian shuffle fluctuations

## Correctness

PASS. For fixed positive linear-time parameter, the finite coupling reduces the shuffled deck to a random set of previously selected cards and a uniformly ordered prefix. The exact maximum law and hypergeometric factorial moments establish the Poisson–geometric pair; a conditional descent CLT after deleting finitely many prescribed fixed positions proves the previously missing joint independence. The classical full-span occupancy CLT supplies the separate Gaussian fluctuation. A distinct finite covariance identity and bounded-moment argument establish the nonzero raw covariance limit. Exhaustive finite checks verify the coupling and the exact conditional identities; they are not used as proof of convergence. The proof excludes zero drift in the shuffle-count parameter, and fixes that parameter independently of deck size.

## Originality

PASS under the accessible-source, best-knowledge standard, not a claim of comprehensive historical priority. Clay (arXiv:2603.09008; first submitted 2026-03-09) establishes separate fixed-point and descent limit laws and the finite coupling, but neither the four-way joint limiting law nor the surviving unscaled covariance. The critical mixed-factorial moment step and the exact conditional covariance are additional arguments beyond the marginal limits; marginal weak limits alone never certify independence. Athanasiadis–Diaconis (arXiv:0912.1686) develop induced descent-set chains and mixing, not these joint critical-time fluctuations. Pehlivan (arXiv:1006.1321) studies top-to-random card-position and guessing distributions. A public record on stationary-uniform permutation fixed-point/descent covariance concerns a different probability law and does not imply the occupancy-driven covariance. Searches for Tsetlin/move-to-front synonyms and for Gaussian–Poisson joint laws returned no directly covering formulation. Residual risk: a general multivariate-shuffle theorem, or an unpublished extension of the source coupling, could already imply the claim.

## Mathematical value

PASS. The source separately studies fixed points, descents, and selected-card occupancy but their **joint** dependence matters when the three are measured on the same incomplete shuffle. This theorem separates the four sources of randomness into two rare pieces and two Gaussian pieces, computes the descent/occupancy Gaussian correlation, and reveals a negative covariance on the unscaled level that cannot be read from either marginal weak limit or from their asymptotic independence under Gaussian scaling. The quantities are canonical shuffle statistics, not constructed parameters or arbitrary finite slices. It does not address biased selection, quantitative multivariate approximation, or variable shuffle intensity.

## Closest literature and limitations

- A. Clay, *On the statistics of random-to-top shuffles*, https://arxiv.org/abs/2603.09008, Sections 3–6 and 8. Marginal laws and finite decomposition are prior work.
- C. A. Athanasiadis and P. Diaconis, *Functions of random walks on hyperplane arrangements*, https://arxiv.org/abs/0912.1686, Section 5. Descent-set and induced-chain statements are prior work.
- L. Pehlivan, *No Feedback Card Guessing for Top to Random Shuffles*, https://arxiv.org/abs/1006.1321. Position and guessing questions are different.
- Published indexed research titled *Boundary localization of fixed-point–descent dependence in a uniform permutation*, 2026. Its stationary-uniform conditional covariance is a comparator, not identical coverage; the full record was not recovered for inspection.

The originality check is necessarily bounded by the accessible literature and indexed research; it is not independent historical certification. The standalone checker verifies finite identities only; the nontrivial infinite statements are justified analytically in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
