# Independent mathematical audit

## correctness

PASS

PASS: The first-passage inverse-Gaussian density is L/(4πDt³)^(1/2)exp[−(L−vt)²/(4Dt)], and its CDF is the stated two-normal-tail formula, normalized to one for v>0. For two laws, log(f1/f2)=A/t+B t+C with explicit A and B controlled by D order and squared-speed/dispersion order. In comparable regimes log ratio has one crossing, so the normalized densities give strict first-order stochastic dominance. In conflicting regimes A>0,B>0 (after relabeling) forces density signs +−+, from which the CDF difference has exactly one simple zero because its total integral is zero and it is strictly decreasing between density sign changes. With equal positive speed, evaluating at t=L/v and applying the strict Mills inequality puts the crossing after the mean. At t=y/v², direct normal-tail expansions give scaled survival limit; differentiating its h functions gives H'(y)=k_D2(y)−k_D1(y) with one derivative change at y_p. Boundary signs show exactly one y* in (0,y_p). Uniform convergence on compact y intervals plus unique CDF crossing proves v² t_cross→y*. New finite computations independently checked 24 density log-ratios, the t_cross≈2.558169017584 example and y*≈1.415604396416. This is not a proof for variable coefficients.

## originality

PASS

PASS (qualified): Inverse-Gaussian hitting-time density and CDF are classical and available in Molini et al. and standard statistical references, so neither is claimed as novel. The assessed addition is the *complete two-parameter necessary-and-sufficient CDF order*, exact single transversal crossing when parameters conflict, mean-travel lower bound and singular v^-2 crossover scaling with a uniquely characterized y*. The inspected transport and IG computation references do not contain this full classification. General stochastic order literature may imply some comparisons, and deriving ordering from density ratio is comparatively direct; the singular crossover and sharp strict placement support a distinct result, with historical risk preserved.

## value

PASS

PASS: Cumulative first arrivals at an absorbing downstream threshold are canonical transport observables. A sharp global test for whether a higher-dispersion tracer is ever guaranteed earlier arrival, coupled with the exact one-crossing law, resolves a genuine model-selection ambiguity. The common-drift singular scaling quantitatively explains why a high-dispersion advantage survives every fixed observation time at zero drift yet reverses at t≈y*/v² for arbitrarily small positive drift. This full boundary classification is naturally motivated rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
