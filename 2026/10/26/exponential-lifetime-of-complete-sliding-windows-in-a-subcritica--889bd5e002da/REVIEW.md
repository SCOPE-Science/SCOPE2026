# Independent mathematical audit

## correctness

PASS

At entry the newly appearing color is absent from the M-1 previous common positions; conditional on its identity the common word is uniform onto over N=n-1 symbols. For u<=M-1 the survival probability is sandwiched between Q_N(m-u)/Q_N(m) and that plus (u/n)E[R_u], where R_u is the number of formerly present colors absent from the surviving suffix. Zero-truncated Poisson exact conditioned occupancy law and uniform lattice local CLT give singleton deletion hazard h_N(k)=n^-alpha(1+o(1)) for k=m-O(n^alpha); summing hazards yields exp(-t). Conditional count/suffix estimate E[R_u]=O(u*n^-alpha)=O(1) for u=O(n^alpha), so repair probability O(n^(alpha-1))->0. Exact mean uses stationary on-set mass divided by entry flux, with same singleton-hazard estimate. Independent Fraction enumeration for n,M=(2,3),(3,4),(4,5), u=0,1,2 checks complete entry conditioning and both finite sandwich inequalities. The asymptotic is proved using the uniform local CLT, not finite tests.

## originality

PASS

Best-of-knowledge contribution is the stationary entry-conditioned full exponential episode-lifetime limit and a repair-error comparison. Long 2026 already implies the exact finite mean from its flux and mass, and states a clump-length heuristic; mean alone is prior and is not independently novel. Complete source comparisons did not identify a proved distributional clump law in Long; other scan-statistic declumping general results might imply it.

## value

PASS

The persistence duration of a newly born rare complete window is a natural Palm/clump statistic, distinct from the huge first-coverage waiting time. Proving an Exp(1) distribution on n^alpha time scale and negligible fresh-draw repairs supplies meaningful scan-statistic structure beyond the previously known stationary mean, and may inform other expiring-resource models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
