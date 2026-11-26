# Independent mathematical audit

## correctness

PASS

The exact tail factors come from writing the multiplicity at size j as an unrestricted nonoverlined count and an independent optional overline in the Boltzmann measure. Requiring a nonoverlined occurrence gives q^j, any occurrence gives 2q^j/(1+q^j), and complete absence gives (1-q^j)/(1+q^j). The product saddle is t_n=pi/(2 sqrt(n))+O(n^-1) with variance asymptotic to 4 n^(3/2)/pi, from the differentiable eta transformation of the product. For the centered coefficient integral the quadratic Gaussian approximation on |theta|<=n^(-7/10) has a uniform O(n^2 |theta|^3) remainder from the third cumulant bound (summing geometric and Bernoulli factors). The normalized restriction multipliers vary by o(1) there: the sum of the forced-presence angular derivatives is O(sqrt(n)), each of the fixed marking factors costs O(j) or is constant, and the single absence costs O(1/t_n), since |1-q^j|>=1-|q|^j. The untouched block of sizes from sqrt(n) to 2 sqrt(n) controls all other arcs: for small angles use the pointwise sine bound, for angles comparable to n^-1/2 the corresponding sine-square Riemann sum is bounded below uniformly on compact rescaled ranges away from 0, and for larger angles use the geometric sum bound. Nonnegative restricted local series cannot increase the normalized modulus. This gives uniform relative transfer for the factors actually used. The proof's illustrative statement that the one-absence multiplier is of order n^-1/4 applies at positive rescaled j; uniformly for 1<=j<=L n^1/4 the lower bound is instead c_L n^-1/2 and the upper bound C_L n^-1/4, which still gives the claimed transfer and uniform absolute local-mass estimate. The marking factors tend to 1/2, giving the geometric coordinate and its independence. For coincidence the exact event requires nonoverlined presence below j and complete absence at j; its rescaled mass density is (pi z/4) exp(-pi z^2/4), with the omitted tail bounded by the B tail. Its integral is 1/2, independently of weak convergence of the ratio. The Rayleigh ratio integration gives r^2/(1+r^2) for r<1. An independent finite replay at branches/2b220df3-4654-41c2-9b71-041731d6de42/recheck/replay.py and its two output chunks checked all integer joint-tail cutoffs and equality through n=12 and the exact n=100,400,900 checkpoint probabilities. This is limited finite corroboration; the limit uses the analytic transfer and tail argument, not those checkpoints.

## originality

PASS

The three statistics, marginal enumerative methods, and Rayleigh running-minimum mechanism have clear antecedents. The supported distinction is the simultaneous law of these three presence conventions for the same unrestricted overpartition, including the literal equality probability for this support/nonoverlined pair.

## value

PASS

Comparing existing mex conventions on one sample identifies three different behaviors: the overline coordinate stays discrete, the first two rare failure types yield competing Rayleigh clocks, and the macroscopic diagonal mass comes from exact equality with probability one half. These give dependence and a lattice-level coincidence inaccessible from separate means or marginal laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
