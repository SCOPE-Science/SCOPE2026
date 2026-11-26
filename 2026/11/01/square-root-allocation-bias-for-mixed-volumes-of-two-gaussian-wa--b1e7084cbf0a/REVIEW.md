# Independent mathematical audit

## correctness

PASS

The independent-copy formula divides by d! and all block lengths. For Gaussian increments each determinant contributes the square roots of the block lengths times a common standard Gaussian determinant; its expectation cancels d! and gives the stated unit-ball factor with the normalized mixed volume. The generating function of F_r is Li_{1/2}(z)^r/(1−z). The first two singular powers are −1−r/2 and −(r+1)/2; transfer gives the asserted leading coefficient and relative correction β_r. The expansion is in a slit domain and can be transferred sufficiently far that log F_r(k), after its leading logarithm, has powers k^{-j/2} through j=5 and remainder O(k^{-3}); thus differencing the remainder does not jeopardize either displayed log-difference estimate. Leading asymptotics give interior maximizers with m/N→p/d, excluding endpoints by the uniform power bound. There the forward increment has leading drift (pN−dm)/(2m(N−m)) with uniform error O(N^{-3/2}). Its forward and backward signs at a maximizer imply |m−pN/d|=O(sqrt N). Expanding there gives slope −d³/(2pq) in the scaled coordinate and zero at the stated α, with uniform O(N^{-2}) increment error, so the location error is bounded in steps. The second log-difference makes the increment strictly decreasing on a common interior interval containing all maxima, excluding three or two nonadjacent maxima. The digamma integrand is e^{−xt/2}/(1+e^{t/2}), strictly bounded by (1/2)e^{−(x/2+1/4)t}; this proves that h decreases and, as ζ(1/2)<0, that β_r/r^{3/2} increases. Hence the bias has sign q−p and vanishes at equality; substitution gives the stated (2,1) example. Replay: RESULT.md lines 37–91, with the precise source normalization below. The supplied verify_budget.py was inspected, not executed, and its finite floating-point estimates are not evidence of an all-large-budget threshold or of exact ties. The proof applies only to fixed p,q and the stated Gaussian walks.

## originality

PASS

The supported distinct result is the integer optimizer theorem with signed square-root shift, bounded step error and eventual adjacency, not the expectation identity, leading proportional split, or individual analytic tools. None of the strongest accessible statements inspected either gives that precise discrete claim or mechanically implies it jointly without the higher coefficient and finite-difference analysis.

## value

PASS

The proportional prediction misses an unbounded number of steps whenever p and q differ. The exact sign and size of that bias, bounded integer location error, and eventual restriction to at most two adjacent optimizers resolve a natural allocation problem quantitatively rather than merely restating the continuous limit or checking an example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
