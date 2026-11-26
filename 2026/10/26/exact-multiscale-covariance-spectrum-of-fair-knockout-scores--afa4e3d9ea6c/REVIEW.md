# Independent mathematical audit

## correctness

PASS

A leaf survives r rounds precisely when its first r independent ancestral choices favor that leaf's path. Two survival paths before the common node use disjoint coins whenever at least one requested survival is below that node; if both reach it, the choices are mutually exclusive. Summing covariances yields the negative square in the claim. Summing (2r-1)2^(-r) gives the second marginal moment; subtracting the squared mean gives the stated variance. With z=1/n and a_h=2^(1-h)-z, constant total wins gives a zero row sum and the subtree contrasts have eigenvalues 2^d a_d^2 plus sum_{h>d} 2^(h-1)a_h^2. Expanding gives 6/2^d-[2(ell-d)+5]/n. Their multiplicities sum to n-1, all are positive, and successive differences are 3/2^d-2/n>0. The extremal Rayleigh bounds follow, including n=2 where both equal 1/2. The permuted deterministic score multiset gives equal diagonal and off-diagonal entries under random labeling and hence one positive eigenvalue nv/(n-1). The fixed weight at level d is 2^(-d); the tail vanishes uniformly in the weak spectral comparison. Bounds 2^(-d)<=lambda_d<=6*2^(-d) dominate the logarithms after weighting, giving per-entrant log pseudodeterminants log(3/2) and log 2 in the limit. Exponentiating their difference gives 3/4. The kernel direction is constant, not a nonzero vector in the zero-sum contrast subspace; the scope wording about a zero-sum direction should be read in this sense, as the finding and proof explicitly say.

## originality

PASS

Random-draw score exchangeability and the deterministic multiset were already explicit, and hierarchical Haar diagonalization is standard. The inspected fixed-bracket dependence results do not state the exact distance-dependent covariance for fair win counts, which is needed to specialize the hierarchical calculation. The supported distinct contribution is that exact kernel and its full spectrum and quantified fixed-versus-random comparison, not the sign or the generic tree diagonalization. No equivalent statement or stronger implication for that full knockout covariance was found in the inspected matching sources.

## value

PASS

The full spectrum quantifies effects not captured by negative dependence alone: final-half contrasts have variance per squared norm 1/n while local contrasts are of order one, and uniform label randomization removes that anisotropy. The exact eigenvalues and limiting geometric mean make the dependence and fixed/random comparison usable beyond a sign result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
