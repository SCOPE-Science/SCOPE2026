# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Conditioning on the first n observations gives the exact joint-discovery probability as `M_n^2-Q_n`; the covariance identity then follows by elementary expectation algebra and `E Q_n=m_n-m_{n+1}`. The negative uniform family is an exact closed-form calculation. The positive finite family has an exact formula whose limit is strictly positive for every `n>=1` and `0<a<1`, so positivity for sufficiently large finite K follows without numerical approximation. The diffuse-tail maximization uses strict log-concavity and a standard one-dimensional asymptotic scaling.

Adversarial checks included degenerate limits, small alphabets, small n, direct pair-sum formulas, and exact rational comparisons. No hidden moment or finiteness assumption is used beyond countable iid sampling for the main identity.

## Originality

**PASS, to the best of our knowledge.** The checked literature contains extensive work on discovery probabilities, Good-Turing estimation, occupancy counts, and missing mass. Good--Toulmin (1956) concerns extrapolating new-species counts and coverage; Starr (1979) and Clayton--Frees (1987) concern estimation of future discovery probability; Ben-Hamou--Boucheron--Ohannessian (2017) concerns concentration of occupancy counts and missing mass. The full open-access article of Chebunin--Zuyev (2022) was checked because it develops covariance functions for occupancy and missing-mass processes under regular variation. It does not state the adjacent realized-discovery identity or the finite-law sign-reversal theorem in the inspected text.

Searches also used equivalent occupancy language such as new urn, newly occupied box, increments of the number of occupied urns, discovery indicator, species accumulation, and missing-mass covariance. No checked source stated the exact decomposition or showed that adjacent discovery covariance has both signs for every n.

Residual risk is nontrivial because the main identity is elementary once the missing mass is conditioned upon. Good--Toulmin (1956) and Starr (1979) were not inspected in complete theorem-level text, and older urn/occupancy references may contain an equivalent increment-covariance formula under different terminology. Skorski (2021) was checked at abstract level for the maximal-variance problem, not theorem by theorem. These are residual originality risks, not evidence of known coverage.

## Value

**PASS.** Missing mass is the conditional probability of a new species, so the identity gives a direct structural explanation of serial dependence in the species-discovery sequence: random heterogeneity of remaining coverage pushes successive discoveries together, while removal of probability mass by a discovery pushes them apart. The resulting sign-indeterminacy rules out a universal negative-dependence heuristic even in ordinary iid sampling. The finite positive and negative constructions make the distinction exact rather than asymptotic.

## Scientific limitations

The result is restricted to adjacent discovery indicators and does not characterize longer lags or the full discovery process. No global extremal covariance over all species laws is claimed. The one-atom/diffuse-tail optimum is family-specific. The principal originality uncertainty is equivalent older occupancy terminology.
