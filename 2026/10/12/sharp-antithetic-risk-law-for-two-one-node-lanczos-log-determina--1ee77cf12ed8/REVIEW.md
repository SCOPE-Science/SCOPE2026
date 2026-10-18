# Independent mathematical audit

## correctness

PASS

PASS: The theorem is for two separately evaluated one-node scalar Lanczos log-Rayleigh outputs, not two-step/block Lanczos. For SPD eigenvalues lambda>mu, the exact factorization R(theta)=a|1+k exp(2i theta)|^2 yields an absolutely uniformly convergent Fourier logarithm. Mean per output log(a) fixes bias B=4 log(cosh(log(kappa)/4)) for every coupling; Parseval gives variance 2 Li_2(k^4) for orthogonal and 4 Li_2(k^2) for independent pairs. Countermonotone quantile rearrangement of the strictly increasing map g(U)=log(mu+(lambda-mu)U), with continuous symmetric Beta(1/2,1/2) marginal, proves global variance/MSE minimality among all couplings and V=1-U equality almost surely. Multiplying orthogonal Rayleigh quotients gives the exact log(1+tau W) arcsine error law. Taylor expansions give 3s^4/128 versus s^2/4; the scalar matrix boundary kappa=1 is exact. An independently implemented 16,384-angle midpoint integration at four contrasts matched bias and both dilogarithm variances to high precision; rational Rayleigh-product identities were separately checked. Integration does not replace the Fourier/rearrangement proof.

## originality

PASS

The countermonotone rearrangement principle itself is classical, and stochastic Lanczos plus orthogonal block probing are established. The single original claim is the complete sharp minimizer and nonlinear-error distribution for exactly two individually Haar one-node log-Rayleigh scalars, with explicit dilogarithm contrast dependence and exact small-contrast order separation. Full inspected primary papers use independently drawn spectral measures or block functions, neither implies this fixed-statistic theorem.

## value

PASS

The fixed two-scalar one-node algorithm is a natural practical low-cost logdet proxy. The theorem gives a mathematically justified optimal coupling, exact bias floor, full error distribution, and fourth-order versus second-order local risk separation while preventing incorrect extrapolation to block/two-step estimators. This goes beyond a routine rearrangement citation because it resolves the optimized nonlinear statistic quantitatively; exact formula and sharp optimizer are useful algorithm-design invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
