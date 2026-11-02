# Independent mathematical audit

## correctness

PASS

PASS. Under the 2pi Fourier convention, restricting a W-bandlimited function to E gives the integral operator W*sinc(pi W(x-y)); normalizing by mW on L²(E,dx/m) leaves B_epsilon, epsilon=(pi W)^2, with rank-one limit P and spectral gap one. For bounded measurable E and essential diameter D, the kernel Taylor series converges uniformly with operator-norm O(epsilon^4 D^8). Schur-complement perturbation with centered coordinate X and v_1=-(X²-mu_2)/6 gives the coefficients of epsilon, epsilon², and epsilon³, including +23 mu_3²/945, and the eigenvector quadratic term. An independently implemented symbolic moment expansion verified the displayed scalar coefficients and optimizer correction, not just quadrature. Centered-interval rearrangement yields mu_2>=m²/12, strict off intervals, proving the leading W³ shape gap. Uniformity is for WD small; no claim for growing diameters.

## originality

PASS

PASS, best-of-knowledge. The prolate-interval work of Bonami–Karoui studies spectral decay and approximants for the standard interval sinc operator, not a sixth-order centered-moment expansion uniformly over arbitrary bounded measurable sets. Baeza-Guasch studies time-frequency concentration and interval/aliasing comparison at different bandwidth regimes; Faou–Le Hénaff analyze general mask operators but not the assessed explicit asymmetric-set moment polynomial. None of the inspected results yields the presented mu_3² and mu_6 coefficients as a stated or direct closed formula. Older small-bandwidth prolate perturbation literature may overlap, retained as risk.

## value

PASS

PASS. Sharp time-bandwidth concentration is a natural spectral invariant; identifying the first three relative corrections for arbitrary disconnected or nonsymmetric measurable windows, including skewness squared, provides geometric information inaccessible from a bare leading mW approximation. The leading optimizer correction and interval shape gap are mathematical applications, independent of any downstream publication-sized theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
