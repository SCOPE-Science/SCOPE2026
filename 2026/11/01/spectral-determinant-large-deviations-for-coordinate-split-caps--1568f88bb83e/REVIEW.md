# Scientific review

## Correctness (C): PASS

The full proof reconstructs the normalized Gaussian monomial basis and exact two-block independent-gamma distribution. Beta-binomial duality gives every eigenvalue, and stars-and-bars composition counts give multiplicities. The Bernoulli method-of-types lower bound and Chernoff upper bound control the logarithm uniformly at all angular quantum numbers, including endpoints, followed by a bounded-variation Riemann sum. The proof establishes the all-degree leading asymptotic and quantified remainder analytically. Exact finite checker identities and supplementary convergence checks passed; finite testing is not treated as proof of the limit.

## Originality (O): PASS, provisional historical priority

The focal 2023 multivariate Fock Toeplitz paper supplies circle-invariant decomposition. A 2016 projective Toeplitz paper treats torus/radial eigenstructures. Charles–Estienne (2018) gives trace and spectral-window results for characteristic symbols, but its regular trace hypotheses exclude the logarithm at zero. Byun–Park (2024) gives sharper gap asymptotics in the one-complex-dimensional spherical ensemble rather than the multiplicity-weighted dimension-three-and-higher sectors here. A broad earlier large-deviation theorem may cover an implicit expression for this rate; Berman (2008) was inspected only at abstract level, and no absence beyond inspected material is asserted. Earlier single-coordinate and low-dimensional cap diagonalizations are not claimed original.

## Mathematical value (V): PASS

The finite-sector spectral determinant and the equivalent probability of a simultaneous angular gap are natural spectral invariants. Their leading rate cannot be read from bulk spectral counts, because extremely small eigenvalues dominate the logarithm. The explicit relative-entropy integral is a dimension-dependent quantitative law and the bounded remainder controls finite-degree approximation for every fixed cap.

## Limitations and verification

Only fixed parameters and a two-block cap in complex dimension at least three are covered. There is no claim of optimized remainder, other shapes, or varying dimension. Standard-library `verify.py` checks finite exact identities and numerical consistency; specialist historical-priority confirmation and independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
