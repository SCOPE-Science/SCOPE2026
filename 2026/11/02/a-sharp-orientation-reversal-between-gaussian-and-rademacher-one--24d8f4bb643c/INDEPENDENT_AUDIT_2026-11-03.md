# Independent mathematical audit

## correctness

PASS

Cayley–Hamilton for 2x2 B=A^T A gives samplewise residual E(w)=det(B)||w||²/(w^TBw). A Gaussian direction is uniform on the circle, so integrating 1/(lambda cos² phi+mu sin² phi) yields 1/sqrt(lambda mu) and expected sigma1 sigma2. The four sign vectors reduce to two projective directions with Rayleigh quotients s±b; averaging gives D*s/(s²−b²). For fixed eigenvalues |b| ranges 0 to (lambda−mu)/2, proving the sharp harmonic/arithmetic squared-singular-value extrema and their basis equality cases. Solving E_R=E_G yields sin(2theta) cutoff sqrt(sigma1²+sigma2²)/(sigma1+sigma2). Uniform orientation measure gives the arccos fraction, its high-kappa expansion and orientation average. Independently tested direct projector/closed-form identities and numerical orientation cases; analytic proof covers all stated real A.

## originality

PASS

Standard Gaussian rangefinder analyses and non-Gaussian Rademacher sketch bounds are earlier; the 2x2 matrix identity and angular integral are classical. Saibaba–Miedlar (2023/2025) treats larger sketch regimes and high-probability bounds, not an exact fixed-spectrum one-probe Rademacher-versus-Gaussian orientation crossover. The surviving claim is a self-contained exact comparison with equality cases and adverse-orientation measure. An earlier specialized two-dimensional derivation remains possible.

## value

PASS

For fixed singular values, coordinate orientation can make the Rademacher one-probe residual near the optimal rank-one error or quadratic in condition number relative to it, while Gaussian remains linear. The exact all-orientation cutoff and fraction answer a natural small-sample question about two widely used sketch distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
