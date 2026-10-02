# Independent mathematical audit

## correctness

PASS

Writing the complete-randomization difference-in-means error as a scaled simple-random-sample mean of A_i=(1-pi)Y_i(1)+pi Y_i(0) preserves range R. Serfling's finite-population bound gives the stated finite-sample exponent and tends to 2pi(1-pi)/R^2. A half-endpoint sharp-null population reduces the lower tail to an exact hypergeometric point probability; Stirling/entropy expansion gives the matching exponent, with the assumed n t_n^2/log n -> infinity making polynomial factors negligible. In fixed strata the quadratic local costs minimize under the weighted error constraint at harmonic allocation, giving Gamma=sum w_j/[p_j(1-p_j)] and exponent 2/(R^2 Gamma). The verifier is corroboration only.

## originality

PASS

Classical finite-population Cramér/moderate-deviation theory gives relative normal-tail approximations for a specified population; recent randomized-experiment papers give finite-sample concentration or minimax rate results. None of the inspected sources states the exact worst-case bounded-potential-outcome moderate-deviation constant, its binary sharp-null attainment, or the fixed-stratum harmonic constant.

## value

PASS

The exact logarithmic constant identifies the true worst-case finite-population tail scale, proves a simple extremizer, and gives a nontrivial stratified harmonic design law directly relevant to bounded-outcome randomization inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
