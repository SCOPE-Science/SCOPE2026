# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 33–77. The unit-square Zak transform is unitary, and each coset gives the ordinary integer-index two-dimensional Fourier coefficient identity for the product with its shifted Zak window. Parseval therefore sums the squared moduli of the shifted Zak windows pointwise; continuity on the torus makes the actual extrema the sharp bounds. For u={x−j/m}, the squared hat Zak modulus is 1−2(1−cos(2πν))u(1−u), so the common maximum is 1 per window at ν=0, and ν=1/2 realizes the minimum for each x. The latter equals four times the sum of squared circle distances from x−1/2. For a lifted center v, choose nearest representatives in [v−m/2,v+m/2], which form a cyclic cut up to common translation, including at ties. Their sum of squared deviations is at least the least cut variance. In the reverse direction, use the mean of any minimizing cut; nearest-representative distances can only decrease from its cut distances. Thus both inequalities give the exact finite formula. For sorted distinct integer lifts, each pair separation is at least its index separation; summing squares gives the bound k(k²−1)/12 for the cut variance, with equality for k≥2 exactly when every consecutive gap is one. This gives the stated mask classification, count, and ratio. The k=1 bound is zero, and for k=m there is only one mask. The inspected source checker reports finite corroboration (2,035 exact mask cases and 1,300 numerical symbol cases), not an all-size proof; it was not executed in this review.

## originality

PASS

The general circle intrinsic-mean calculation and the full-grid frame property are existing mathematics. A later dated catalogue record also gives exactly the same continuous sharp-bound formula for arbitrary real shifts. The distinct contribution supported here is the explicit sharp arithmetic bound after each grid-coset erasure and the exact adversarial bound and all equality masks for every retained cardinality. No inspected earlier result gives the same masked Gabor optimization or implies it as a stated stronger result.

## value

PASS

A user of the periodically thinned Gabor system needs a quantitative lower frame margin, not just frame membership for the unthinned grid. The arithmetic formula gives that exact margin for every surviving pattern, and the adversarial extremum identifies which losses most damage conditioning at fixed retained cardinality. This remains useful beyond the elementary spacing inequality and the already known general circular minimization method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
