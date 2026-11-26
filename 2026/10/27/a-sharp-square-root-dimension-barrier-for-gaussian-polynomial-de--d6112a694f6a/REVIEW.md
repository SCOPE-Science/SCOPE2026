# Independent mathematical audit

## correctness

PASS

In the full Gaussian polynomial space of total degree r, homogeneous harmonic sectors are mutually orthogonal both in norm and after multiplication by the radial objective; quotients combine as convex averages. For d=1 these are even and odd. Substitution t=||x||²/2 gives the compressed multiplication Jacobi matrix with Laguerre parameter d/2+ℓ-1 and size floor((r-ℓ)/2)+1. For fixed degree, increasing the parameter by one size-biases the positive measure p(t)² t^α exp(-t)dt and can only increase its mean by Cauchy–Schwarz. Decreasing the available polynomial degree also cannot improve the minimum. The ℓ=0 sector is therefore globally optimal and the root is multiplied by two. For the all-degree bound, the vectors of lowering and raising actions have squared norms q and q+d, q the mean Hermite degree in [0,r]. Reverse triangle and monotonicity in q prove the claimed bound, including r=0 where the value is d. For d=O(sqrt r), the alternating sine trial vector on the last floor(r^(3/4)) indices has squared norm one and difference energy O(r^(-3/2)); the two zero-boundary edges are included in (61). With j=r/2+O(r^(3/4)) and β=d/2, the Jacobi diagonal minus adjacent off-diagonals is (β-1)²/(2j)+O((d+2)³/j²)=d²/(4r)+o(1) uniformly. The weighted difference energy is O(r^(-1/2)), giving the matching upper side. The lower bound can be rationalized as d²/(sqrt(r+d)+sqrt r)²: it tends to c²/4 at finite c, diverges if d/sqrt r→∞, and stays bounded away from zero on any subsequence with d/sqrt r bounded below. All dimensions, parity cases and the necessity in the arbitrary-sequence claim are covered. The frozen numerical table is corroboration, not a proof or an independent rerun.

## originality

PASS

Credit the known Laguerre extreme-root transition: Krasikov's two-sided, parameter-uniform inequalities already give the sharp critical constant and divergence for the indicated Laguerre zeros after substitution; bounded parameters are handled by classical bounds. The distinct supported finding is the exact identification of the full multivariate Gaussian hierarchy, rather than a radial restriction, and its simple all-(r,d) Gaussian lower bound, placing that spectral behavior in the total-degree hierarchy. The inspected Gaussian hierarchy results cover a fixed-d rate and a univariate exact model, not this characterization with dimension dependence. No originality is credited to the root asymptotics in isolation.

## value

PASS

Dimension-uniform reliability of a total-degree approximation hierarchy is a natural issue even for the simplest radial quadratic. The full-space solution excludes an improvement by nonradial trial polynomials, supplies an exact benchmark at every (r,d), and proves a direct finite-degree barrier. This turns familiar spectral behavior into a concrete failure mode and convergence criterion for the optimization hierarchy, not a new result claimed merely by renaming Laguerre parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
