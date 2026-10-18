# Independent mathematical audit

## correctness

PASS

For each fixed occupied label set A of size k, conditional bootstrap configurations are uniform surjections. Identifying two draw positions gives same-label probability S(n-1,k)/S(n,k) for Stirling numbers of the second kind; exchangeability makes conditional unbiased bootstrap variance k(1-q)v_A/(k-1), and average over uniform k-subsets has E[v_A]=(k-1)S²/k. Hence E[S*²|K=k]=(1-q)S² for 2<=k<=n, with k=1 directly zero. Centered multinomial multiplicities give Cov(K,S*²)=(1-1/n)^n S²/(n-1) by conditioning on one omitted label; ties counted by source labels, not values. Independent Fraction enumeration of all ordered n^n resamples for n=2..5 and distinct fixed profiles, including tied values, reproduced both conditional and unconditional expressions. Enumeration is corroboration, symbolic argument proves all n>=2.

## originality

PASS

Rao–Pathak–Koltchinskii address random occupied-support size and sequential resampling, and Pauly studies the fixed-support bootstrap empirical process; neither inspected primary treatment gives an exact support-size conditional unbiased sample-variance multiplier or a data-free mixed covariance. Published Resultary semantic searches of bootstrap distinct-count, occupancy and mixed-variance aliases returned related but nonimplicative occupancy/sampling results. Conditional Stirling factor and covariance are not merely their existing marginal support-count moments. Old survey-sampling formulas under different normalization remain risk; search absence not certainty.

## value

PASS

K is a standard proxy for the information retained by an ordinary bootstrap replicate, while sample variance is a central bootstrap statistic. Exactly quantifying E[S*²|K] and universal scale-free Cov(K,S*²) for every nonconstant dataset is a motivated finite-sample regression of a natural estimator on a natural occupancy statistic, not an arbitrary parameter slice or a restated K distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
