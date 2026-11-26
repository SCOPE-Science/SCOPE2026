# Independent mathematical audit

## correctness

PASS

At each fixed time, independence makes the variance a sum of Bernoulli variances, whereas the mean derivative is strictly negative. The derivative of the variance is a nonzero sum of at most 2n distinct exponentials after grouping; it is positive at zero. Multiplying by a nonvanishing exponential that eliminates one exponent, differentiating and using Rolle's theorem with multiplicities proves the requisite zero bound inductively, including when rates coincide. Two distinct strict maxima enclose a stationary minimum, so the ceiling of 2n−1 derivative zeros permits at most n strict maxima. For the ratio-20 construction at a_j=log(4)/λ_j, the jth term is −λ_j/8, faster terms are negative and slower terms sum to at most λ_j/19. At b_j=log(2)/(2λ_j) the jth term exceeds λ_j/4 and the slower terms are positive; the faster negative tail is bounded by a series whose first term is 20λ_j/1024 and successive ratios are at most 20·2^(−190)<1/2. Hence it contributes in magnitude less than λ_j/20. Chronologically the consecutive witnesses a_{j+1}, b_j, a_j are ordered by their multiples 2, 10 and 40 of log(2)/λ_{j+1}; the origin is a positive-sign initial witness. This gives 2n−1 distinct positive zeros, and the global ceiling with multiplicity makes each simple and excludes any others. The one-species case uses just the origin and a_1. Alternation gives the exact maxima/minima counts, and strict signs persist in a neighborhood of the hazards at these fixed witness times, directly proving robustness. No finite numerical replay is needed for this analytic proof.

## originality

PASS

The same variance curve is classical under the exact alias of Poissonized occupied-box counts. The universal zero bound follows from classical exponential Chebyshev theory, and neither that bound in isolation nor the one-component peak is credited as new. The distinct verified contribution is the sharp finite-n mode classification, especially the explicit factor-20 rate separation achieving the full zero bound for every size, with stability. The closest occupancy work treats oscillation and limiting variance in infinite models and the indexed richness work uses a different sampling rule. This is a bounded statement-level assessment.

## value

PASS

Even with independent losses and monotone mean richness, the temporal ensemble variance can have as many distinct strict and stable peaks as there are species. The least size allowing two peaks and the all-size finite sharp scale construction give explicit, reproducible counterexamples to inferring unimodality of uncertainty from monotone survival. The exact bound also answers how much arbitrary positive rate heterogeneity can change the temporal peak count in this model; it is not merely the standard Bernoulli variance identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
