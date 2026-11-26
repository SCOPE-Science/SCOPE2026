# Independent mathematical audit

## correctness

PASS

The Schur assumptions make A positive definite. In the stated coordinates the boundary-to-v covariance vanishes. The retained principal block and positive last variance make the compressed covariance positive definite. An independent proof uses the conditional law of (u,v) given q: the marginal of q and the conditional mean agree for both Gaussians; the exact conditional precision is the rotation of the uncorrected T, and the compressed conditional covariance is its inverse with off-diagonal deleted. If r is the conditional correlation, standardizing both variances gives correlation matrix [[1,r],[r,1]] versus the identity, and r^2/(1-r^2) is the squared off-diagonal of the conditional precision divided by det(T). That off-diagonal is c det(T)/(b^2+c^2), proving the stated delta and the two directed KL formulas, including exact coupling invariance and the c=0 criterion. At eigenvalues 1 and kappa the off-diagonal magnitude is at most (kappa-1)/2, with equality exactly at equal diagonals in the aligned basis. The first aligned diagonal is kappa b/(b^2+c^2); solving for equal diagonals gives p=1/(kappa^2+1) for kappa>1. Such orientations admit a positive beta with beta^2/alpha<det(T)/b. The scalar case is exact, and the example has det(S)=epsilon and trace(S)=5/4+epsilon as claimed. The frozen scope paragraph describes u as the normalized direction of the inverse's complement component; literally it is the negative of that normalized vector for beta>0, but the aligned line and compression are unchanged by sign. An independent direct-matrix reproduction of 300 random SPD cases found maximal absolute KL identity errors below 2.1e-15, and corroborated a kappa=3 extremizer and the Schur-boundary family. The uploaded script was inspected, not executed.

## originality

PASS

The distinct supported contribution is the exact law for this coupled compression as a function of its original complement entries, uniform over the admissible boundary coupling, with sharp orientation in that original complement and a fixed-loss Schur-degeneration witness. The compressed covariance construction itself is a specialization of Fifen–Karambal–Hennig (with the same aligned direction); the numeric reverse-envelope function is already known in an overlapping scalar-isotropic problem, and the standardized conditional Gaussian relation is classical. Neither is credited as a separate original claim. They do not supply the required dependence on the uncorrected T for this boundary-aligned operator.

## value

PASS

The smallest case with an actual boundary-to-bulk deletion is a motivated test of how to interpret a coupled Lanczos approximation. The invariant shows which local geometry controls relative entropy, even while the coupling-corrected Schur matrix is made arbitrarily ill-conditioned. This gives a mechanism and a quantitative witness that a Schur-based bound can be very pessimistic; it does not rely on a marginal numeric gain or on reciting the previously known scalar-isotropic envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
