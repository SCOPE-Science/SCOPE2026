# Independent mathematical audit

## correctness

PASS

Conditioning one excursion on success gives the terminal marks, since the trials are iid and geometrically repeated. The absorbing-interval transform has a near-endpoint term exp(-qd sqrt(1+s)) and an opposite-endpoint term bounded exponentially in q. After z=qd, the local densities are dominated by a constant times z^(beta-1), and the part outside any fixed target neighborhood is exponentially small. This proves the rescaled transform on each side, with a leading coefficient of zero allowed, and p_r ~ (c_+ + c_-) Gamma(beta) q^(-beta). The conditional time transform gives E[U|Z]=Z/2 and Var(U|Z)=Z/4, so Cov(Z,U)=beta/2 and the claimed correlation is 1/sqrt(2) for the limit law. The failed-duration sum is independent of the terminal marks at finite rate; its Laplace transform on the rp_r scale tends to (1+theta)^(-1), while the terminal duration on that scale vanishes. The mean threshold follows from the single-trial elapsed mean (1-p_r)/r. For total variation the coupling can disagree only if the far endpoint is hit first and before reset, with probability sinh(qd)/sinh(2aq). Add the omitted half-line Gamma tail, use ring success mass at least half the untruncated half-line mass for x>=2beta+2, and bound the cost of normalization by twice the unnormalized discrepancy divided by ring success mass. This gives the claimed factor-four bound for the symmetric pure power family, not an exact TV asymptotic. Proof replay: RESULT.md lines 54–110; CHECK.py and VERIFICATION.md were inspected, not executed, and the mass comparisons in the script are not an empirical verification of the joint TV bound.

## originality

PASS

The supported contribution is the joint high-rate law of terminal distance, terminal duration and side under target-contact density powers, with the quantitative ring-to-half-line TV bound for a pure power. Last-reset weighting, the renewal mean and the unmarked exponential clock are not credited as new. The strongest inspected position/time precursor concerns total arrival time and last reset position; its integrand can give a prelimit successful-excursion measure but does not supply the stated asymptotic or quantitative domain comparison.

## value

PASS

The limit identifies persistent dependence invisible to the two Gamma marginals or to the unmarked arrival clock. Its exponent-independent correlation and independent side are interpretable properties of successful trajectories. For the pure-power family, the explicit whole-law error controls replacing the ring by a half-line for events involving both marks simultaneously; that guarantee is not available from a mean or a marginal transform alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
