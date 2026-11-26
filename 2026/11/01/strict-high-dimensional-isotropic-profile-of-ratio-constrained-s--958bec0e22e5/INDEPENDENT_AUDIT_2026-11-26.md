# Independent mathematical audit

## correctness

PASS

Independently checked chamber coordinates: with d_k=x_(k+1)−x_(k), the nonnegative orthant is truncated by Σ D_k d_k≤s, so the contraction of chamber volume is ∏ s(m−k)/D_k and the gamma quotient follows. Conditional uniform barycentric weights have E[W_kW_l]=(1+δ_kl)/(m(m+1)). The resulting trace around c has numerator equal to the sum of squared centered vertex norms plus the squared norm of their sum, giving exactly both terms of R_m after division by the simplex trace (m−1)/(m(m+1)). Permutation symmetry makes the two covariances scalar on the same zero-sum hyperplane. Conditional on order, the rescaled coordinates are uniformly bounded; their means are the Riemann sums for g_s with uniformly bounded error from the single moving jump, and each variance is O_s(1/m). Finite grids and monotonicity give the stated sup-rank convergence. The first R_m term is O_s(1/m) after normalization, and the rest converges to Var(log Z), Z uniform on [1,1+s]. Stirling gives the stated entropy I. Direct differentiation of log F and u=log(1+s) reduce its sign to u sinh u+u²−4(cosh u−1); terms through degree four cancel and all even coefficients beginning at degree six are strictly positive. The small-s expansions and large-s limits give the two endpoints, and substitution gives the quoted trisection limit. Verified at fixed s with the order of limits as stated; neither finite-dimensional monotonicity nor convergence uniform in s is claimed. The frozen script was inspected, not executed.

## originality

PASS

This pass is for the strict isotropic-profile theorem, with its finite-dimensional contraction identity, not for priority on the shape law, limiting covariance, or the bare formula obtainable by combining prior radial and volume asymptotics. Oct. 18 record 26d47f09e2ad already proves the empirical law and extrema at every fixed ratio, which imply the identical uniform-in-rank shape, and its radial limit gives the same covariance limit. The distinct results in the actual finding are the strict comparison across all ratio parameters with exact endpoint range and the exact finite-dimensional moment identity used to derive the profile. Those are not stated by the strongest inspected precedents; an exact limiting expression by itself does not prove the inequality or constrain the finite-dimensional correction.

## value

PASS

The natural affine volume/covariance normalization exhibits a complete, strict interpolation across all fixed ratio constraints, with exact endpoint constants. Showing strictness is substantive because the variance and inverse volume factor change in opposing directions and the leading derivative coefficients cancel. The exact finite-dimensional trace formula also permits quantitative comparison before taking the dimension limit. This is useful even though the earlier typical shape and radial limit themselves are not distinct contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
