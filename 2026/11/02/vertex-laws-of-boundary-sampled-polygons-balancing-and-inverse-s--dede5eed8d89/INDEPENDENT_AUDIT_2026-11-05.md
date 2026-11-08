# Independent mathematical audit

## correctness

PASS

Every genuine side of a convex polygon lies on an exposed supporting line. Samples almost surely avoid original corners, and exactly min(C_i,2) extremal sampled points on side i become hull vertices, including singleton/segment degenerate hull cases; C follows Multinomial(n,p). Product exponential GF and binomial marginal give the exact PGF and mean. For any two side probabilities at fixed total, conditioning on other occupancy and the pair total s reduces each threshold of min(B,2)+min(s−B,2) to a symmetric central interval a≤B≤s−a for B~Bin(s,u); its derivative is s*binom(s−1,a−1)u^{a−1}(1−u)^{a−1}[(1−u)^{s−2a+1}−u^{s−2a+1}], positive for u<1/2. Pair-balancing therefore increases every upper tail, and standard majorization chains prove global stochastic order. The mean summands have f_n(p)=−n(n−1)(n−2)p(1−p)^{n−3}<0 for n≥3, giving strict mean Schur concavity. For q_i=1−p_i, deficits sum to a rational function with genuine order-two poles at t=1/q_i of coefficient multiplicity*(1−q_i)/q_i>0, so expectations recover unordered side proportions and m. Independent exact multinomial/GF and two balancing examples through n≤8 agree; the analytic proof handles all admissible polygons/n, unlike finite tests.

## originality

PASS

The supporting-side reduction and asymptotic limit 2m already follow from boundary random-polytope literature; individually Schur-ordered occupancy threshold counts are also prior work. The new substantive combination is stochastic order of the correlated SUM of occupied-at-least-one and occupied-at-least-two cells for every threshold, together with full inverse side-length recovery. The 2013 occupancy source was read as an accessible Russian PDF (main theorem), but specialist equivalent results remain a qualified risk.

## value

PASS

The statistic is directly observable in random boundary sampling; a complete finite-sample law, all-threshold shape-balancing extremality and inverse recovery of side probabilities are mathematically motivated, independently useful statements rather than mere occupancy bookkeeping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
