# Independent mathematical audit

## correctness

PASS

Conditional on (V,Z), the Xi are iid N(sqrt(1-2V) Z/2,V). Conditional on V, Xi+Xj is centered Gaussian of variance (1-2V)+2V=1 for every distinct i,j. Direct conditional covariances give diagonal 1/4+EV/2 and off-diagonal 1/4-EV/2. A centered normal variance mixture has fourth cumulant 3 Var((1+2V)/4)=3 Var(V)/4, strictly positive if rho is not a point mass. The difference cancels Z and has conditional char fn exp(-V t^2), the Laplace transform uniquely determines the finite mixing law. Independent Fraction arithmetic checked both explicit examples, including cumulants 0 and 3/256. These are exact algebraic calculations, not a finite experiment in place of a general proof.

## originality

PASS

Zheng–Zhou prove rigidity from JOINT bivariate Gaussianity, which does not follow from a single Gaussian sum and second moments. Evans–Zhou (1999) construct different exchangeable laws sharing EVERY partial-sum distribution, using piecewise-linear characteristic functions, but do not provide Gaussian pair sums or the same-mean covariance match and Laplace-identifying difference family. Newman 2026 addresses finite-coordinate joint marginals and directing-law recovery, not this one-dimensional projection. No exact construction located by targeted semantic searches. Best-of-knowledge novelty limited to this specific natural Gaussian-projection counterfamily, not general nonidentifiability.

## value

PASS

An explicit infinite exchangeable counterfamily locates a sharp observational weakness immediately adjacent to published Gaussian rigidity: scalar Gaussianity of every pair sum plus the whole covariance matrix cannot force Gaussian process structure. The opposing difference law exactly identifies the hidden variance mixing measure. A continuum of laws and explicit Gaussian/non-Gaussian pair give a meaningful testable distinction rather than a routine normalization check; nonidentifiability in general is not newly claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
