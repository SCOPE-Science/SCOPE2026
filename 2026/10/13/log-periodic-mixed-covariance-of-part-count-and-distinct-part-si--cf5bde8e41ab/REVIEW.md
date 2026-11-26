# Independent mathematical audit

## correctness

PASS

For fair independent separator bits the covariance with their sum is one quarter of the sum of insertion influences. Conditional on the two local lengths, the distinctness gain at size j is the indicator of no unchanged occurrence times the new-child count at j, subtracting a child duplicate and subtracting loss of the parent. A size-j part in an interior region uses the cut–(j−1 noncuts)–cut word of probability 2^{−j−1}. Its distinct starts separated by less than j have incompatible bits; starts j apart share one cut; others are independent. For independent dependency neighborhoods the void estimate used in (3) was also derived directly: for k≥1 set f(k)=∫₀¹t^{k−1}exp(−λt)dt and f(0)=f(1). Integration by parts gives λf(k+1)−kf(k)=1_{k=0}−exp(−λ), and the one-step differences are bounded by f(1)≤min(1,1/λ). Subtracting the sum outside each neighborhood, independent of its indicator, bounds the expected Stein residual by that difference bound times b1+b2. After conditioning on local lengths at most M=ceil(4 log₂ n), remove word positions intersecting conditioned bits or domain endpoints. There are O(j+M) omitted starts. An unchanged word that remains possible among them can use at most one forced endpoint cut: the interior of the affected parent or children cannot be inside another part, and splits at the obligatory ends only cost one endpoint bit. Hence the summed omitted-word probability is O((j+M)2^{−j}), uniformly in the central window. The same envelope covers the mean adjustment and the dependency-neighborhood error. Geometric-run probabilities give the pivotal signed weight (3−j)2^{−j}−4^{−j}; multiplying the void error by its absolute indicator bound costs O(j(j+M)4^{−j}) per cut and size. The sum is o(1) since the window starts at ¾ log₂ n. Truncating local lengths costs O(n(log n)2^{−M}); O(log n) boundary cuts are negligible by the truncated-geometric bound O((j+1)2^{−j}). For small j one can choose Ω(n/(j+1)) disjoint full interior words avoiding the changed bit; any success is unchanged, yielding superpolynomial void suppression. The large-j geometric tail and the central duplicate term are negligible even after summing over cuts. Thus the expression reduces to (1/2)∑(3−j)t_j exp(−t_j) with t_j=n2^{−j−1}, up to absolute o(1). Lattice reindexing and the exponential tails give the asserted A and B including the constant 4 inside B. The Mellin integral gives Γ(1−2πiℓ/ln 2)/ln 2, nonzero at ℓ=1, so positivity, nonconstancy and eventual negative covariance follow; log-moment integration gives the stated period mean for B. Independent finite corroboration used coefficients of (1−y[x/(1−x)−x^j])^{-1} and its y-derivative via a short denominator recurrence, then compared with direct composition enumeration through n=12. For sample n=64,91,128,181,256,362,512,724,1024, exact covariance minus the predicted profile had absolute value at most 4.08×10^{−5}. The infinite result is supplied by the error analysis, not the comparisons.

## originality

PASS

Prior exact generating functions encode the mixed statistic, and marginal distinctness already exhibits dyadic oscillations. The strongest catalog overlap also studies the same mixed-covariance mechanism with number of parts, but the second variable is maximum part size, not the number of represented part sizes. The distinctness asymptotic through constant order is the supported contribution, not the exact generating function, influence identity, or generic phenomenon of periodicity.

## value

PASS

The result measures dependence between two natural statistics of the same composition—fragmentation and diversity. It resolves the sign and full logarithmic order, proves that a constant leading coefficient does not suffice, and exhibits the absolute-accuracy second term. These are informative mixed-statistic features not given by the known marginal distinctness behavior or by covariance with the maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
