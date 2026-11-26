# Independent mathematical audit

## correctness

PASS

The focal opinion meets the two half-weight inequalities exactly for ranks L through R in a strict ordering. Below L, earlier candidate ranks have too much weight above, while L is admissible; reflection gives R for upper ranks. If L>R, the same inequalities put every lower-half target at the upper central value and every upper-half target at the lower central value. The resulting linear equations preserve all ranks: same-side gaps scale as e^(-t); the central gap in the moving-pair case scales as e^(-2t). The central mean is conserved and supplies the stated forced linear solutions. For ties, the nearest admissible value is the focal value projected onto the interval of medians. Its ends are the first weighted order statistics at cumulative weight >=1/2 and >1/2, respectively. Both are 1-Lipschitz in sup norm (coordinatewise monotone and translation-equivariant), and projection via min and max preserves this bound, proving unique continuous dependence and the tie extension. Substituting even and odd n into q gives the displayed strict cutoffs for convergence to consensus, not finite-time arrival, and the integer jumps as stated. Independent exact replay: python3 /workspace/branches/independent_checks.py 4, with 25,128 rational weighted-quantile/ODE comparisons at weight thresholds and between them, for strict and tied profiles.

## originality

PASS

The finding's new mathematical content is the explicit all-time order-statistic solution and its exact limiting selection and cluster-count staircase. Credit the ODE, the tie rule and the qualitative theory to Han et al.; the universal-consensus cutoff alone is covered as a direct corollary of their Theorem 12, not a separate original result. The inspected prior material does not determine the rankwise trajectory or selected limits from each initial profile.

## value

PASS

A homogeneous complete network is a natural exact benchmark of the already established model. The solution replaces a qualitative convergence result with initial-condition-specific limits, two distinct transient decay rates, and all self-weight boundaries for the number of limiting opinions. It also resolves equal initial opinions and threshold ties. This is useful independently of the prior universal-consensus criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
