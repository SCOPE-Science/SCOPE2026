# Scientific review

## Correctness — PASS
The product orthonormal basis and kernel are explicit. The separate diagonal and linear polynomial terms have \(O(\sqrt d)\) expected absolute size, whereas the cross-coordinate quadratic term has order \(d\). A bounded triangular-array Lindeberg theorem gives the centered chi-square limit for every sequence with convergent average squared coordinates; the zero-variance alternative follows directly from the mixed-term second-moment bound. Uniform integrability and a compactness argument give the stated spatially uniform law. The support endpoints supply sharp lower-bound evaluation points, and the uniform law identifies every asymptotically maximizing sequence. Exact rational finite-dimensional Gram tests and independent stochastic checks corroborate the algebra, not the infinite proof.

## Originality — PASS, subject to historical priority
Trefethen's 2016 hypercube work fixes approximation spaces and studies analytic approximation convergence as polynomial degree changes, not the endpoint norm of the degree-two continuous orthogonal projector when dimension changes. Caliari–De Marchi–Vianello study discrete hyperinterpolation for a three-dimensional cube and increasing degree, not the continuous projector with fixed total degree and increasing dimension. Closest accessible research-index hits concern second Walsh or Johnson projectors on distinct discrete spaces, and the accessible prior quadratic-ball and affine-cube claims do not imply this symmetric-product variance law. No inspected source establishes the full uniform spatial profile and corner-localization equivalence. Searches are not proofs of novelty; potentially stronger general polynomial-chaos or tensor projection bounds are the main residual risk.

## Value — PASS
The theorem determines the leading worst-case stability of a canonical fixed-total-degree quadratic least-squares projector in arbitrarily high dimension, uniformly across symmetric compact product priors. It identifies a sharp Gaussian coefficient depending only on the variance, not the fourth moment or detailed density, and characterizes all asymptotically worst evaluation locations. This gives an exact limiting answer for Legendre, Chebyshev, a non-Jacobi mixture and a full Jacobi family, at a regime different from the conventional fixed-dimension/high-polynomial-degree literature.

## Limits
No exact finite-dimensional maximum, rate, nonsymmetric extension, or independent publication-priority guarantee is asserted. Same-model reasoning is not independent validation.

Self-review: passed. Independent audit: not yet performed.
