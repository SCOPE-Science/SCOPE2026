# Independent mathematical audit

## correctness

PASS

Angular orthogonality makes the normalized monomials eigenvectors, with squared monomial norm (α+1)B(k+1,α+1); the numerator has t bounded above by b_m<1, so the beta-normalized eigenvalues tend to zero. For the superlevel bound, H_c(s)=B(s+1,α+1)(λ(s)−c) is analytic for real s>−1, and its integrand sign changes exactly 2m times at the endpoints. If H_c had 2m+1 zeros with multiplicity, their derivative conditions would give orthogonality to a span of 2m+1 functions t^s(log t)^j. After log t these are an exponential Chebyshev family: dividing by a nonvanishing exponential and differentiating reduces the dimension by one and Rolle's theorem bounds the zero count with multiplicity. A nonzero function in the span vanishing at all 2m endpoints must have simple zeros there and none elsewhere, so it can be signed to give a strictly positive integral against the signed weight, contradicting orthogonality. Between consecutive positive components the two sides are positive, requiring at least two zeros counted with multiplicity (including even-order contact); eventual negativity requires one further zero after the last positive component. Thus m+1 components need at least 2m+1 zeros even if the first reaches s=0. Separated discrete blocks also give distinct continuous components by their intervening non-high integer indices. For sharpness set u=(k+1)(1−t); its density is proportional to u^α(1−u/(k+1))^k on (0,k+1), dominated before normalization by u^α exp(−u/2) for k≥1, and the normalized densities converge in L1 to the gamma density. Take 0<A<B with gamma mass in (A,B) greater than c. For K_j=L^{2j}, rings with 1−t in (A/K_j,B/K_j) are disjoint and strictly interior for large L. At k=K_j−1 the same ring contributes the limiting gamma mass and all other rescaled intervals escape toward zero or infinity; at k=L^{2j+1}−1 all do. Strict peaks and valleys hold simultaneously for sufficiently large L, and yield both equality counts. This proves every real α>−1, both interpolations and m=1, without extrapolating from the frozen numerical check, which was inspected but not executed.

## originality

PASS

The diagonal formula and zero-count mechanism are already available; the upper bound is an application of classical variation diminution, not a new general principle. The supported distinct claim is the jointly sharp spectral-component law, including realization at each prescribed threshold and weight in both the continuous and actual lattice spectra. The closest inspected annulus result uses a different space, a local-peak invariant and a different sharpness constraint.

## value

PASS

The number of disjoint annuli limits how many disjoint ranges of angular modes can simultaneously pass a specified concentration cutoff. The construction realizes that full capacity at any threshold and weight, rather than showing isolated multiple peaks that might not cross a common threshold. Separating the scales with both high and low integer witnesses ensures that the bands persist in the actual operator spectrum, not merely its interpolation. This gives a precise achievable design constraint for a natural radial model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
