# Independent mathematical audit

## correctness

PASS

Independently expand the bin integral about its midpoint v=u+j+1/2. Removing the common KΔ^(1−p), the integral is v^(−p)[1+p(p+1)/(24v²)+O(v^(−4))], since the odd centered moments vanish and the second moment is 1/12. Thus log B_j, up to a common term, is −p log v+p(p+1)/(24v²)+O(v^(−4)). Subtracting adjacent bins gives respectively the third-order coefficients −p(p+14)/12 and −p(p+50)/12 and the two second-order coefficients p and 2p. To justify differentiating the remainder in RESULT.md lines 41–62, use w=1/u: after dropping the common prefactor, the integrals of (1+wx)^(−p) on fixed subintervals of [0,3] and their logarithms are real analytic near w=0 with uniform derivative bounds for p in the stated compact set. Differentiating the Taylor series in p or applying ∂_u=−w²∂_w preserves the required uniform orders. In the ordered columns (p,u), the products in the determinant are −p/u³+5p/u⁴ and −p/u³+4p/u⁴ to that order. Their difference is p/u⁴+O(u^(−5)), and the c column adds the factor 1/Δ. There is no singularity at p=1, and strict positivity is uniform for sufficiently large u on each compact subset of positive p. The inverse function theorem gives the claimed local identification for exact mean ratios, not a stochastic error bound. The frozen symbolic checker was read, not run; it checks coefficients, not the uniform differentiability argument.

## originality

PASS

Bounded pass for the explicit adjacent log-ratio expansions and leading Jacobian coefficient for three consecutive equal-width mean-count bins. Neither the general idea that p and c trade off nor the fact of local injectivity is credited in isolation. Related estimation work and a stronger structural identification result concern different outputs; none of the inspected statements gives the quantitative late-window expansion.

## value

PASS

Three equal adjacent windows are a natural minimal mean-count design after eliminating amplitude with ratios. The leading ratios both depend on the same combination p/u, so the coefficient after cancellation quantifies when the second direction of local information survives; a mere nonzero-determinant claim would miss how rapidly it is lost. For known fixed width this is an explicit local area scaling, useful for comparing noiseless late-window designs. It is not a condition number, likelihood statement, or guarantee of practical precision from observed counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
