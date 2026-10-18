# Scientific review — convex-order endemic prevalence

## Correctness: PASS

The finite-type SIRS equilibrium has an exact scalar reduction: for \(x=\mathcal R_0\widehat I>0\), the susceptible equilibrium is \(s_j=p_jg_x(h_j)\) with \(g_x(h)=(1+\mu h)/[1+x+(\mu+(\mu+\gamma)x)h]\). The equation \(\sum_jp_jg_x(h_j)=1/\mathcal R_0\) has exactly one positive root whenever \(\mathcal R_0>1\); every such root reconstructs the original compartment balances. Direct differentiation yields strict convexity in \(h\) and strict monotonicity in \(x\), proving the convex-order comparison. The mean-preserving two-point parametrization has strictly positive dispersion derivative away from zero for all \(0<p<1\). An implicit-function expansion establishes the stated second-order coefficient. The included checker independently passed 5,109 symbolic, exact-rational and numeric assertions. Boundaries, positivity and the exclusion of the disease-free case are explicit.

## Originality: PASS

The November 2023 preprint and April 2024 journal paper by El Khalifi and Britton are the closest sources: the final publication proves increasing endemic burden with waning heterogeneity only when the lower-immunity fraction is at least one half (Proposition 2), explicitly describing the complementary smaller-fraction case as suggested by numerics rather than proved. Its Appendix A.1.2 does not establish the general finite-type convex-order comparison. The authors' earlier gradual-waning comparison changes an individual's susceptibility trajectory rather than dispersing the type-specific mean duration in the sudden-loss model. Foutel-Rodier, Charpentier and Guérin compare booster-vaccination intervals for disease-free susceptibility and invasion, not endemic burden under reciprocal waning-rate heterogeneity. Searches of relevant published mathematical findings and alternative formulations found no statement known to imply the presented comparison. General convexity tools are not themselves claimed as new. Residual risk: an unlocated general epidemic or order-theoretic theorem might yield the same specialization; independent literature review may revise the priority assessment.

## Value: PASS

The result proves a specifically documented open parameter regime, \(0<\(p<1/2\)\), in a motivating epidemiological model. The finite-type convex-order theorem explains the underlying mechanism without a two-group restriction, and the positive population-split-independent quadratic coefficient quantifies the burden of small waning heterogeneity. These statements distinguish equilibrium endemic burden from the related but different vaccination-threshold comparisons and provide a reusable analytic principle.

## Limits

The result assumes complete homogeneous population mixing, permanent type labels, exponential waiting for sudden immunity loss within each type, shared demographic/recovery parameters, and \(\mathcal R_0>1\). It is not a transient or global-stability result. Equilibrium impact under heterogeneity in waning **rates** rather than **reciprocal rates** is not established. Potential unpublished or poorly indexed general convex-order results remain a publication-priority risk. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
