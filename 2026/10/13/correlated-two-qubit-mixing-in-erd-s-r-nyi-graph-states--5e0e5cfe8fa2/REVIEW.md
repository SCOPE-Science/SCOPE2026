# Independent mathematical audit

## correctness

PASS

Computational-basis tracing cancels the nontrivial binary characters of the external bits and leaves a nonzero off-diagonal precisely when the two-row cut has a nonzero left kernel. Two independent uniform rows yield the claimed p. I independently expanded the joint success probabilities by inclusion-exclusion on the three possible nonzero left-kernel vectors of each cut. For each intersection pattern the resulting linear constraints on shared/internal edges contribute 2^(-rank), and each outside column supplies an independent copy of the external constraint rank. In ascending powers of t the joint polynomials are (1,-11/4,11/4,-1,0) for overlap and (1,-3,11/2,-6,4) for disjointness. Subtracting p² gives both strictly positive claimed covariances, also at n=4. The factors of 6 in the variance double the three unordered choices per triple or quadruple. For the mixed isolation moment, a specified isolate inside the pair guarantees deficiency, and one outside removes an independent column, giving conditional deficiency 3t−2t². An isolate has probability t/4 and two have probability 2(t/4)². Hence the respective coefficients of t in Var(Y), Var(Z), Cov(D,Z) are n(n−1)(n+1)/4, n/4, and n(n−1)/4. This gives n(n−1)/2 in the residual variance, with all higher terms and the squared residual mean bounded by O(n⁴t²). Substituting t=8·2^(−n) yields the announced leading variance and expectation and the one-third mean share.

## originality

PASS

Cut rank is established and the connection to low-weight stabilizers is substantive. The distinct contribution surviving the inspected comparisons is the exact two intersection-type covariances across sampled graphs and the quantitative fluctuation decomposition. The known first moments of the low-weight sectors are not the needed joint moments.

## value

PASS

Independently sampled edges do not make disjoint pair tests independent. The exact intersection-type covariances quantify that dependency and supply the variance of a natural count of maximally mixed marginals. The sharper residual distinguishes two facts that a one-site expectation misses: isolates account for the leading variance but only a third of the leading mean. This supports exact fluctuation estimates for the canonical dense graph ensemble without extrapolating to circuits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
