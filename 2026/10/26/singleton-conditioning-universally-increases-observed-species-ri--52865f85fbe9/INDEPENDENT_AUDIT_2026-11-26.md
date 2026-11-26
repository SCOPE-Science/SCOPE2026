# Independent mathematical audit

## correctness

PASS

Conditional on T nonfocal draws, their multiset has the same law as a length-T prefix of an independent renormalized iid list or a uniform permutation of the nonfocal census individuals. Thus unconditional richness can be realized as R_T + 1_{T<n} and singleton-conditioned richness as 1+R_{n-1}. For T<n use monotonicity; for T=n use R_n − R_{n-1}≤1. The census prefix exists whenever the target event has positive probability; T=n is used only if feasible. The indicator covariance equals event probability times the conditional mean gap, and summing over species includes zero-probability events with contribution zero. In the iid case n≥2, singleton conditioning guarantees K≥2 while the all-focal outcome has positive probability; the strict increment of a strictly increasing g at 2 ensures strict covariance. For every 2≤r≤n, the supplied uniform iid example and census example have positive exact-r events with K≤n−r+1, whereas all n distinct nonfocal species occur with positive unconditional probability. The argument includes n=1 and full-census equality cases. The proof was reconstructed directly; the bundled code and certificate were inspected, not executed. The reported 28 counterfamily checks are elementary assertions, not full distribution enumerations.

## originality

PASS

Best of current knowledge: the fixed-species singleton conditional stochastic order against the unconditional law in both sampling models is distinct from the inspected equal-box covariance, presence conditioning, and frequency-count asymptotics. The positive singleton covariance in the uniform model is not separately new.

## value

PASS

Richness and singleton frequency are standard sampling summaries. This gives a distribution-level guarantee, not just a moment sign, that survives arbitrary abundance heterogeneity and the switch from iid draws to a census. The sharp failure of every higher fixed multiplicity identifies why singleton conditioning is special and makes the result useful without claiming general association.

The dated certificate retains the supplied scientific assessment, sources and limitations.
