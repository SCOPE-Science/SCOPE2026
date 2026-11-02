# Independent mathematical audit

## correctness

PASS

For the target distance R sampled once and held fixed, the conditional Laplace transform is F_R(s)=(r+s)e^{-R sqrt((r+s)/D)}/[s+r e^{-R sqrt((r+s)/D)}]. Differentiation yields E[T|R]=(e^{qR}-1)/r and E[T^2|R]=(2e^{2qR}-(2+qR)e^{qR})/r^2. Integrating against lambda exp(-lambda R) proves the stated first/second moments, finite iff q<lambda and 2q<lambda respectively. Rescaling Y_R=r e^{-qR}T makes its transforms converge uniformly on a small complex neighborhood to 1/(1+w), hence fixed integer moments tend to m!, giving the exact all-moment criterion mq<lambda. Algebraic optimization of 1/[D lambda^2 z(1-z)] yields mean optimum z=1/2; of 1/[z(1-2z)]-1 yields CV optimum z=1/4, CV²=7 and mean cost factor 4/3. Independent symbolic differentiation/integrals verified the finite formulas; divergence and uniqueness follow analytically.

## originality

PASS

Qualified best-of-knowledge assessment after independent statement-level comparisons of the cited specific results, published index and accessible primary texts; inaccessible full texts remain explicitly stated risks, not proof of noncoverage.

## value

PASS

The broad fixed-random-target setting has known mean-optimal Poisson resetting, but a natural reliability question is whether variance remains finite and which rate optimizes dispersion. The sharp integer-moment thresholds, infinite variance at the known mean optimum, and distinct exact CV-optimum with small mean cost are concrete mathematically useful boundary phenomena.

The dated certificate retains the supplied scientific assessment, sources and limitations.
