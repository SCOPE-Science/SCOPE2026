# Review: A sharp distributional boundary for default contagion under log-convex shock survival

## Correctness — PASS

The claim fixes the cap, net worths, liability shares, independence assumption, and event being compared. In the star, a source shock of size \(z\) creates shortfall \((z-x)_+\), split equally across the \(m\) targets; all targets default exactly when \(z>(m+1)x\). The two event probabilities are therefore \(S((m+1)x)\) and \(S(x)^{m+1}\). Convexity of \(\log S\) and \(S(0)=1\) imply the inequality, with strictness under strict convexity. The two-rate witness also has the exact positive difference \(\tfrac14(e^{-1/5}-e^{-2})^2\).

## Originality — PASS

The closest primary source is Glasserman and Young's *How Likely Is Contagion in Financial Networks?* (OFR Working Paper 13-09, first public version 2013-06-21; DOI 10.1016/j.jbankfin.2014.02.006). Its Theorem 2 and Corollary 3 use IFR shock assumptions for weak contagion with equal outside assets; Section 3.3 notes equality of the compared probability expressions for exponential shocks under equal outside assets and full source connectivity, and discusses Pareto-like tails at large thresholds. It does not state the strict all-feasible-threshold result for log-convex survival, especially non-degenerate exponential-rate mixtures. Visentin, Battiston, and D'Errico (arXiv:1608.07831) compare aggregate loss orderings across contagion models, a different observable. Searches of the mathematical claim and its aliases returned no directly matching published result; the closest surfaced records concern unrelated epidemic, reliability, or financial-flow models.

## Value — PASS

The result isolates a precise distributional boundary in a canonical clearing model: exponential homogeneity gives equality, whereas latent heterogeneity in exponential loss rates gives strict strong contagion even at small feasible thresholds. This complements the known IFR and Pareto-tail cases and clarifies that equal balance-sheet sizes alone do not determine the direction of the probability comparison. The contribution is an exact analytic statement, not an empirical estimate.

## Limitations and residual risk

The result is limited to the stated star topology, equal net worths and outside assets, independent shocks, and the specified event-probability comparison. The underlying convexity inequality is standard; originality is claimed only for its explicit exact consequence in this clearing-network setting. A broader search of reliability-theory literature could reveal equivalent applications not found in the inspected financial-network sources.

Self-review: passed. Independent audit: not yet performed.
