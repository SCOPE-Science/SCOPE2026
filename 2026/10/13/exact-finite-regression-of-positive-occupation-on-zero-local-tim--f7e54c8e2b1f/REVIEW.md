# Review
## Correctness
PASS. Conditioning on the reflected path fixes every zero time and every excursion length. Reflection symmetry makes each excursion sign fair, so every nonzero time is positive with conditional probability \(1/2\). This proves the full conditional mean, not only a covariance identity.

The local-time mean and variance are independently derived from exact return probabilities. The central-binomial telescoping identity gives the mean, while the Markov property and the convolution of \((1-z)^{-1/2}\) give the second factorial moment. Exhaustive enumeration confirms the reflected-path fibers and all moment formulas on finite horizons.

## Originality
PASS, with a specific historical risk. The closest complete finite-path article treats strict positive occupation together with a downcrossing-based local-time analogue and proves an excursion-rearrangement theorem. Its finite local-time variable is not the number of zero visits used here. A complete later article defines precisely the zero-visit local time and one-sided occupation time but studies strong approximations and limit theorems rather than this finite regression.

Targeted searches for the conditional slope, covariance formulation, and signed-occupation equivalent did not locate the statement. The remaining risk is an older fluctuation-theory source using another zero-time convention.

## Value
PASS. Local time and occupation time are canonical, heavily studied path functionals. The result gives a simple exact finite bridge between them: every additional zero visit reduces conditional expected positive occupation by exactly \(1/2\). The resulting covariance is not an isolated calculation; it is a direct consequence of a stronger reflected-path regression and cleanly separates zero-slot effects from signed excursion imbalance.

## Closest literature and limitations
The closest finite paper uses a different discrete local-time statistic based on downcrossings. The closest same-object full text is asymptotic. The theorem is specific to symmetric excursion signs and strict occupation; skew walks or alternative zero conventions change the finite identity.

Self-review: passed. Independent audit: not yet performed.
