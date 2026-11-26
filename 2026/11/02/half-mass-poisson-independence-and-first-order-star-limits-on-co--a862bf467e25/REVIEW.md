# Independent mathematical audit

## correctness

PASS

With iid vertex colors and an open neighborhood the mean is p_c(2p(S))^d, giving subcritical extinction by Markov. The only dependent distinct centers are at distances one and two. At distance one the other neighbors are disjoint and the centers must satisfy each other's palette constraints; at distance two precisely two open neighbors are shared. Both give the joint upper bound p_c² p(S)^(2d−2), so the displayed normalized variance vanishes for supercritical mass. At criticality use one indicator per (center, palette, color), with dependence neighborhoods the closed center ball of radius two times the types. The product-of-means sum is at most m² D_d 2^(−d). At a common center, different center colors are disjoint; for equal color, distinct palettes give the exact intersection-mass^d term, whose total is at most m²ρ^d. At distinct close centers at least 2d−2 input vertices have palette restrictions of mass at most 1/2, giving the remaining 4m²D_d2^(−d) bound. Each pair of distinct half-mass palettes has intersection mass strictly below 1/2 by positivity. For an independent normalization check of the point-process estimate, solve the Poisson Stein equation with the immigration–death semigroup on the finite index set, using indicator test functions. Its solution has all mixed second differences bounded by ∫0^∞ 2 exp(−2t)dt=1: both inserted particles must survive and the mixed difference of an indicator is at most 2. In the generator identity compare each first difference to the vector with its dependence neighborhood removed; the comparison terms cancel by independence from that indicator, and the two errors are bounded by b1 and b2 (the death term already removes the indicator itself). Thus supremum-event TV is bounded by b1+b2, in particular by the claimed 4(b1+b2), independent of the citation's norm convention. Summing independent Poisson coordinates separately by type contracts TV and gives exact means p_c. Fixed Boolean threshold evaluations then follow by a finite union bound for the noncritical events and TV for the critical vector. The empty critical set, positive dimensions including d=1, and uniform odd/even consequences fit the same calculation. For q=2 each palette total sums two independent Pois(1/2) variables, giving joint positivity (1−e^(−1))².

## originality

PASS

Credit is limited to the simultaneous marked, possibly overlapping half-mass palette vector in iid vertex-colored cubes and the resulting fragment evaluation. One isolated-vertex coordinate has concrete site-percolation precedence risk; neither that single count, generic Poisson approximation, nor a general first-order convergence law is credited as new. No inspected result supplies the fixed-palette joint law for all these marks and overlapping palettes.

## value

PASS

The natural question is whether simultaneously rare star events with overlapping palettes on the same cube behave independently, not just whether any one count is Poisson. The full multitype law supplies concrete joint threshold probabilities, including the zero–one versus nontrivial uniform-palette dichotomy for the specified Boolean fragment. The bound identifies a palette-overlap error distinct from geometric near-center dependence. This is an increment beyond a scalar isolated-vertex approximation, without implying an unrestricted first-order convergence law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
