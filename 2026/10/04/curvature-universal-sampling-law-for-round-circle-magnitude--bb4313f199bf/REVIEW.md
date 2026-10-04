# Review

## Correctness

PASS. Homogeneity reduces each finite magnitude to the reciprocal of a single row-average of the exponential distance kernel. For \(\kappa<1\), that row-average is exactly a composite trapezoidal rule. The endpoint expansion
\[
D_\kappa(s)=s+\frac{\pi^2(\kappa-1)}6s^3+O(s^5)
\]
gives the first and third derivative jumps of the exponential kernel, and Euler–Maclaurin yields the displayed \(n^{-2}\) and \(n^{-4}\) coefficients. The reciprocal-series calculation gives the magnitude expansion. At \(\kappa=1\), exact geometric sums replace the invalid smooth-midpoint argument and produce the parity split.

The packaged checker independently evaluates the defining finite sums, the Euclidean chord specialization, the smooth two-term residual, and the intrinsic parity formulas. The analytic argument, not the finite checks, establishes the theorem.

## Originality

PASS with a bounded residual risk. The current accessible version of the 2024 regular-polygon/circular-space paper was inspected in its magnitude section and searched for convergence and asymptotic terminology. It gives the homogeneous finite magnitude formula but no sample-count convergence law. The Leinster–Willerton paper was inspected in its Euclidean-circle and round-metric sections. It explicitly passes equal-spacing sums to continuum integrals and records common first and second endpoint derivatives across curvature, but it states no rate in the number of sample points.

Targeted searches combined magnitude with regular polygons, equally spaced circle samples, round metrics, relative curvature, Euler–Maclaurin, convergence rate, and intrinsic parity. No equivalent curvature-resolved sampling expansion or intrinsic even–odd law was located. The main residual risk is that the same elementary asymptotic calculation may appear in unindexed notes under numerical-quadrature terminology.

## Value

PASS. The finite-to-continuum approximation is not auxiliary: it is the mechanism used in the foundational circle-magnitude calculation, and the 2024 work renews interest in regular polygons as magnitude test spaces. The theorem identifies exactly what geometric information the discretization error sees. The universal \(n^{-2}\) term reflects the common local metric normalization, curvature first appears at \(n^{-4}\), and the geodesic endpoint \(\kappa=1\) undergoes a parity transition because antipodal distance ceases to be smooth. This supplies a quantitative bridge between finite regular samples and continuum magnitude across Euclidean, spherical, and hyperbolic round geometries.

Same-model review: passed. Independent audit: not yet performed.
