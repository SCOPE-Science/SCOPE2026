# Independent mathematical audit

## correctness

PASS

The cell Bernoulli variance is computed locally. The curvature term in each n-cell is u²/n, and only O(1) boundary cells per column have nonzero variance, so replacing the curve by its tangent changes the variance sum by O(1). The resulting phase dependence is v_{2i/n}({i²/n}). Complete quadratic Gauss-sum bound |G_n(k,l)|²<=n gcd(2k,n) proves equidistribution for all positive integer n, not only primes. Averaging unit vertical phase gives K(s)=.5 E|s(U1-U2)-(V1-V2)| with two exact rational branches; integrating K(2x) gives target 311/1440+log(2)/24. Independent code directly integrates actual curved boundary cells at grids up to n=4000 and exactly checks the phase-average integral; convergence tests are corroborative only.

## originality

PASS

The exact curved-boundary constant is not implied by inspected star-discrepancy or expected L² discrepancy estimates for jittered samples, which concern different test function classes. Nearby published straight-line and triangular-indicator laws depend on fixed orientation and lattice phase, but do not give complete quadratic-phase equidistribution for the curved y=x² boundary. The calculation is a motivated exact constant for a first nonlinear shape, with meaningful risk of a broad older smooth-boundary theorem.

## value

PASS

The area under y=x² is a natural first genuinely curved discontinuity for square-grid jittered Monte Carlo. Its exact all-grid asymptotic constant, including the log 2 contribution, quantifies geometric and arithmetic effects invisible in generic error-rate bounds and supplies an independently useful benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
