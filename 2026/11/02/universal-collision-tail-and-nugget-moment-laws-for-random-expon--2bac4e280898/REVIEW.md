# Scientific review

## Correctness — PASS

The tridiagonal Ornstein–Uhlenbeck precision factorization follows directly from independent innovations and is independently reconstructible from the displayed quadratic form. Its isolated short-gap rank-one singularity has spectral coefficient \(1/(\gamma\Delta)\), not a trace coefficient. Bounded continuous iid densities give the exact first-order collision intensity; the probability of two separately short gaps is lower order in the tail calculation after the auxiliary separation cutoff is removed. Layer-cake and Stieltjes integration then give the exact open moment threshold and the regularization constants. The Cauchy–Schwarz equality condition characterizes the optimal continuous iid density. The included exact symbolic and numerical checks corroborate specified finite-dimensional identities, rather than certify the infinite limit.

## Originality — PASS, qualified

Rybicki and Press established the computational significance of exponential-correlation Markov precision; this familiar factorization is not claimed as new. Barnett, Greengard and Rachh study deterministic Matérn covariance approximation and regularized matrix conditioning, not this fixed-\(n\) random-site spectral inverse tail. Barthelmé and Usevich derive kernel spectral behavior under a flattening parameter with fixed sites. Ranjan, Haynes and Karsten address practical near-singularity and nugget remedies, without an inspected exact random-design expectation law. Huang and collaborators study the different minimum kernel and growing-matrix eigenvalue asymptotics; full text access was unavailable, so an overlap risk remains. No directly implying result emerged from the documented mathematical-record and primary-literature searches, but non-discovery does not prove global novelty. A dedicated publication-priority review is still needed.

## Value — PASS

Near-coincident random sites are a practical Gaussian-process matrix-conditioning issue. The result quantifies the exact unavoidable heavy tail rather than merely giving a worst-case spacing estimate: its density functional \(\int w^2\) distinguishes iid sampling designs, supplies a sharp uniform-design extremum, and specifies the precise logarithmic or power-law expected amplification produced as jitter is removed. This is a natural interpretable numerical-stability boundary even without claims about posterior risk or asymptotic optimization of a full inference procedure.

## Scope and residual risks

The density must be continuous on a bounded interval, the kernel exponential, and the sample count fixed; the constants are not claimed for other kernels, correlated sampling, floating-point condition estimates, or prediction error. The priority comparison is incomplete for paywalled specialized random-kernel literature. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
