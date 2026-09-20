# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

PASS. The proof reduces the third-cumulant effective count to a variance-weighted Bernoulli mean and the fourth-cumulant count to an inverse participation ratio of the Bernoulli variances. The key comparison is the nonnegativity of the weighted variance of the success probabilities; Cauchy--Schwarz gives the active-count bound. The fixed-variance projection bounds follow from these identities plus the exact extrema of a sum of squares on the capped simplex. Equality cases were checked against the proof hypotheses. Exact-rational finite checks support the algebra but are not used as a substitute for proof.

Potential failure modes considered included deterministic Bernoulli summands, complementary probabilities with equal variances, zero skewness without equal probabilities, endpoint variance V=n/4, and the residual-variance case in the lower fourth-cumulant envelope. None invalidates the stated claims.

## Originality

PASS, to the best of our knowledge. Hoeffding (1956) supplies the classical mean-fixed extremal background. Peköz, Röllin, Čekanavičius and Shwartz (2009) explicitly derive the real-valued third-moment-matching parameters p* and n*; the present N3 is exactly their n*, so that formula is not claimed as new. Tang and Tang (2023) survey Poisson-binomial stochastic ordering and approximation. Shuldiner and Oldford (2022) develop general moment and central-moment formulas for Bernoulli sums.

The literature search did not locate the hierarchy N3 <= N4 <= r, the equivalent joint third/fourth-cumulant inequality, or the stated sharp fixed-(n,V) skewness/kurtosis envelopes. The principal residual risk is terminology-equivalent coverage in older moment-inequality or Bernoulli-sum literature. The Shuldiner--Oldford full text was not inspected here beyond its abstract and bibliographic description, so it is the most relevant unverified source for possible formula-level overlap.

## Value

PASS. The result turns the 2009 three-moment fitted trial count into one member of a monotone low-cumulant hierarchy and supplies a stronger fourth-cumulant lower bound on the number of active Bernoulli components. The sharp projection formulas give immediately checkable feasibility constraints for Poisson-binomial modeling and an exact finite-n range for the third absolute moment entering normal-approximation bounds.

## Scientific limitations

The theorem assumes independent Bernoulli summands. It gives necessary low-moment constraints, not a complete characterization of all feasible cumulant triples. The active-count bound does not identify a unique Bernoulli decomposition from low moments alone. The Berry--Esseen consequence concerns its Lyapunov numerator and does not claim an optimal distributional-approximation constant.
